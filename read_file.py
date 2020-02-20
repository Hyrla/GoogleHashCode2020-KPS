from book import Book
from library import Library
import time


def reading_file(name, books, libraries):
    print("Reading file")
    mon_fichier = open(name, "r")
    content = mon_fichier.readlines()
    nb_books = content[0].split(" ")[0]
    nb_libraries = content[0].split(" ")[1]
    nb_days_scanning = content[0].split(" ")[2]

    for idx, livre in enumerate(content[1].split(" ")):
        new_book = Book(idx, int(livre))
        books.append(new_book)

    for idx, library in enumerate(content[2:]):
        if len(library) > 2:
            print(idx, library)
            if idx % 2 == 0:
                new_library = Library(idx, [], int(library.split(" ")[1]), int(library.split(" ")[2]))
                libraries.append(new_library)
            else:
                libraries[-1].books = []
                temp_list_livres = library.split(" ")
                for num in temp_list_livres:
                    num = int(num)
                    libraries[-1].books.append(books[num])
        #time.sleep(0.01)

    mon_fichier.close()