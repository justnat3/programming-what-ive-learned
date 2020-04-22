
// console.log('Welcome to my Rock, Paper, Scissors game: ')
// console.log('Please choose on of three options: Bear, Human, or gun: ')
let getUserChoice = (userInput) => {
    // userInput = userInput.toLowerCase();
    if (userInput === 'bear' || userInput === 'human' || userInput === 'gun') {
        return userInput;
    } else {
        return(alert('Please enter valid option'));
    }
}


let computersChoice = () => { // Get Computers Choice
    compOptions = ['gun', 'bear', 'human']
    
    let compInput = compOptions[Math.floor(Math.random()*3)]
        return(compInput)
}


function compareAnswers(getUserChoice, computersChoice){ // Comapre the two 
    if (getUserChoice  === 'bear'){
        if (computersChoice === 'human'){return(' Computer was mauled by a Bear...')}        
    }
    if (getUserChoice  === 'human'){
        if (computersChoice === 'bear'){return(' You were mauled by a bear...')}
    }
    if (getUserChoice  === 'gun'){
        if (computersChoice === 'bear'){return('Computer was killed by your gun...')}
    }
    if (getUserChoice === 'bear'){
        if (computersChoice === 'gun'){return('You were killed by the Computer with a gun...')}
    }
    if (getUserChoice === 'human'){
        if (computersChoice === 'gun'){return('A gun cant\'t kill a human by itself, you win...')}
    }
    if (getUserChoice === 'gun'){
        if (computersChoice === 'human'){return('Your gun can\'t kill a human by itself, The computer wins...')}
    }
    if (getUserChoice === 'human'){
        if (computersChoice === 'human'){return('The two humans vocally battle it out and get no where...')}
    }
    if (getUserChoice === 'bear'){
        if (computersChoice === 'bear'){return('The two bears avoid each other...')}
    }
    if (getUserChoice === 'gun'){
        if (computersChoice === 'gun'){return('You kill eachother.. Draw..')}
    }
}


function playGame() {
    let promptUsesChoice = prompt("Please choose bear, human or gun");
    let userChoice = getUserChoice(promptUsesChoice);
    let compChoice = computersChoice();
    // console.log(userChoice);
    // console.log(compChoice);
    alert(compareAnswers(userChoice, compChoice));
};


playGame()