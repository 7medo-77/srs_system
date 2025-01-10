from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from authentication.models.AuthUser import AuthUser
from django.urls import reverse
from authentication.models.AuthUser import AuthUser

# Log In Controller
def log_in(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Authenticate the user
        resUser = AuthUser.objects.get(id=4)
        print(resUser.username)
        # print(type(resUser.first_name))

        user = authenticate(request, username=username, password=password)
        # user = authenticate(request, id=resUser.id, password=resUser.first_name)

        if user is not None:
            # Check if the user's role matches the selected role
            if user.role == role:
                login(request, user)  # Log the user in
                # Redirect based on role
                if role == 'admin':
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                elif role == 'instructor':
                    return redirect('instructor_dashboard')  # Redirect to instructor dashboard
                elif role == 'student':
                    url = reverse('grading:student-details', kwargs={'user_id': user.user.id})
                    print(url)
                    return redirect(url)  # Redirect to student dashboard
            else:
                return HttpResponse("Role does not match. Please try again.")
        else:
            print(request.body, user)
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'authentication/welcome.html')

# Sign Up Controller
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        role = request.POST.get('role')
        phone_number = request.POST.get('phone_number')

        # Create a new user
        user = AuthUser.objects.create_user(
            username=username,
            password=password,
            email=email,
            role=role,
            phone_number=phone_number
        )
        user.save()
        return redirect('log_in')  # Redirect to login page after sign-up
    return render(request, 'authentication/sign_up.html')

# Log Out Controller
def log_out(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('log_in')  # Redirect to login page after logout