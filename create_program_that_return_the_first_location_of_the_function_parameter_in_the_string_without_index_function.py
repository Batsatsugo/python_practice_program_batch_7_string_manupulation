# DECLARE word, character, found

# word = input("Enter the word: ")
# character = input("Enter the character to find: ")
word = input("Enter the word: ")
character = input("Enter the character to find: ")

# found = False
found = False

# FOR i in range(len(word)):
#     IF word[i] == character:
#         PRINT(f"The character '{character}' first appears at index {i}.")
#         found = True
#         BREAK
for i in range(len(word)):
     if word[i] == character:
         print(f"The character '{character}' first appears at index {i}.")
         found = True
         break

# IF not found:
#     PRINT(f"The character '{character}' is not found in the string.")
if not found:
     print(f"The character '{character}' is not found in the string.")