import sys

print("Module search paths:")
for path in sys.path:
    print(f"  {path}")

# Add a custom path (e.g., your web project directory)
sys.path.append('/path/to/your/web/project')
