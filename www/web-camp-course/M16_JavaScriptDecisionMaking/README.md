<h1>Module 16. JavaScript Decision Making</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[]()
<>
[]()
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>
    <li><a href="#u1">1. Comparisons</a></li>
    <li><a href="#u2">2. Console.*()</a></li>
    <li><a href="#u3">3. parseInt() / prompt()</a></li>
    <li><a href="#u4">4. Running Js from a Script;</a></li>
    <li><a href="#u5">5. If Condition;</a></li>
    <li><a href="#u6">6. Logical Operators;</a></li>
></ul>


<h2 id="u1">1. Comparisons</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* Comparation Operators(Return boolean values;);
* +-------------------------------------------------------------------------+|
* > greater then
* < less then
* >= great then or equal
* <= less then or equal
* == equality
* != not equality
* === strict equality
* !== strict non-equliaty
* +-------------------------------------------------------------------------+|
*  Every character has a unicode value
*   'a' -> 61
*   'b' -> 62
*   so on...
*   'a' < 'b' // true;
* +-------------------------------------------------------------------------+|
* 
* EQUALITY(== , ===)
*   == check for equality of two values;
*   1 == 1 true;
*   1 == 2 false;
*   'a' == 'b' // true
*   0 == false ; //true
* +-------------------------------------------------------------------------+|
*   ===(strict equality)
*   Check for equalityof value and type;
*   5 === 5 // true;
*   1 === 2 // //false
*   2 === '2' // false
*   false === 0 //false
* * +-------------------------------------------------------------------------+|
*   //NON EQUAL
*   10 != '10' //false;
*   10 !== '10' // true;
* * +-------------------------------------------------------------------------+|
* */
```

<h2 id="u2">2. Console.*()</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* Console
* * +-------------------------------------------------------------------------+|
* Console.log(argument);
* console.log("Hello");
* +-------------------------------------------------------------------------+|
* console.warn("Warning message");
* +-------------------------------------------------------------------------+|
* console.error(" Error message");
* +-------------------------------------------------------------------------+| 

* */
```


<h2 id="u3">3. parseInt() / prompt()</h2>
<p>|____________________________|</p>

```javascript
/*
* 
* prompt("Please Enter a Number:");
* 
* let userName =  prompt("Please Enter your UserName: ");
* 
* Taking a userInputNumber from text type and convert it to a number;
* let input = parseInt()
* */
```

<h2 id="u4">4. Running Js from a Script;</h2>
<p>|____________________________|</p>

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Boiler Plate</title>

    
</head>
<body>


<!--
Include Script File
Include it on the bottom file when we want our html elements to be created
before our js script will interact with it;
-->

<script src="scriptfile.js"></script>
</body>
</html>
```

```javascript
/* scriptfile.js */
console.log("Hello There!;")
console.warn("OH NO!");
```
<h2 id="u5">5. If Condition;</h2>
<p>|____________________________|</p>

```javascript
// if(cond) else if(condition else)

console.log("Before condition");
// Random number between 1-10;
let rand = Math.floor(((Math.random() * 10) + 1));

// if
if(rand < 5){
    console.log(`Your random number ${rand} < 5`);
}else if (rand === 5){ //else if
    console.log(`Your random number ${rand} is 5`);

}else{ //else
    console.log(`Your random number ${rand} > 5`);
}

console.log("After condition");
```

```javascript
let age = parseInt(prompt("Age:"));
let fee = 0;

if(age >= 0 && age <=4){
    console.log(`Child 0 - 4 fee ${fee}`);
}else if (age >= 5 && age <=10){
    fee = 10;
    console.log(`Kid 5 - 10 fee ${fee}$`);
}else if (age >= 11 && age <=18){
    fee = 15;
    console.log(`Teen 11 - 18 fee ${fee}$`);
}else {
    fee = 20;
    console.log(`Senior19 - 65 fee ${fee}$`);
}
```

<h3>Nesting Conditions</h3>
```javascript
// Password at least 6+ chars
// Can't contain space;

let password = prompt("Enter Pass:");

if (password.length >= 6){
    if (password.indexOf(" ") === -1){
        console.log("GJ! No space");
    }else{
        console.log("Can't contain spaces;")
    }
}

```
<h2 id="u6">6. Logical Operators;</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* Logical Operators;
* * +-------------------------------------------------------------------------+|
* 
* * +-------------------------------------------------------------------------+|
* && AND
* * +-------------------------------------------------------------------------+|
* true && true -> true;
* true && false -> false;
* false && true -> false;
* false && false -> false;
* * +-------------------------------------------------------------------------+|
* * * +-------------------------------------------------------------------------+|
* || OR
* * * +-------------------------------------------------------------------------+|
* true || true -> true;
* true || false -> true;
* false || true -> true;
* false || false -> false;
** +-------------------------------------------------------------------------+|
* ! NOT
 +-------------------------------------------------------------------------+|
* !(1 === 1) -> false;
* !true -> false;
* !false -> true
* 
* !null -> true;
* 
* !!!false /true/false/true
* 
* */
```





