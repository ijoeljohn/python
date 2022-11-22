from itertools import islice
file = "lab3/file.txt"
enter = int(input('enter some random number = '))
with open(file,'r') as filecontent:
    for fline in islice(filecontent,enter):

        print(fline)