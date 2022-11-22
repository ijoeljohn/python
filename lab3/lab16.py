filename = "lab3/file.txt"
with open (filename,'r') as filecontent:
    lines_list = filecontent.readlines()
    print([a.replace('\n','') for a in lines_list])