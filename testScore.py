import scoring
from book import Book
from library import Library

lib = [Library([Book(0,5),Book(1,3),Book(2,2)],2,1),Library([Book(0,5),Book(3,6),Book(4,1)],1,1)]
print(scoring.scoreAllLibs(lib,4))
