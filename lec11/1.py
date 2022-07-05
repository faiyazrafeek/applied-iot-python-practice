#basic for loops

for i in [1,2,3]:
    print(i)


for color in ['red', 'green', 'blue']:
    print(color)

#simple repeat loops

for i in range(1,11):
    print(i, 'Hello')

#accumulation loops

def sumList(nums):
    '''Return the sum of the numbers in the list'''

    sum = 0
    for i in nums:
        sum+=i
    
    return sum


print(sumList([2,3,5,7]))


def evenPrint(name):
    for i in range(0, len(name), 2):
        print(name[i])


evenPrint('Faiyaz')