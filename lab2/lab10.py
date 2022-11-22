def Reverse(tuples):
    tup = ()
    for k in reversed(tuples):
        tup = tup + (k,)
    print (tup)
tuples = ('z','a','d','f','g','e','e','k')
(Reverse(tuples))
