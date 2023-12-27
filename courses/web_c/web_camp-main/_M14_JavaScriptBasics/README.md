
<h1>Module 14. JavaScript Basics</h1>
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
    <li><a href="#u1">1. Primitive Types;</a></li>
    <li><a href="#u2">2. Variables;</a></li>
    <li><a href="#u3">3. Updating Variables; </a></li>
    <li><a href="#u4">4. Const & Var</a></li>
    <li><a href="#u5">5. Boolean</a></li>
    <li><a href="#u6">6. Changing the variable Type;</a></li>
    <li><a href="#u7">7. Variable Naming and Conventions;</a></li>
</ul>


<h2 id="u1">1. Primitive Types</h2>
<p>|____________________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* Primitive Types;
+-------------------------------------------------------------------------+|
* Number
* String
* Boolean
* Null
* Undefined
+-------------------------------------------------------------------------+|
* */
```

<h3>Number DataType;</h3>
<p>|_____________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* Number DataType;
+-------------------------------------------------------------------------+|
* Js has only one number;
* Positive/ Negative / Integers / Decimal numbers; 
+-------------------------------------------------------------------------+|
* */
```

<h3>Math Operators;</h3>
<p>|____________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* Math Operators;
+-------------------------------------------------------------------------+|
* PEMDAS (Order of operatos)
* Paranthesis / Exponent / Multiplication / Division / Addition / Substraction / 
+-------------------------------------------------------------------------+|
* Addition 50 + 5;
+-------------------------------------------------------------------------+|
* Substratction 90 - 1;
+-------------------------------------------------------------------------+|
* Multiplication 1111 * 7;
+-------------------------------------------------------------------------+|
* Division 400/25;
+-------------------------------------------------------------------------+|
* Modulo 25 % 20;
+-------------------------------------------------------------------------+|
* Exponent 2 ** 3;
+-------------------------------------------------------------------------+|
* */
```

![Math Operators;](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssMathOperatorsJs.png?raw=true)

<h3>NaN(NOT a NUMBER);</h3>
<p>|____________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* NaN(NOT a NUMBER) but it's still a part of NUMBER family;
+-------------------------------------------------------------------------+|
* */

0/0 //NaN

1 + NaN //NaN

typeof NaN // Number
```
![NaN Number;](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssNaNJs.png?raw=true)

<h2 id="u1">2. Variables;</h2>
<p>|____________________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* Variables;
+-------------------------------------------------------------------------+|
* we can store a value and give it a name so that we can:
*   Refer back later;
*   Use that value to do stuff;
*   Or change it later;
+-------------------------------------------------------------------------+|
* */

// Basic Syntax;
let name = value;

let year = 1998;

// RecallValues;

let number1 = 25;
let number2 = 50;

number1 + number2; // 75;

let numberTotal = number1 + number2;
numberTotal; // 75;


/*
+-------------------------------------------------------------------------+|
* Variable Exercise;
+-------------------------------------------------------------------------+|
* Define a varialbe called myLuckyNumber and set it to 37;
* Define a varialbe called octopusLimbs and set it to 8;
+-------------------------------------------------------------------------+|
* */

let myLuckyNumber = 37;
let octopusLimbs = 8;

```

![Variables;](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssVariablesJs.png?raw=true)

<h2 id="u3">3. Updating Variables;</h2>
<p>|___________________________________|</p>

```javascript
/*
+-------------------------------------------------------------------------+|
* Updating Variables;
+-------------------------------------------------------------------------+|
* Increment Operator(+1)(Pre fixed / Post Fixed)
* ++number / number++; (before execute / after execute)
* 
* Decrement Operator(-1)(Pre fixed / Post Fixed)
* --number / number--; (before execute / after execute)
*
* number += 5;
* number = number + 5;
*
* number -= 5;
* number = number - 5;
*
* number *= 5;
* number = number * 5;
*
* number /= 5;
* number = number / 5;
* */
```

<h4> Incremenet / Decermenet by 1;</h4>

![Increment/Decrement](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssIncrementDecrementJs.png?raw=true)


<hr>

<h4>Updating Variables;</h4>
![Updating Varialbes Operators](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssUpdatingVariablesJs.png?raw=true)


<h2 id="u4">4. Const & Var</h2>
<p>|______________________________|</p>

```javascript
/*
* CONST (Stand for CONSTANT and you can't change the value anymore once it's created;)
* const number = 4;
* number = 25; // error
* 
* const pokemonPower = 2000;
* pokemonPower += 250; // error
* */

const number = 4;
number = 25; // error

const pokemonPower = 2000;
pokemonPower += 250; // error

/*
* Var KEYWORD
* It's the old version of creating variables, replaced by let;
* Works in the exact same way;
* */

var power = 150; //150
power += 50; //200

/*
* Const Exercise;
* Define a const called boilingPointC set it to 100;
* Define a const called boilingPointF set it to 212;
* */

const boilingPointC = 100;
const boilingPointF = 212;
```

![Const & Var](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssConst&VarJs.png?raw=true)

<h2 id="u5">5. Boolean</h2>
<p>|__________________________|</p>

```javascript
/*
* Boolean (true or false , this keywords are case sensitive;)
* Can store only 2 values : true or false;
* */

let isBattleTowerOver = false;
let isLoggedIn = true;
```

![Boolean](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssBooleanJs.png?raw=true)

<h2 id="u6">6. Changing the variable Type;</h2>
<p>|________________________________________________|</p>

```javascript
/*
* Changing variable type;
* One variable already declared dosen't have a fixed data type;
* That type can be changed anytime we want durring the process;
* */

let isThatPikaPika = true; // boolean
isThatPikaPika = 2100; // number
isThatPikaPika = "It's PIKA!"; // text
```

![Changing Var Type](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssChangingVarTypeJs.png?raw=true)

<h2 id="u7">7. Variable Naming and Conventions;</h2>
<p>|__________________________________________________________|</p>

```javascript
/*
* Naming Conventions;
* let varName = value;
* varName is called an "identifier";
* Rules;
*   An identifier can't start with a digit ex: 1name, 23Identifier;
*   Can start with ($) or (_) ex : $nameVar, $balance, _currentDirectory;(DON'T USE IT)
*   USE camelCase RULE; ex: camelCase, nameVar, currentBalance, currentDirectory, isLoggedIn;
*   Use meaningful names for your vars;
*   When boolean give it a meaningfull prefix isGameOver, isAlive, isBattleOver;
* */
```

![naming Convention](https://github.com/TonyDN98/web_camp/blob/main/M14_JavaScriptBasics/ss/ssNamingConventionJs.png?raw=true)

