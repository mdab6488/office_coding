import requests

print("Requests module contents:")
print(dir(requests))

# Show only public members
public_members = [m for m in dir(requests) if not m.startswith('_')]
print(public_members)
