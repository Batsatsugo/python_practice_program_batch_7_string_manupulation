# DECLARE word, prefix, is_starting

# word = input("Enter the word: ")
# prefix = input("Enter the prefix to check: ")
word = input("Enter the word: ")
prefix = input("Enter the prefix to check: ")

# is_starting = True
# IF len(prefix) > len(word):
#     is_starting = False
# ELSE:
#     FOR i in range(len(prefix)):
#         IF word[i] != prefix[i]:
#             is_starting = False
#             BREAK
is_starting = True
if len(prefix) > len(word):
     is_starting = False
else:
     for i in range(len(prefix)):
         if word[i] != prefix[i]:
             is_starting = False
             break

# IF is_starting:
#     PRINT("The word starts with the given prefix.")
# ELSE:
#     PRINT("The word does NOT start with the given prefix.")
if is_starting:
     print("The word starts with the given prefix.")
else:
     print("The word does NOT start with the given prefix.")