# DECLARE text, width, zeros_needed

# text = input("Enter the string: ")
# width = int(input("Enter the total width: "))
text = input("Enter the string: ")
width = int(input("Enter the total width: "))

# zeros_needed = width - len(text)
zeros_needed = width - len(text)
# IF zeros_needed > 0:
#     text = "0" * zeros_needed + text
if zeros_needed > 0:
     text = "0" * zeros_needed + text
# PRINT("Zero-filled string:", text)
print("Zero-filled string:", text)