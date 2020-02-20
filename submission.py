def submission(libraries,fileName):
    file = open(fileName,"r")
    file.write(len(libraries)+"\n")
    for i in libraries:
        file.write(i.id+" "+len(i.books))
