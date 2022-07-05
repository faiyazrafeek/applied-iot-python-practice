# Python OOP

s = "hello"


print(s.upper())

#count the elements

name = "Mohammed Rafeek Faiyaz Ahamed"



words = list()

words.append('fruits')
words.append('animal')

print(words)


newFile = open('test.txt', 'w')
newFile.write('Sample text here....')

newFile.close()

newFile = open('test.txt', 'r')
print(newFile.read())
newFile.close()



def muls(a,b):
    if a==b or a+b == 5 or abs(a-b) == 5:
        return True
    else:
        False


print(muls(7,5))


colors = ['red', 'green', 'blue']

print('-'.join(colors))