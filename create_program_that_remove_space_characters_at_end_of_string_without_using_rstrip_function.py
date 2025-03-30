# DECLARE word, index, trimmed_word

# word = input("Enter a word: ")
word = input("Enter a word: ")

# index = len(word) - 1
# WHILE i >= 0 and word[i] == " ":
#     i -= 1
index = len(word) - 1
while index >= 0 and word[index] == " ":
    index -= 1

# trimmed_word = word[:i + 1]
# PRINT("Trimmed word:", trimmed_word)
trimmed_word = word[:index + 1]
print("Trimmed word:", trimmed_word)
