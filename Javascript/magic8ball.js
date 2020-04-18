//Challenge: the user will be able to input a question, then our program will output a random fortune.
// Solution
alert('I am the magic 8 ball, a couple questions before we start...') //Begin the game letting the user know there are questions
const name = prompt('What is your name?: ') // Gets users name
const question = prompt('What is your question?: ') // What is the users question
const answer = Math.floor(Math.random()*20) // generate random number

//return the answer based on the number generated

if (answer === 0){alert('It is Certain. ' + name)}
if (answer === 1){alert('Reply hazy, try again. ' + name)}
if (answer === 2){alert('As I see it, yes. ' + name)}
if (answer === 3){alert('Without a doubt. ' + name)}
if (answer === 4){alert('Outlook good. ' + name)}
if (answer === 5){alert('Most Likely. ' + name)}
if (answer === 6){alert('Don\'t count on it. ' + name)}
if (answer === 7){alert('You may rely on it. ' + name)}
if (answer === 8){alert('Ask again later. ' + name)}
if (answer === 9){alert('Yes. ' + name)}
if (answer === 10){alert('Outlook not so good. ' + name)}
if (answer === 11){alert('My sources say no. ' + name)}
if (answer === 12){alert('Better not tell you now. ' + name)}
if (answer === 13){alert('My reply is no. ' + name)}
if (answer === 14){alert('Cannot predict now. ' + name)}
if (answer === 15){alert('Concentrate and ask again. ' + name)}
if (answer === 16){alert('Yes - Definitely. ' + name)}
if (answer === 17){alert('It is decidedly so. ' + name)}
if (answer === 18){alert('Very Doubtful. ' + name)}
if (answer === 19){alert('Signs point to yes. ' + name)}
if (answer === 20){alert('My sources say yes. ' + name)}
//log it. test it. implement it. 