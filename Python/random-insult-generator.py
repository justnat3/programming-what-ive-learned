
import random
randomBodyParts = ['head', 'arms', 'legs', 'feet', 'toes', 'hips', 'thumbs', 'nails', 'knuckles', 'wrists', 'throat', 'ribs', 'veins', 'skin', 'tongue']

randomAdjectives = ['smelly', 'cunt', 'medically challanged', 'silly', 'crazy', 'clorophormic wasting', '2-faced', 'abnormal', 'aborted', 'abysmal', 'begging', 'bickering', 'bitchy', 'blasphemous','chaotic', 'cheerless']
randomWords = ['pumbus', 'cunt', 'penis', 'chode', 'hole', 'whore', 'tweater']

randomBodyPart = random.choice(randomBodyParts)
randomAdjective = random.choice(randomAdjectives)
randomWord = random.choice(randomWords)

print('Your ' + randomBodyPart + " looks like a " + randomAdjective + ' ' + randomWord )

input('hit enter to exit')