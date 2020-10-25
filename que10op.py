#


import pickle
f=open('joke.dat','ab+')
l=[]
a=int(input('id: '))
b=input('type: ')
c=input('desc: ')
l.append(a)
l.append(b)
l.append(c)
print('before adding')
f.seek(0)
try:
 while True:
     n=pickle.load(f)
     print(n)
except EOFError:
 None
pickle.dump(l,f)
print('after adding')
f.seek(0)
try:
 while True:
     n=pickle.load(f)
     print(n)
except EOFError:
 f.close()

'''Output:
id: 2
type: rom
desc: taylor swift is bad
before adding
[1, 'comedy', "no it isn't funny"]
[2, 'romance', 'taylor swift is cricketer']
after adding
[1, 'comedy', "no it isn't funny"]
[2, 'romance', 'taylor swift is cricketer']
[2, 'rom', 'taylor swift is bad']
'''