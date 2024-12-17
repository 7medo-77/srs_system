#!/bin/bash

# Define the output file
OUTPUT_FILE="all_concatenated.py"

# Clear the output file if it already exists
>"$OUTPUT_FILE"

# Loop through all Python files in the directory
for file in *.py; do
  # Skip the output file, __init__.py, and seed.py
  if [[ "$file" != "$OUTPUT_FILE" && "$file" != "__init__.py" && "$file" != "seed.py" ]]; then
    echo "Processing $file..."

    # Add a comment indicating the source file being appended
    echo -e "\n# --- Start of $file ---\n" >>"$OUTPUT_FILE"

    # Append the content of the file to the output file
    cat "$file" >>"$OUTPUT_FILE"

    # Add a comment indicating the end of the source file
    echo -e "\n# --- End of $file ---\n" >>"$OUTPUT_FILE"
  fi
done

echo "All Python files have been concatenated into $OUTPUT_FILE"
