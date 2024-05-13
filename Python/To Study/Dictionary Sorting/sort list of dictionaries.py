#sorting 
def sort_books(books):
    sorted_books = sorted(books, key=lambda book: book['author'])
    return sorted_books

#    sorted_items = sorted(items, key=lambda item: item['key']) (sorts by value)




#https://app.programiz.pro/community-challenges/challenge/book-shelf/info

# Problem Title:
# Sorting Books by Author

# Problem Description:
# You are given a list of dictionaries representing books, each containing 'title' and 'author' keys. Your task is to write a Python function sort_books(books) to sort the books alphabetically by the authors' names.

# Function Signature:
# def sort_books(books: List[Dict[str, str]]) -> List[Dict[str, str]]:

# Input:

# books: A list of dictionaries where each dictionary represents a book. Each dictionary contains 'title' and 'author' keys.
# Output:

# Returns a list of dictionaries sorted alphabetically by the authors' names.
# Example:

# python
# Copy code
# books = [
#     {'title': 'Book1', 'author': 'Author2'},
#     {'title': 'Book2', 'author': 'Author1'}
# ]
# sorted_books = sort_books(books)
# print(sorted_books)
# Output:

# css
# Copy code
# [{'title': 'Book2', 'author': 'Author1'}, {'title': 'Book1', 'author': 'Author2'}]
# Constraints:

# The input list books contains at most 10^4 dictionaries.
# Each book dictionary contains at most 100 characters for both 'title' and 'author' keys.
# The 'title' and 'author' values contain only alphanumeric characters and spaces.
