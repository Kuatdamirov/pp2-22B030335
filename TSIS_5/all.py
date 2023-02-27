import re 
s='abb Hello, my name_is Kuat. ILearn python! ab abb'
#1
print(1, re.match(r'ab*', s))
#2
print(2, re.match(r'ab{2,3}', s))
#3
print(3, re.search(r'[a-z]+_[a-z]+', s))
#4
print(4, re.search(r'[A-Z][a-z]+', s))
#5
print(5, re.search(r'^a.*b$', s))
#6
print(6, re.sub('\s', ':', s))
print('6_2', re.sub("[ ,.]", ":", s))
#8
print(8, re.split('[A-Z]', s))
#9
print(9, re.sub(r"(\w)([A-Z])", r"\1 \2", s))