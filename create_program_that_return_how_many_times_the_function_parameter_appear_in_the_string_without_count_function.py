# DECLARE word, character, count

# word = input("Enter the word: ")
# character = input("Enter the character to count: ")
word = input("Enter the word: ")
character = input("Enter the character to count: ")

# count = 0
count = 0

# FOR c in word:
#     IF c == character:
#         count += 1
for c in word:
     if c == character:
         count += 1
# PRINT(f"The character '{character}' appears {count} times in the word.")
print(f"The character '{character}' appears {count} times in the word.")