def write_file(libraries):
    fichier = open("outputB.txt", "w")
    fichier.write(str(len(libraries)))
    fichier.write("\n")
    for lib in libraries:
        if len(lib.books)<=0 :
            continue
        fichier.write(str(lib.id) + " " + str(len(lib.books)))
        fichier.write("\n")

        for book in lib.books:
            fichier.write(str(book.id) + " ")
        fichier.write("\n")
    fichier.close()
