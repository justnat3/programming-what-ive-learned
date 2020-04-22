
import random
<<<<<<< HEAD
randomBodyParts = ['head', 'arms', 'legs', 'feet', 'toes', 'hips', 'thumbs', 'nails', 'knuckles', 'wrists', 'throat', 'ribs', 'veins', 'skin', 'tongue']

randomAdjectives = ['smelly', 'cunt', 'medically challanged', 'silly', 'crazy', 'clorophormic wasting', '2-faced', 'abnormal', 'aborted', 'abysmal', 'begging', 'bickering', 'bitchy', 'blasphemous','chaotic', 'cheerless']
randomWords = ['pumbus', 'cunt', 'penis', 'chode', 'hole', 'whore', 'tweater']
=======

randomBodyParts = ['head', 'arms', 'legs', 'feet', 'toes', 'hips', 'fingers']
randomAdjectives = ['smelly', 'cunt', 'medically challanged', 'silly', 'crazy', 'clorophormic wasting']
randomWords = ['pumbus', 'manbun', 'cunt', 'penis', 'chode', 'hole', 'whore', 'tweater']
>>>>>>> 6c8e3346aef50d2a156de7346fc6c683d983748b

randomBodyPart = random.choice(randomBodyParts)
randomAdjective = random.choice(randomAdjectives)
randomWord = random.choice(randomWords)

print('Your ' + randomBodyPart + " looks like a " + randomAdjective + ' ' + randomWord )
input('hit enter to exit')
