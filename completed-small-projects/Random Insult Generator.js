
//What does the computer need to know?

//Random Body Parts
let randomBodyParts = ['head', 'arms', 'legs', 'feet', 'toes', 'hips'] 
//random Describing words
let randomAdjectives = ['smelly', 'cunt bearing', 'medically challanged', 'silly', 'crazy', 'clorophormic wasting']
//random words for discribing 
let randomWords = ['pumbus', 'manbun', 'cunt', 'penis', 'chode', 'hole', 'whore', 'tweater']
//randomize body part
let randomBodyPart = randomBodyParts[Math.floor(Math.random()*5)]
//randomize adjective
let randomAdjective = randomAdjectives[Math.floor(Math.random()*6)]
//randomize words
let randomWord = randomWords[Math.floor(Math.random()*8)]
//output
alert('Your ' + randomBodyPart + " looks like a " + randomAdjective + ' ' + randomWord )

// your arms are like a smelly manbun
