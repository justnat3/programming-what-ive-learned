print('Stories: A New Toy, Day at the Zoo')

userInput = input('pick a story:')
usrChoice = userInput.lower()

if usrChoice == 'a new toy':
    print('There is a new toy on the market that has everyone saying (exclamation)! It is called the (sound) (adjective) (noun) box and will be in stores in (a Month). the (sound) (adjective) (noun) box is a new gadget that lets you do just about anything! It (verb)s, it (verb)s, it even serves (a Drink)! It is easy to operate and requires no instructions! You can also haveit custom made to be any size you want up to (integer) inches and (color) or glow in the darkwith no extra charge! The original product is pocket-sized and (color) there are (integer) jacks on the product for 6V DC power and for upgrades and add-ons. You can add headphones, (plural Noun) monitors, (plural Noun), and more, and use them all at the same time!')

    exclamation = input('Everyone saying ___ !:  ')
    sound = input('Pick a Sound: ')
    adj = input('Pick a adjective: ')
    noun = input('Pick a Noun: ')
    aMonth = input('Pick a Month: ')
    sound2 = input('Pick another Sound: ')
    adj2 = input('Pick another adjective: ')
    noun2 = input('Pick another Noun: ')
    verb = input('Pick a verb: ')
    verb2 = input('Pick another verb: ')
    aDrink = input('Pick a Drink: ')
    integer = input('Pick a number: ') #as a string
    color = input('Pick a color: ')
    color2 = input('Pick another color: ')
    integer2 = input('Pick another number: ')#as a string
    pluralNoun = input('Pick a Plural Noun: ')
    pluralNoun2 = input('Pick another Plural Noun: ')

    print('There is a new toy on the market that has everyone saying ' + exclamation + '! It is called the ' + sound + '' + adj + ' ' + noun + ' box and will be in stores in ' + aMonth + '. the ' + sound2 + ' ' + adj2 + ' ' + noun2 + ' box is a new gadget that lets you do just about anything! It ' + verb + 's, it ' + verb2 +'s, it even serves ' + aDrink + '! It is easy to operate and requires no instructions! You can also have it custom made to be any size you want up to ' + integer + ' inches and ' + color + ' or glow in the dark with no extra charge! The original product is pocket-sized and ' + color2 +  'there are ' + integer2 + ' jacks on the product for 6V DC power and for upgrades and add-ons. You can add headphones, ' + pluralNoun + ', monitors, ' + pluralNoun2 + ', and more, and use them all at the same time!')

else:
    print('\nThat is not a story in our cataloge\n')

if usrChoice == 'day at the zoo':

    print('\nToday I went to the zoo. I saw a __adjective__  __noun__ jumping up and down in its tree. He __verbPastTense__  __adverb__ through the large tunnel that led to its __adjective__ __noun__. I got some peanuts and passed them through the cage to a gigantic gray __noun__ towering above my head. Feeding that animal made me hungry. I went to get a __adjective__ scoop of ice cream. It filled my stomach. Afterwards I had to __verb__ __adverb__ to catch our bus. When I got home I __verbPast__ my mom for a __adjective__ day at the zoo.\n' )

    adj = input('Pick a adjective: ')
    noun = input('Pick a Noun: ')
    verbPast = input('Pick a verb in the past tense: ')
    adverb = input('Pick a adverb: ')
    adj2 = input('Pick another adjective: ')
    noun2 = input('Pick another Noun: ')
    noun3 = input('Pick another Noun: ')
    adj3 = input('Pick another adjective: ')
    verb = input('Pick another verb: ')
    adverb2 = input('Pick a adverb: ')
    verbPast2 = input('Pick another verb: ')
    adj4 = input('Pick another adjective: ')

    print('\nToday I went to the zoo. I saw a ' + adj + ' ' + noun + ' jumping up and down in its tree. He ' + verbPast + ' ' + adverb + ' through the large tunnel that led to its ' + adj2 + ' ' + noun2 + '. I got some peanuts and passed them through the cage to a gigantic gray ' + noun3 + ' towering above my head. Feeding that animal made me hungry. I went to get a ' + adj3 + ' scoop of ice cream. It filled my stomach. Afterwards I had to ' + verb + ' ' + adverb2 + ' to catch our bus. When I got home I ' + verbPast2 + ' my mom for a ' + adj4 + ' day at the zoo.\n' )





