import read_file
import scoring

books = []
libraries = []

nbDays = read_file.reading_file("a_example.txt", books, libraries)
print(books)
print(libraries)
print(scoring.scoreAllLibs(libraries,nbDays))
