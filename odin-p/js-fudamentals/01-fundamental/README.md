# Js Fundamentals 1

## How to run Js code

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>
<body>
  <script>
    // Your JavaScript goes here!
    console.log("Hello, World!")
  </script>
</body>
</html>
```

**`console.log()` is the command to print something to the developer console in your browser.**

 *Another way to include JavaScript in a webpage is through an external script. This is very similar to linking external CSS docs to your website.*

 ```html
 <script src="javascript.js"></script>
 ```

 ## [Variables](https://javascript.info/variables)

 You can think of variables as simply “`storage containers`” for data in your code.  

![vars](https://cdn.statically.io/gh/TheOdinProject/curriculum/d39eaf2ca95e80705f703bb218216c10508f5047/foundations/javascript_basics/fundamentals-1/imgs/00.png)

*In the newest JavaScript versions we have two more ways — `let` and `const`.*

The above tutorial mentioned this, but it’s important enough to note again: let and const are both relatively new ways to declare variables in JavaScript. In many tutorials (and code) across the internet you’re likely to encounter `var` statements. Don’t let it bother you! There’s nothing inherently wrong with `var`, and in most cases `var` and let behave the same way. But sometimes the behavior of `var` is not what you would expect. Just stick to `let` (and `const`) for now.

!`NOTE`: `var` can lead to wrong types and it's not what we expect.

```js
let message;
message = 'Hello!';

alert(message); // shows the variable content
```

#### Multiple declarations

```js
let user = 'John', age = 25, message = 'Hello';
```

#### Copy from one to another

```js
let hello = 'Hello world!';

let message;

// copy 'Hello world' from hello into message
message = hello;

// now two variables hold the same data
alert(hello); // Hello world!
alert(message); // Hello world!
```

#### Declaring twice triggers an error

```js
let message = "This";

// repeated 'let' leads to an error
let message = "That"; // SyntaxError: 'message' has already been declared
```

## Variable naming

There are two limitations on variable names in JavaScript:  

The name must contain only letters, digits, or the symbols $ and _.  
The first character must not be a digit.  
When the name contains multiple words, camelCase is commonly used. That is: words go one after another, each word except first starting with a capital letter: myVeryLongName

```js
let userName;
let test123;
```

## Constants

To declare a `constant` (unchanging) variable, use const instead of `let`:

```js
const myBirthday = '18.04.1982';

// can't reassign
const myBirthday = '18.04.1982';

myBirthday = '01.01.2001'; // error, can't reassign the constant!

```

### Uppercase constants

There is a widespread practice to use constants as aliases for difficult-to-remember values that are known prior to execution  

Such constants are named using capital letters and underscores.
  
For instance, let’s make constants for colors in so-called “web” (hexadecimal) format:  

```js
const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// ...when we need to pick a color
let color = COLOR_ORANGE;
alert(color); // #FF7F00
```

