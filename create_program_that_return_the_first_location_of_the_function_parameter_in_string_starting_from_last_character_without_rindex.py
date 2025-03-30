# DECLARE word, char, found

# word = input("Enter the word: ")
# char = input("Enter the character to find: ")
word = input("Enter the word: ")
char = input("Enter the character to find: ")

# found = False
found = False

# FOR i in range(len(word) - 1, -1, -1):
#     IF word[i] == char:
#         PRINT(f"The character '{char}' last appears at index {i}.")
#         found = True
#         BREAK
for i in range(len(word) - 1, -1, -1):
     if word[i] == char:
         print(f"The character '{char}' last appears at index {i}.")
         found = True
         break
if not found:
     print(f"The character '{char}' is not found in the word.")