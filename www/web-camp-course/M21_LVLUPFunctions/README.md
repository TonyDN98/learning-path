<h1>Module 21. JavaScript LvLUpFunctions</h1>
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
    <li><a href="#u1">1. Scope </a></li>
    <li><a href="#u2">2. Function Expression </a></li>
    <li><a href="#u3">3. High Order Functions </a></li>
    <li><a href="#u4">4. Returning Functions</a></li>
    <li><a href="#u5">5.  Defining Methods </a></li>
    <li><a href="#u6">6.  Keyword this </a></li>
</ul>


<h2 id="u1">1. Scope</h2>

<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* Scope - Var Visibility
* let name - block scoped;
* var name - visibile outside after a loop ends his execution;
* +-------------------------------------------------------------------------+|
*/

function collectEggs(){
    let totalEgg = 6; // visible only here
    console.log(totalEgg);
}


let bird = 'Scarlet Bird';
function birdWatch(){
    bird = ''
}



// Lexical Scope; Nested visibilty of functions inside another function;

function bankRob(){
    const heros = ['batman', 'superman', 'batmobvile'];
    function cryForHelp(){
        for (hero of heroes){ // heros are accesbile from parent element;
            console.log(`HELP ${hero.toUpperCase()}`);
        }
    }
    cryForHelp();
}

bankRob();
```


<h2 id="u2">2. Function Expression</h2>
<p>|____________________________|</p>

```javascript

// storing a function inside a variable;

const add = function (x,y) {
    return x+y;
};

add(3,4);

<h2 id="u3">3. High Order Functions</h2>
<p>|____________________________|</p>
```

```javascript
// Accepts other functions as arguments;
// Return a function;

function callbackTwice(func){
    func();
    func();
}

function rolldie(){
    const roll = Math.floor((Math.random()* 10) + 1);
    console.log(roll)
}

callbackTwice(rolldie)

```


<h2 id="u4">4. Returning Functions</h2>
<p>|____________________________|</p>

```javascript

function  makeBetweenFunc(min,max){
    return function (num){
        return nun >= min && num <= max;
    }
}

makeBetweenFunc(100,200);

function isBetween(n){
    return n >= 50 && m <= 100;
}

function isBetween(n){
    return n >= 50 && m <= 100;
}
```

<h2 id="u5">5. Defining Methods</h2>
<p>|____________________________|</p>

```javascript
const myMath = {
    blah : 'Hi',
    add(x,y){
        return x + y;
    },
    multiply(x,y){
        return x * y;
    },
    cube(x){
        return x**3;
    }
};

myMath.add(1,2);
myMath.multiply(1,2);
myMath.cube(5);

const square = {
    area(x){
        return x * x;
    },
    parimeter(x){
        return x * 4;
    }
};
```
<h2 id="u6">6. Keyword this</h2>
<p>|____________________________|</p>

```javascript
/*
* Refers to the current object;
* */

const hen ={
    name : 'Helen',
    eggCount : 0,
    layAnEgg(){
        this.eggCount=this.eggCount++;
        return `EGG`;
    }
};
```
