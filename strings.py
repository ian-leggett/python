message = "Hello world"

# Character count
print(len(message))

# Access the first character
print(message[0])

# Access the last character
print(message[-1])

# Access a range of characters
print(message[0:5])

# Set message to lowercase
print(message.lower())

# Set message to uppercase
print(message.upper())

# Count how many characters repeat
print(message.count('l'))

# Replace a string
message = message.replace('world', 'uninverse')
print(message)

# Concat strings using F strings
greeting = "Hello"
name = "Ian"

message = f'{greeting} {name}'
print(message)

