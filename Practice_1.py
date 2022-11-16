"Exercise: 1 (pag 11)"
'Exercise: 1 (pag 11)'
1256983%28
7
"Seven coins will remain to him"
'Seven coins will remain to him'
"Exercise: 2 (pag 16)"
'Exercise: 2 (pag 16)'
12**25%15
12
8 or 3**5 > 100
8
12<8
False
"First question is False"
'First question is False'
5*3**3
135
900/75
12.0
135 != 12
True
"Second question is True"
'Second question is True'
"Exercise: 3 (pag 21)"
'Exercise: 3 (pag 21)'
"[[]] + "PYTHON"
SyntaxError: unterminated string literal (detected at line 1)
"[[]]" + "PYTHON"
'[[]]PYTHON'
"[[]]"[0:2]+"PYTHON"+"[[]]"[2:4]
'[[PYTHON]]'
"Python"[-2]
'o'
"Python"[0:-2]*4
'PythPythPythPyth'
"Python"[-1:-2]
''
"Python"[4:]
'on'
"Python"[-2:]*4
'onononon'
"Perl"[2]*6
'rrrrrr'


"Exercise: 4 (pag 26)"
'Exercise: 4 (pag 26)'
len ("python")
# => 6


"Exercise: 4 (pag 24)"
'Exercise: 4 (pag 24)'
"python"upper(pyt)
# => SyntaxError: invalid syntax
# => "python".upper(pyt)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    "python".upper(pyt)
NameError: name 'pyt' is not defined
"python".upper("pyt")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    "python".upper("pyt")
TypeError: str.upper() takes no arguments (1 given)
"python".upper([0:3])
SyntaxError: invalid syntax
"python".upper('pyt')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    "python".upper('pyt')
TypeError: str.upper() takes no arguments (1 given)
"python"[0:3].upper()+"python"[-3:0]
'PYT'
"python"[0:3].upper()+"python"[-3:]
'PYThon'
3*"python"[:1]
'ppp'
len("python")*"python"[:1]
'pppppp'
len("git")*"git"[:1]
'ggg'




"Exercise: 5 (pag27)"
'Exercise: 5 (pag27)'
print(7+3*2)
13
print('7'+str(3*2))
76
print('7'+'3*2')
73*2
print('7'+3*2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print('7'+3*2)
TypeError: can only concatenate str (not "int") to str
print((7+3)*2)
20
"The error is causing because the semantics of the numbers in every case"
'The error is causing because the semantics of the numbers in every case'



"Exercise: 6 (pag31)"
'Exercise: 6 (pag31)'
your hobby="basketball"
SyntaxError: invalid syntax
your_hobby="basketball"
'My hobby is {0}.'.format{your_hobby}
SyntaxError: invalid syntax
'My hobby is {0}.'.format(your_hobby)
'My hobby is basketball.'
f'My hobby is {your_hobby}.
SyntaxError: unterminated string literal (detected at line 1)
date='2018-11-01'
date
'2018-11-01'
date='01/11'
date
'01/11'

"Exercise: 7 (37)"
'Exercise: 7 (37)'
the favourite one will be the first=['Read books']
SyntaxError: invalid syntax
the_favourite_one_will_be_the_first=['Read books']
the_favourite_one_will_be_the_first.append('Hiking')
the_favourite_one_will_be_the_first.append('Theater')
the_favourite_one_will_be_the_first.append('Puzzles')
the_favourite_one_will_be_the_first.append('Clarinet')
the_favourite_one_will_be_the_first.append('Bastketball')
the_favourite_one_will_be_the_first.append('Writing')
the_favourite_one_will_be_the_first.append('Dancing')
the_favourite_one_will_be_the_first
['Read books', 'Hiking', 'Theater', 'Puzzles', 'Clarinet', 'Bastketball', 'Writing', 'Dancing']
the_favourite_one_will_be_the_first[0]
'Read books'
the_favourite_one_will_be_the_first[4]
'Clarinet'
the_favourite_one_will_be_the_first.del[4]
SyntaxError: invalid syntax
del the_favourite_one_will_be_the_first[4]
the_favourite_one_will_be_the_first
['Read books', 'Hiking', 'Theater', 'Puzzles', 'Bastketball', 'Writing', 'Dancing']
"Exercise: 8 (38)"
'Exercise: 8 (38)'
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
cities
['Brno', 'Ceske Budejovice', 'Hradec Kralove', 'Liberec', 'Olomouc', 'Ostrava', 'Pardubice', 'Plzen', 'Prague', 'Usti nad Labem']
"*".join(cities)
'Brno*Ceske Budejovice*Hradec Kralove*Liberec*Olomouc*Ostrava*Pardubice*Plzen*Prague*Usti nad Labem'

"Excercise: 9 (pag49)"
'Excercise: 9 (pag49)'

print output
import subprocess

