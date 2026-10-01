from book import Book


def main():

    print("My Book App")

    book1 = Book('1984', 'George Orwell', 1949)
    print(book1.get_details())

if __name__ == "__main__":
    main()