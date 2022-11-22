def Appendtext(fname):
	with open(fname,'a+') as f:
		f.write('appending line 1, ')
		f.write('appending line 2. ')
	f.close()

Appendtext('lab3/file.txt')

x= open('lab3/file.txt')
print(x.read())