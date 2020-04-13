# programming-what-ive-learned
Journey Through Learning Programming


Definition: 
"Strings are a data type used to represent text and are wrapped in either a single or double quotes."
"A list of characters surrounded by quotes, used to represent text in computer programs."
"Strings in JavaScript (as in most programming languages) are just sequences of characters, which can include letters, numbers, punctuation, and spaces. We put strings between quotes so JavaScript knows where they start and end."Example
	* 
Single quote: var name = 'Joe';
	* 
Double quote: var name = "Joe";

Best Practice
	* 
Choose one implementation, either single or double quote, and use consistently.
	* 
Teams will often have agreed upon style guide.

Error 
	* 
Single and double quote: var name = 'Joe";
	* 
Double and single quote: var name = "Joe';

Turn Any Data Type Into a String


	1. 
typeof 24; // 'number' 
	2. 
typeof '24'; // 'string'
	3. 
typeof true; // 'boolean'
	4. 
typeof 'true'; // 'string'

Single or Double Quotes Within Strings
	* 
Error

		* 


var greeting = 'It's good to meet you!';
Single quote within text wrapped in single quotes.
		* 


var greeting2 = "Tell Jack that I say "Hi"";
Double quotes within text wrapped in double quotes.
	* 
Solution

		* 


var greeting = "It's good to meet you!";
Single quote within double quotes.
		* 


var greeting2 = 'Tell Jack that I say "Hi"';
Doubles quotes within single quotes.
	* 
Escape Clause Solution

		* 


var greeting = 'It\'s good to meet you!';
Escape clause used before single quote within text wrapped in single quotes.
		* 


var greeting2 = "Tell Jack that I say \"Hi\""; 
Escape clause used before double quotes within text wrapped in double quotes.


Looking Ahead - Future Lessons
	* 
Joining Strings


		1. 
var greeting = "Hi,";
		2. 
var myName = "Rob";
		3. 
greeting + " " + myName; // "Hi, Rob"

	* 
Finding the Length of a String


		1. 
var neighborGreeting = "Hi, Rob";
		2. 
neighborGreeting.length; // 7

	* 
Getting a Single Character from a String


		1. 
var neighborGreeting = "Hi, Rob";
		2. 
neighborGreeting[0]; // "H"
		3. 
neighborGreeting[1]; // "i"

	* 
Upper Case


		1. 
var neighborGreeting = "Hi, Rob";
		2. 
neighborGreeting.toUpperCase(); // "HI, ROB"

	* 
Lower Case


		1. 
var neighborGreeting = "Hi, Rob";
		2. 
neighborGreeting.toLowerCase(); // "hi, rob"







variables

// In the following lab you will see how we can use the Chrome Developer tools to practice our JavaScript

var transportation = 'car';

// invalid variable names
var 1stPet = 'Bear'; // starts with number
var var = 'variables'; // keyword/reserved word
var first name = 'John'; // space between words

// valid variable names
var fruit = 'apple'; // stars with upper/lower case letter
var $money = 5; // starts with $
var _weather = 'hot'; // begins with underscore

// camelCase examples
var lunchCostPerStudent;
var homeRuns;
var userExperience;

// human readability - less code doesn't always mean better code - which is more human readable?
var x = 25;
var applesFromTree = 25;

// until a variable is assigned a value it is uninitialized and its value is undefined
var transporation; // undefined
var transporation = 'car'; // 'car'

// dynamic typing
var transporation = 'car';
var passLieDetector = false;
var groceryBill = 74;
typeof transportation; // "string"
typeof passLieDetector; // "boolean"
typeof groceryBill; // "number"

variables

// review
// variables are containers that store data
// must begin with upper/lower case a - z, $, _
// camelCase best practice

// practice
var example = 'first example';

// challenge - rewrite invalid or bad practice variable names
var 1stPet = 'Bear';
var BaseballTeam = 'Dodgers';
var favoritedayoftheweek = 'Friday';
var favorite color = 'green';
var var = 'car';

// possible solutions
var pet1 = 'Bear'; // numbers are ok if not the first character
var baseballTeam = 'Dodgers';
var favoriteDayOfTheWeek = 'Friday';
var favorite_color = 'green';
var favoriteColor = 'green';
var travel = 'car';




Strings

// string - strings are a data type used to represent text and are wrapped in either a single or double quote

// same value
var name = 'Joe';
var name = "Joe";

// error - mixing single and double quote
var name = 'Joe";

// wrapping any primitive in quotes will turn it into a string
typeof 24; // "number"
typeof '24'; // "string"
typeof true; // "boolean"
typeof 'true'; // "string"
typeof undefined; // "undefined"
typeof "undefined"; // "string"

// quotes within string
// errors
var greeting = 'It's great to see you!'; // error, matching inner and outer single quotes
var response = "Billy said, "I am sick""; // error, matching inner and outer double quotes
// possible solution
var greeting "It's great to see you!";
var response = 'Billy said, "I am sick"';
// possible solution - escape character - turns special characters into string characters
var greetings 'It\'s great to see you!';
var response "Billy said, \"I am sick\"";

// length property - returns the lengh of a string
var greeting = "It's good to meet you!";
greeting.length; // 22

// toUpperCase()
var greeting = 'Good to see you!';
var shoutGreeting = greeting.toUpperCase();
shoutGreeting; // 'GOOD TO SEE YOU!'


// review
// strings used to represent text
// turn any primitive data type into a string by adding single or double quotes
// escape backslash to handle special characters
// length property and toUpperCase() method

// challenge
// change the following code to make valid strings
var animal = 'horse"; // error
var answer = false; // "boolean"
// possible solution
var animal = 'horse';
var answer = 'false';

