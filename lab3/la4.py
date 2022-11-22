def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='') 

if __name__ == '__main__':
    fname ="lab3/file.txt"  
    N = 1
    try:
        LastNlines(fname,N)
    except:
        print('not found')    
