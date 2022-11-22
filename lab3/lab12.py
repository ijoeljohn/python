names = ['jessa','eric','bob']

with open('lab3/file.txt','w') as fp:
    for item in names:
        fp.write("%s\n" % item)

    print('done')    