# Js Fundamentals

## [String Fundamentals](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Strings)

### Declare Strings

```js
let name = 'Something here';
```

### Single quotes, double quotes, and backticks

```js
let single = 'Single Quote';
let double = "Double Quote";
let backtick = `backtick`;
console.log('single ',single);
console.log('double ',double);
console.log(`backtick `, backtick);
```

### Embedding Js

*Inside a template literal, you can wrap JavaScript variables or expressions inside ${ }, and the result will be included in the string*

```js
let name = 'Tony';
let greeting = 'Hello ${name}';
console.log(greeting); // Hello, Tony

let one = 'Hello';
let two = 'There';
let join = ${one}${two};
console.log(join)
```
### Include Expressions in Strings

```js
let song = 'ILoveYou';
let score = 9;
let highScore = 10;
let output = 'I give this song ${song} a score of ${(score / highScore) * 100}%';
console.log(output);
```

### Convert to STRING

```js
let myString = "123";
let number = Number(myString);
console.log(typeof number);
let otherString = String(number);
```

## [Conditions Fundamentals](https://javascript.info/comparison)

### Comparators

`Greater/les`s than: `a > b`, `a < b`.  
`Greater/less than or equals`: `a >= b`, `a <= b`.  
`Equals`: `a == b`, please note the double equality sign `==` means the equality   test, while a single one a = b means an assignment.  
`Not equal`s: In maths the notation is` ≠`, but in JavaScript it’s written as a `!= `b.

### [if-else-else if](https://www.w3schools.com/js/js_if_else.asp)

```js
// IF
if (condition) {
  //  block of code to be executed if the condition is true
}

if (hour < 18) {
  greeting = "Good day";
}
```
   

```js
//IF ELSE
if (condition) {
  //  block of code to be executed if the condition is true
} else {
  //  block of code to be executed if the condition is false
}


if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}

```

  

```js
  // ELSE IF
  if (condition1) {
  //  block of code to be executed if condition1 is true
} else if (condition2) {
  //  block of code to be executed if the condition1 is false and condition2 is true
} else {
  //  block of code to be executed if the condition1 is false and condition2 is false
}

if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

## [logic Operators](https://javascript.info/logical-operators)

### OR ||

```js
alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false
```

### OR "||" finds the first truthy value

```js
// if one value its true then expression is true;
result = value1 || value2 || value3;
```

```js
alert( 1 || 0 ); // 1 (1 is truthy)

alert( null || 1 ); // 1 (1 is the first truthy value)
alert( null || 0 || 1 ); // 1 (the first truthy value)

alert( undefined || null || 0 ); // 0 (all falsy, returns the last value)
```

### && (AND)

```js
result = a && b;

alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false

// example with IF

let hour = 12;
let minute = 30;

if (hour == 12 && minute == 30) {
  alert( 'The time is 12:30' );
}


```

### AND “&&” finds the first falsy value

```js
result = value1 && value2 && value3;

// if the first operand is truthy,
// AND returns the second operand:
alert( 1 && 0 ); // 0
alert( 1 && 5 ); // 5

// if the first operand is falsy,
// AND returns it. The second operand is ignored
alert( null && 5 ); // null
alert( 0 && "no matter what" ); // 0
```

> The precedence of AND && operator is higher than OR ||.

### ! (NOT)  
The boolean NOT operator is represented with an exclamation sign `!`.

```js
result = !value;

alert( !true ); // false
alert( !0 ); // true
```

```js
// The answer is 2, that’s the first truthy value.

alert( null || 2 || undefined );
```


## [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)

### Built-in browser functions

#### Manipulate text
```js
const myText = "I am a string";
const newString = myText.replace("string", "sausage");
console.log(newString);
// the replace() string function takes a source string,
// and a target string and replaces the source string,
// with the target string, and returns the newly formed string
```

#### manipulate Array

```js
const myArray = ["I", "love", "chocolate", "frogs"];
const madeAString = myArray.join(" ");
console.log(madeAString);
// the join() function takes an array, joins
// all the array items together into a single
// string, and returns this new string
```

#### generate a random number

```js
const myNumber = Math.random();
// the random() function generates a random number between
// 0 and up to but not including 1, and returns that number
```

## Functions Vs Methods

```js
function draw() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
  for (let i = 0; i < 100; i++) {
    ctx.beginPath();
    ctx.fillStyle = "rgba(255,0,0,0.5)";
    ctx.arc(random(WIDTH), random(HEIGHT), random(50), 0, 2 * Math.PI);
    ctx.fill();
  }
}

// Invoke it

draw();
```

### Default parameters

```js
function hello(name = "Chris") {
  console.log(`Hello ${name}!`);
}

hello("Ari"); // Hello Ari!
hello(); // Hello Chris!
```

### Anonymous functions and arrow functions

```html
<input id="textBox" type="text" />
<div id="output"></div>
```

```js
const textBox = document.querySelector("#textBox");
const output = document.querySelector("#output");

textBox.addEventListener("keydown", (event) => {
  output.textContent = `You pressed "${event.key}".`;
});
```