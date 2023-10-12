let single = 'Single Quote';
let double = "Double Quote";
let backtick = `backtick`;
console.log('single ',single);
console.log('double ',double);
console.log(`backtick `, backtick);

let name = 'Tony';
let greeting = 'Hello ${name}';
console.log(greeting); // Hello, Tony

// let one = 'Hello';
// let two = 'There';
// let join = ${one}${two};
// console.log(join)

// Include Expressions in Strings
let song = 'ILoveYou';
let score = 9;
let highScore = 10;
let output = 'I give this song ${song} a score of ${(score / highScore) * 100}%';
console.log(output);

// CONVERTER 
let myString = "123";
let number = Number(myString);
console.log(typeof number);
let otherString = String(number);

// Functions

let text= `Me is string`;
let newText = text.replace('string', 'sausage');
console.log(newText);

// Array
let myArray = ["I", "love", "you", "iubito", "!"];
let newArray = myArray.join(" ");
console.log(newArray);

// Generate a random number;
const randomNumber = (Math.random() * 9);
console.log("Random number: ", randomNumber);