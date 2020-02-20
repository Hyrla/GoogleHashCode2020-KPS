def scoreLib(library, total_days):
    Dscan = total_days - library.nb_day
    library.books.sort(key=lambda x:x.score)
    NbookScannable = library.nb_scan_by_days * Dscan
    score = 0
    for i, book in enumerate(library.books):
        if i < NbookScannable:
            score += book.score
        else:
            break
    return score

def isInLib(library,id):
    for i in library.books:
        if i.id == id:
            return True
    return False

def scoreAllLibs(libraries, total_days):
    libToScan = []
    while len(libraries) > 1:
        for i in libraries:
            i.max_score = scoreLib(i,total_days)
        libraries.sort(key = lambda x:x.max_score)
        libToScan.append(libraries[0])
        libraries.pop(0)
        for i in libraries:
            #print(i.books)
            i.books = [item for item in i.books if not isInLib(libToScan[-1],item.id)]
            #print(i.books)
    libToScan.append(libraries[0])
    return libToScan
