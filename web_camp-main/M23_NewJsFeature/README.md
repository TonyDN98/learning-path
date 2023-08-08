<h1>Module 23. New Js Features;</h1>
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
    <li><a href="#u1">1. Default Parameters;</a></li>
    <li><a href="#u2">2. Spread syntax; </a></li>
    <li><a href="#u3">3. Spread Array;</a></li>
    <li><a href="#u4">4. Spread Objects;</a></li>
    <li><a href="#u5">5. Rest Parameter;</a></li>
    <li><a href="#u6">6. Destructuring Arrays;</a></li>
    <li><a href="#u7">7. Destructuring Objects;</a></li>
</ul>


<h2 id="u1">1. Default Parameters;</h2>

<p>|____________________________|</p>

```javascript
/*
* Default Parameters;
* */

              // b = 5 default parameter values;
 function add(a,b=5){
 return a + b}

 add(5) // 10;

function rolDie(numSides =6){
     return Math.floor(math.random() * numSides + 1);
}

function greet(person,msg="Hey There") {
    console.log(`${msg} ${person}`);
}

```

<h2 id="u2">2. Spread syntax;</h2>
<p>|____________________________|</p>

```javascript
/*
* Spread syntax;
* ...array
* 
* */

const nums = [11,14,18,19,22,59];

Math.max(...nums);
Math.min(...nums);

console.log(nums); // 11,14,18,19,22,59;
console.log(...nums); // 11 14 18 19 22 59;
```

<h2 id="u3">3. Spread Array;</h2>
<p>|____________________________|</p>

```javascript
const dogs =['Mity', 'Bity', 'Turbatul'];
const cats =['Dl.labute pufoase', 'Bity albiciosul', 'Mishu'];

const allPets = [...dogs, ...cats];

console.log(allPets); //dogs , cats
```

<h2 id="u4">4. Spread Objects;</h2>
<p>|____________________________|</p>

```javascript

const formData = {
    email: "bluemarin@gmail.com",
    password : 'tobito123',
    userName : 'Pantalonasi'
};

// copy the object data intro a new object and add custom keys;
let newUser = {...formData, id: 2345, isAdmin:false};

console.log(newUser);

```

<h2 id="u5">5. Rest Parameter;</h2>
<p>|____________________________|</p>

```javascript
// Rest of the parameters
// Looking at min or max functions that can take a lot of argumnets;
Math.max(1,3,5,6,7,8,9);

function sum(...numbers){
    // now we have acces to array methods;
     return numbers.reduce((total,el) => total + el)
}
```

<h2 id="u6">6. Destructuring Arrays;</h2>
<p>|____________________________|</p>

```javascript
// Is based on the order of the array;
// const[var,var,var] = array;

const scores = [9955,6633,  5566,  5111,4987,4532,4111];
// const       [gold,silver,bronze,...everyOneElse]
const[gold,silver,bronze,...everyOneElse] = scores;



````


<h2 id="u7">7. Destructuring Objects; more PRACTICAL</h2>
<p>|____________________________|</p>

```javascript
// More Practical then Destructuring Arrays;
// const{var,var,var} = user;
// We single them out into their own variables;
const user = {
    email: "harvbey@nothing.ro",
    password : "something123",
    firstName : "Trevor",
    lastname : 'T',
    born : 1938,
    bio : "American Presedent ",
    city : 'Sun Francisco',
    state : "California"
};

const firstName = user.firstName;
const lastName = user.lastname;
//.. and so on util state we dont want that;

const {email , firstName,city,bio, state} = user;
//Renaming them after we single them out;

const {email: userEmail , firstName:First ,city : userCity ,bio : userBio, state} = user;
```