// challenge - fix errors
var greeting1 = "Sam says, "hi."";
var greeting2 = 'It's great to see you!';
// possible solution without escape character
greeting1 = 'Sam says, "hi."';
greeting2 = "It's great to see you!";

// challenge
// make a valid string with escape character
// use \n two times to start a new line
var greeting3 = 'Don't forget to grab the newspaper on your way out. You are going to be on the bus for a long time because of traffic.';
// possible solution
greeting3 = 'Don\'t forget to grab the newspaper\n on your way out. You are going to be\n on the bus for a long time because of traffic.';

// challenge
// find length of greeting3;
// use toUpperCase() method to turn greeting3 into an uppercase string
greeting3.length;
greeting3.toUpperCase();


Operators

// operators
// operators assign and compare values, performing arithmetic operations and more, allowing programmers to create a single value from one or more values.

// binary operators -> an operand before and after operator
2 + 3;
x * z;

// unary operators -> a single operand before or after the operator
y++
++y

// arithmetic operators -> * / % + -
// addition and subtractions operator
var count = 10 + 5 -4; // 11

// division and multiplication operator
var mult == 3 * 5; // 15
var div = 12 / 4; // 3

// modulos operator -> remainder of two values
var remainder = 21 % 4; // 1

// assignment operators -> assigns value to its left operand based on the value of the right operand
x = 14;
var count = 5;
count = count + 4; // 9
count += 4; // 13
count = count - 5; // 8
count -= 5; // 3

// comparison operators -> compare both sides of the equation and return a logical value based on whether the comparison is true
// == checks for if value is equal
// === checks if value and type are equal
var x = 8;
var y = '8';
x == y; // true - the number type value of 8 is equal to the string type value of '8'
x === y; // false - the type of x is not the same as the type of y

// string operator -> when used on strings this is called the concatenation operator
// addition operator used for string concatenaton
var firstName = 'Rob';
var middleName = 'Grant';
var lastname = 'Merrill';
var fullName = firstName + ' ' + middleName + ' ' + lastName;
fullName; // 'Rob Grant Merrill'

Definition:
“Operators are used to assign values, compare values, perform arithmetic operations and more. Operators allow programmers to create a single value from one or more values.”Binary Operators:
	* 
Definition: Requires two operands, one before the operator and one after the operator.
	* 
Syntax: operand1 operator operand2
	* 
Example: 2 + 3; or x * z;

Unary Operators:
	* 
Definition: Requires a single operand, either before or after the operator.
	* 
Syntax: operator operand OR operand operator
	* 
Example: y++ OR ++y

Arithmetic Operators: Multiplication, Division, Modulus, Addition and Subtraction
	* 
Definition: Takes numerical values (either literals or variables) as their operands and returns a single numerical value.
	* 
Example: var count = 10 + 5 - 4; // 11
	* 
Example: var mult = 3 * 5; // 15

Modulus Operators
	* 
Definition: This will give us the remainder of two values.
	* 
Example: 21 % 4; // 1

Assignment Operators:
	* 
Definition: Assigns a value to its left operand based on the value of its right operand.
	* 
Example: var count = 5;

Comparison Operators:
	* 
Definition: Compare both sides of equation and returns a logical value based on whether the comparison is true. The operands can be numerical, string, logical, or object values.
	* 
Equality operator (==): Checks for equality in value. Coersion may take place finding equal values between a string and number.
	* 
Strict equality operator (===): Checks for equality in value and type. Does not leave room for coersion.
	* 
example: 5 == '5'; // true
	* 
example: 5 === '5' // false

String Operator:
	* 
Definition: When the ‘+’ is used on strings the ‘+’ operator is called the concatenation operator.
	* 
example: 'Hello' + ' ' + 'world'; // 'Hello world' 



obejcts

dot notation


object literal notation


bracket notation


Definition:
"An object is a value type consisting of key/value pairs inside curly braces. The keys are also known as properties. Everything in JavaScript that isn’t a primitive is an object."
"A set of key-value pairs. Each key is a string that can be paired with any JavaScript value. You can then use the key to retrieve whatever value it's within in the object."
"Objects in JavaScript are very similar to arrays, but objects use strings instead of numbers to access the different elements. The strings are called keys or properties, and the elements they point to are called values. Together these pieces of information are called key-value pairs."Vocabulary Change:
	* 
Variables become known as properties in objects.
	* 
Functions become known as methods in objects.

Object Literal Notation:
	* 
Syntax: var object = {};
	* 
Key/Properties: Single or double quotes not needed for valid variable names. Invalid variable names will require single or double quotes.

		* 
age = 24;
		* 
"user age" = 24;

How to Access Properties on an Object: 
	* 
The two primary ways of accessing properties of an object are with dot notation and bracket notation.
	* 
Bracket Notation:

		* 
Syntax: object[‘property’] = value;
		* 
Example:



             var book = { title: ‘Huck Fin’, pages: 260 };
             book[‘title’]; // ‘Huck Fin’
             book[’pages’]; // 260
	* 
Dot Notation:


		* 
   Syntax: object.property = value;
		* 
   Example:



               var name = { firtName: ‘John’, lastName: ‘Doe’ };
               name.firstName; // ‘John’
               name.lastName; // ‘Doe’How to Add Properties and Values on an Object: 
	* 
You can add items to an object by using strings.
	* 
Bracket Notation:

		* 
var person = {};
		* 
person["name"] = "Rob";
	* 
Dot Notation: 

		* 
var person = {};
		* 
person.name = "Rob";




