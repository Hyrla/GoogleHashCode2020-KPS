import read_file
import scoring
import write_file

books = []
libraries = []

nbDays = read_file.reading_file("a_example.txt", books, libraries)
print(books)
print(libraries)
#librarie = libraries[:]
libToScan = scoring.scoreAllLibs(libraries,nbDays)
#print(libToScan)
write_file.write_file(libToScan)
