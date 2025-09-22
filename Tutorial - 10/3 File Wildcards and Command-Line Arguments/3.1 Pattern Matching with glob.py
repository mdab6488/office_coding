# The glob module makes file pattern matching simple using Unix-style wildcards, which is invaluable for web applications that need to process batches of files or find assets matching specific patterns.

import glob

# Find all Python files in current directory
python_files = glob.glob('*.py')
print(f"Python files: {python_files}")

# Find all JSON files (useful for loading configuration)
config_files = glob.glob('*.json')
print(f"JSON files: {config_files}")

# Recursive search for image files
image_files = glob.glob('**/*.png', recursive=True) + \
              glob.glob('**/*.jpg', recursive=True) + \
              glob.glob('**/*.gif', recursive=True)
print(f"Image files: {image_files}")

# Process all text files in a directory
for file_path in glob.glob('content/*.txt'):
    with open(file_path, 'r') as f:
        content = f.read()
        # Process content for web display
    
# This functionality is particularly useful for static site generators or content management systems that need to process groups of files with specific extensions 