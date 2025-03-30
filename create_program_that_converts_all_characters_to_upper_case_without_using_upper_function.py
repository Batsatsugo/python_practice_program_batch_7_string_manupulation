# DECLARE word, uppercase_word

# word = input("Enter a word: ")
word = input("Enter a word: ")

# uppercase_word = ""
# for char in word:
#     if 'a' <= char <= 'z':
#         uppercase_word += chr(ord(char) - 32)
#     else:
#         uppercase_word += char
uppercase_word = ""
for char in word:
    if 'a' <= char <= 'z':
        uppercase_word += chr(ord(char) - 32)
    else:
         uppercase_word += char
# print("Uppercase word:", uppercase_word)
print("Uppercase word:", uppercase_word)