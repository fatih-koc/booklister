import argparse

class Library:

    def __init__(booktxt):
        
        with open(f'./{booktxt}.txt', 'w') as textfile:
            books = textfile.readlines()
            return books

    # def __del__():
    #     pass

    # def listBooks():
    #     pass

    # def addBook():
    #     pass

    # def removeBook():
    #     pass



Library('books')

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     try:
#         parser.add_argument("--add", help="Add a book", type=str)
#         books = parser.parse_args()
#         print(books.add)
#     except:
#         print("No books added")


#     try:
#         parser.add_argument("--remove", help="Remove a book", type=str)
#         books = parser.parse_args()
#         print(books.remove)
#     except:
#         print("No books removed")


    # books_to_add = add_book.get(args.add_book,"")





