#!/bin/bash

# Output file
# OUTPUT_FILE="concatenated_django_project.txt"
OUTPUT_FILE="concatenated_urls.txt"

# Clear the output file if it exists
>"$OUTPUT_FILE"

# Define directories and files to exclude
EXCLUDE_DIRS=("env" "venv" "__pycache__" "migrations" "static" "media" "node_modules" "django_env")
EXCLUDE_FILES=("*.env" "*.ini" "*.yml" "*.yaml" "*.txt" "*.md" "*.json" "*.sqlite3")

# Function to check if a file should be excluded
should_exclude() {
  local file=$1

  # Check if the file is in an excluded directory
  for dir in "${EXCLUDE_DIRS[@]}"; do
    if [[ $file == *"/$dir/"* ]]; then
      return 0
    fi
  done

  # Check if the file matches an excluded pattern
  for pattern in "${EXCLUDE_FILES[@]}"; do
    if [[ $file == $pattern ]]; then
      return 0
    fi
  done

  return 1
}

# Find all Python files and concatenate them
find . -type f -name "urls.py" | while read -r file; do
  if ! should_exclude "$file"; then
    echo "=== $file ===" >>"$OUTPUT_FILE"
    cat "$file" >>"$OUTPUT_FILE"
    echo -e "\n\n" >>"$OUTPUT_FILE"
  fi
done

echo "All project files have been concatenated into $OUTPUT_FILE"
