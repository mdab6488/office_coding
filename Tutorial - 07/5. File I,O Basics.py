# Web development often involves reading config files or processing uploaded data.

"""🔹 Reading Files"""
with open('config.txt', 'r') as file:
    content = file.read()
    print(content)

# Read Line by Line:
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes trailing newlines

"""🔹 Writing Files"""
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
    
# Web Context: Saving uploaded files:
# Simulating saving an uploaded image
uploaded_data = b"fake_binary_data"
with open('uploaded_image.png', 'wb') as file:
    file.write(uploaded_data)
