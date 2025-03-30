# DECLARE word, width, space_needed

# word = input("Enter the word: ")
# width = int(input("Enter the total width: "))
word = input("Enter the word: ")
width = int(input("Enter the total width: "))

# spaces_needed = width - len(word)
# IF spaces_needed > 0:
#     word = " " * spaces_needed + word
spaces_needed = width - len(word)
if spaces_needed > 0:
     word = " " * spaces_needed + word

# PRINT("Right-justified word:", word)
print("Right-justified word:", word)