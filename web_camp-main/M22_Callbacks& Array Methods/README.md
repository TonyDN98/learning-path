<h1>Module 22. Callback & Arrays Methods;</h1>
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
    <li><a href="#u1">1. ForEach</a></li>
    <li><a href="#u2">2. Map</a></li>
    <li><a href="#u3">3. Arrow Super Useful </a></li>
    <li><a href="#u4">4. Arrow Implicit Return </a></li>
    <li><a href="#u5">5. SetInterval / SetInterval </a></li>
    <li><a href="#u6">6.  Some & Every</a></li>
</ul>


<h2 id="u1">1. forEach not that common anymore</h2>

<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* 
* +-------------------------------------------------------------------------+|
*/

const numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];

function print(elemenet){
    console.log(elemenet);
}

numbers.forEach(print) // 1..10

// Common syntax; Rly Common;
numbers.forEach(function (el) {
    if (el % 2 == 0) {
        console.log(el);
    }
})

```


<h2 id="u2">2. Map</h2>
<p>|____________________________|</p>

```javascript
// MAP
// const something = array.map(function(param))
const numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];

 const doubles = numbers.map(function (num){
    return num * 2;
})

// DO NOT ALTER THE FOLLOWING CODE:
const fullNames = [{first: 'Albus', last: 'Dumbledore'}, {first: 'Harry', last: 'Potter'}, {first: 'Hermione', last: 'Granger'}, {first: 'Ron', last: 'Weasley'}, {first: 'Rubeus', last: 'Hagrid'}, {first: 'Minerva', last: 'McGonagall'}, {first: 'Severus', last: 'Snape'}];

const firstNames = fullNames.map(function (fname) {
    return fname.first;
    
})


// Coming back from arrow;

const newMovies = movies.map(function (movie) {
    return `${movie.title} - ${movie.score / 10}`
})

// or arrow

const newMovies = movies.map(movies =>(
    `${movie.title} - ${movie.score / 10}`
))
```

<h2 id="u3">3. Arrow Super Useful</h2>
<p>|____________________________|</p>

```javascript
/*
* Shorter version on single use parameter function;
* Create function expressions;
* Only works if there is only and only one expression or statement;
* */

const add = (x,y) => {
    return x * y;
}

// it's the same as 

const add = function (x,y){
    return x * y;
}

add(22,55);

// * +-------------------------------------------------------------------------+|


const square = function (x){
    return x * x;
}

const square = (x) =>{
    return x * x;
}

square(5);

// * +-------------------------------------------------------------------------+|

let rolldie = function (){
    return Math.floor((Math.random() * 10) + 1 );

}

let rollDie = () =>{
    return Math.floor((Math.random() * 10) + 1 );
}

rollDie();


// exercise

let greet = (name)=>{
    return `Hey ${name}!`
}
```


<h2 id="u4">4. Arrow Implicit Return</h2>
<p>|____________________________|</p>

```javascript
// old syntax with return 

let rollDie = () =>{
    return Math.floor((Math.random() * 10) + 1 );
}


// new syntax with implicit returning;
let rollDie = () =>(
    Math.floor((Math.random() * 10) + 1 )
)
rollDie();


const isEven = (nr) =>(
    nr % 2 == 0
)
```


<h2 id="u5">5. SetInterval / SetInterval</h2>
<p>|____________________________|</p>

```javascript
// setTimeout
// Hello/ Goodby3 // after 3 sec are u still there ? 
console.log("Hello!");
setTimeout(()=>{
    console.log('Are you still there? ')
}, 3000)
console.log('Goodby3');


// setInteval
// Continue execute this function every 3 sec

const id = setInterval(()=>{
    console.log(Math.random() * 10)
},3000)
 
//Stops with ClearInterval(id);

```

<h2 id="u6">6. Some & Every</h2>
<p>|____________________________|</p>

```javascript
// Both return boolean values true or false;
// Every(element)
const mathExams = [76,88,99,87,97,95,79];

mathExams.every(score => score >= 75 ); // true

// of only a single one is < 75 will return false 

const mathExams = [76,88,72,87,97,95,79];
mathExams.every(score => score >= 75 ); //false


// Some(elements);
const mathExams = [76,88,99,87,97,95,79];

mathExams.some(score => (score >= 50) && (score <= 73) ); //true


allEvens.every(even => even % 2 == 0)
```

