with open("lab3/file.txt",'r') as fp:
    lines = len(fp.readlines())
    print('total number of lines:', lines)