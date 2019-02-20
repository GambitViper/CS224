from os import listdir

contains = [f for f in [rs for rs in listdir('datafiles')] 
                if f+".rand" in listdir('datafiles/'+f)]
print contains
print

evens = [f for f in [rs for rs in listdir('datafiles')] 
            if int(f.split('.')[1]) % 2 == 0]
print evens
print

pairs = [(f1, f2) for f1 in [rs for rs in listdir('datafiles')] for f2 in [rs for rs in listdir('datafiles')] 
            if (int(f1.split('.')[1]) + int(f2.split('.')[1]))% 100 == 0]
print pairs
print


