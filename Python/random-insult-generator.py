
import random

randomBodyParts = ['head', 'arms', 'legs', 'feet', 'toes', 'hips', 'fingers']
randomAdjectives = ['smelly', 'cunt', 'medically challanged', 'silly', 'crazy', 'clorophormic wasting']
randomWords = ['pumbus', 'manbun', 'cunt', 'penis', 'chode', 'hole', 'whore', 'tweater']

randomBodyPart = random.choice(randomBodyParts)
randomAdjective = random.choice(randomAdjectives)
randomWord = random.choice(randomWords)

print('Your ' + randomBodyPart + " looks like a " + randomAdjective + ' ' + randomWord )
input('hit enter to exit')
