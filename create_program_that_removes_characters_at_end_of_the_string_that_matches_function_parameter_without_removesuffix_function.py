# DECLARE word, suffix

# word = input("Enter a word: ")
# suffix = input("Enter the suffix to remove: ")
word = input("Enter a word: ")
suffix = input("Enter the suffix to remove: ")

# IF word.endswith(suffix):
#     word = word[:len(word) - len(suffix)]
if word.endswith(suffix):
    word = word[:len(word) - len(suffix)]

# PRINT("Modified word:", word)
print("Modified word:", word)