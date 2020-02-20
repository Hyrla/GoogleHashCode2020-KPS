def write_file(libraries):
    fichier = open("output.txt", "w")
    fichier.write(str(len(libraries)))
    fichier.write("\n")
    for lib in libraries:
        fichier.write(str(lib.id) + " " + str(len(lib.books)))
        fichier.write("\n")

        for book in lib.books:
            fichier.write(str(book.id) + " ")
        fichier.write("\n")
    fichier.close()
