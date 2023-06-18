from typing import Set, Union, Dict, Optional, List


# TODO task 1

# def caesar_cipher(text: str, shift: int) -> str:
#     encrypted_text = ''
#     for char in text:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
#             encrypted_text += encrypted_char
#         else:
#             encrypted_text += char
#
#     return encrypted_text
#
#
# shift = int(input("Enter the encryption shift: "))
# text = input("Enter the text to encrypt: ")
#
# encrypted_text = caesar_cipher(text, shift)
# print("Encrypted text:", encrypted_text)


# TODO task 2

# fruit_input = input('Enter a fruit: ').lower()
#
# fruits_tuple = ('apple', 'apple', 'anime', 'anime', 'watermelon', 'strawberry', 'pear', 'anime', 'anime', 'animemango')
#
# fruit_count = 0
#
# for fruit in fruits_tuple:
#     if fruit_input in fruit:
#         fruit_count += 1
#
# if fruit_count <= 1:
#     fruit_input = fruit_input
# else:
#     fruit_input = fruit_input + 's'
#
# print(f'You have: {fruit_count} {fruit_input}')

# TODO task 4

# manufacturers_tuple = ("ford", "toyota", "honda", "toyota", "chevrolet", "toyota", "bmw")
#
# manufacturer_name = input("Enter the name of the manufacturer to replace: ").lower()
# replacement_word = input("Enter the replacement word: ")
#
# replaced_tuple = tuple(
#     replacement_word if manufacturer.lower() == manufacturer_name else manufacturer for manufacturer in
#     manufacturers_tuple)
#
# print("Replaced tuple:", replaced_tuple)

# TODO task 5

# def superset(set1: Set[Union[int, str]], set2: Set[Union[int, str]]) -> str:
#     if set1 == set2:
#         return "The sets are equal."
#     elif set1.issuperset(set2):
#         return f"Object {set1} is a pure superset."
#     else:
#         return "No superset detected."
#
#
# print(superset({1, 2, 3, 4}, {2, 4}))
# print(superset({1, 2, 3, 4}, {1, 2, 3, 4}))
# print(superset({1}, {1, 2, 3, 4}))

# TODO task 6

# def add_word(dictionary: Dict[str, str], word: str, translation: str) -> None:
#     dictionary[word] = translation
#     print(f"Added '{word}' with translation '{translation}' to the dictionary.")
#
#
# def remove_word(dictionary: Dict[str, str], word: str) -> None:
#     if word in dictionary:
#         del dictionary[word]
#         print(f"Removed '{word}' from the dictionary.")
#     else:
#         print(f"'{word}' does not exist in the dictionary.")
#
#
# def search_word(dictionary: Dict[str, str], word: str) -> None:
#     translation = dictionary.get(word)
#     if translation is not None:
#         print(f"'{word}' translation: '{translation}'")
#     else:
#         print(f"'{word}' not found in the dictionary.")
#
#
# def replace_word(dictionary: Dict[str, str], word: str, new_translation: str) -> None:
#     if word in dictionary:
#         dictionary[word] = new_translation
#         print(f"Replaced '{word}' translation with '{new_translation}'.")
#     else:
#         print(f"'{word}' not found in the dictionary.")
#
#
# dictionary: Dict[str, str] = {}
#
# while True:
#     print("English-French Dictionary")
#     print("1. Add word")
#     print("2. Remove word")
#     print("3. Search word")
#     print("4. Replace word")
#     print("5. Quit")
#
#     choice: str = input("Enter your choice (1-5): ")
#
#     if choice == "1":
#         word = input("Enter the English word: ")
#         translation = input("Enter the French translation: ")
#         add_word(dictionary, word, translation)
#     elif choice == "2":
#         word = input("Enter the English word to remove: ")
#         remove_word(dictionary, word)
#     elif choice == "3":
#         word = input("Enter the English word to search: ")
#         search_word(dictionary, word)
#     elif choice == "4":
#         word = input("Enter the English word to replace: ")
#         new_translation = input("Enter the new French translation: ")
#         replace_word(dictionary, word, new_translation)
#     elif choice == "5":
#         print("Thank you for using the dictionary. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option (1-5).")


# TODO task 7

# def set_gen(numbers: List[int]) -> Set[str]:
#     unique_set: Set[str] = set()
#     count_dict = {}
#
#     for num in numbers:
#         if num in count_dict:
#             count = count_dict[num]
#             count_dict[num] += 1
#             unique_set.add(str(num) * (count + 1))
#         else:
#             count_dict[num] = 1
#             unique_set.add(str(num))
#
#     return unique_set
#
#
# print(set_gen([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
