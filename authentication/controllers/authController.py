# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse
# from authentication.models.AuthUser import AuthUser
# import csv

# # # Sign Up Controller
# # def sign_up(request):
# #     if request.method == 'POST':
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #         email = request.POST.get('email')
# #         role = request.POST.get('role')
# #         phone_number = request.POST.get('phone_number')
# #         # Create a new user
# #         user = AuthUser.objects.create_user(
# #             username=username,
# #             password=password,
# #             email=email,
# #             role=role,
# #             phone_number=phone_number
# #         )
# #         user.save()
# #         return redirect('sign_in')
# #     return render(request, 'authentication/sign_up.html')

# # Sign In Controller
# def sign_in(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         role = request.POST.get('role')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirect to a dashboard or home page
#         else:
#             return HttpResponse("Invalid credentials")
#     return render(request, 'authentication/sign_in.html')

# # Logout Controller
# def sign_out(request):
#     logout(request)
#     return redirect('sign_in')

# # Recursive Function to Generate User Report (CSV)
# def generate_user_report(users, file, depth=0):
#     if depth == 0:
#         writer = csv.writer(file)
#         writer.writerow(['Username', 'Email', 'Role', 'Phone Number'])
#     for user in users:
#         writer = csv.writer(file)
#         writer.writerow([user.username, user.email, user.role, user.phone_number])
#         if user.role == 'admin':  # Example of recursion: Process admins differently
#             generate_user_report(AuthUser.objects.filter(role='admin'), file, depth + 1)

# # Export User Report to CSV
# def export_user_report(request):
#     users = AuthUser.objects.all()
#     with open('user_report.csv', 'w', newline='') as file:
#         generate_user_report(users, file)
#     return HttpResponse("User report exported to CSV.")

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
                    url = reverse('grading:student-details', kwargs={'student_id': user.id})
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