# DECLARE word, all_lowercase

# word = input("Enter a word: ")
word = input("Enter a word: ")

# all_lowercase = True
# FOR char in word:
#     IF 'A' <= char <= 'Z':
#         all_lowercase = False
#         BREAK
all_lowercase = True
for char in word:
     if 'A' <= char <= 'Z':
         all_lowercase = False
         break
if all_lowercase:
    print("The word is completely in lowercase.")
else:
    print("The word is not completely in lowercase.")