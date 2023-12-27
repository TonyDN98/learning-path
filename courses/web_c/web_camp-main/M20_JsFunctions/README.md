<h1>Module 20. JavaScript Functions;</h1>
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
    <li><a href="#u1">1. 1. Functions Syntax;</a></li>
    <li><a href="#u2">2. 2. Arguments;</a></li>
</ul>


<h2 id="u1">1. Functions Syntax;</h2>

<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* 2 steps process: Define --> RUN
* +-------------------------------------------------------------------------+|
* Syntax :
* function funcName(param) {
*   // do something
* }
* +-------------------------------------------------------------------------+|

*/

// first Function
function singSong(){
    console.log("Do");
    console.log("Re");
    console.log("Mi");
}

singSong(); // DO RE MI

```


<h2 id="u2">2. Arguments;</h2>
<p>|____________________________|</p>

```javascript
// Greet function with parameters;

function greetPerson(person){
    console.log(`Hi ${person}`);
}

function rant(message){
    console.log(`${message}`.toUpperCase());
    console.log(`${message}`.toUpperCase());
    console.log(`${message}`.toUpperCase());
}


// Multiple Arguments;

function repeat(str, numTimes){
    let result = '';
    for (var i = 0; i < numTimes; i++) {
        result+= str;
    }
    console.log(result)
}

repeat("LOL", 3);

function isSnakeEyes(dice1, dice2){
    if (dice1 === dice2){
        console.log('Snake Eyes!');
    }else {
        console.log('Not Snake Eyes!')
    }
}
```