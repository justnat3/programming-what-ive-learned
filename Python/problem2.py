
input('Please type a string:')

def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for alphabet in inputStr:
        if alphabet in vowels:
            num_vowels = num_vowels + 1 
    return num_vowels

str1 = "I really do not know what I am talking about"
print(getCount(str1))
