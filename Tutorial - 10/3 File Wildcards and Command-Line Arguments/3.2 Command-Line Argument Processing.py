# Web development tools often need to process command-line arguments for configuration, and Python provides two main modules for this purpose: sys for simple cases and argparse for complex interfaces.

"""3.2.1 Basic Argument Processing with sys"""
import sys

# Simple command-line argument processing
# Run with: python script.py arg1 arg2 arg3
print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")

# Typical usage in web development scripts
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == 'start-server':
        print("Starting server...")
    elif command == 'deploy':
        print("Deploying application...")
    else:
        print(f"Unknown command: {command}")
        
"""3.2.2 Advanced Argument Processing with argparse"""
import argparse

# Create argument parser for a web development utility
parser = argparse.ArgumentParser(
    prog='site-builder',
    description='Static site generator tool'
)

# Add arguments
parser.add_argument('action', choices=['build', 'deploy', 'clean'],
                   help='Action to perform')
parser.add_argument('--output', '-o', default='dist',
                   help='Output directory (default: dist)')
parser.add_argument('--verbose', '-v', action='store_true',
                   help='Enable verbose output')
parser.add_argument('--config', '-c', default='config.json',
                   help='Configuration file (default: config.json)')

# Parse arguments
args = parser.parse_args()

# Use arguments in web development context
print(f"Performing action: {args.action}")
print(f"Output directory: {args.output}")
if args.verbose:
    print("Verbose mode enabled")
    
# The argparse module is particularly useful for creating administrative scripts for your web applications, such as deployment tools, database migration scripts, or content management utilities 