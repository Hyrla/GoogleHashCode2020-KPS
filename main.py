import read_file
import scoring
import submission

books = []
libraries = []

nbDays = read_file.reading_file("a_example.txt", books, libraries)
print(books)
print(libraries)
librariesInput = libraries[:]
print(scoring.scoreAllLibs(librariesInput,nbDays))
print(libraries)
