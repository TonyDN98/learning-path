<h1>Module 32. NPM</h1>
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
    <li><a href="#u1">1. </a></li>
    <li><a href="#u2">2. </a></li>
</ul>


<h2 id="u1">1. Require a File and a Directory </h2>
<p>|____________________________|</p>

```javascript
/*
* // from js file.
* module.exports = something
* Exports an object;
* */

const add = (x,y) => x + y;

const PI = 3.14527;


// dosent matter whats executed;
module.exports.add = add;
module.exports.PI = PI;



// in the other js file module;
const math = require('./math');


// we can access now;
math.add();
math.PI;


/*
* Requiring an entire Directory; 
* Combining js files into a single one module;
* Its a must to have an index.js
* 
* */
```

<h2 id="u1">2. package.JSON Dependencies;</h2>
<p>|____________________________|</p>

```javascript
/*
* Nav to the mai root dir of the package.json
* Use command npm isntall; to install all the required dependencies;
* Never share node_modules with anyone can take a lot of space;
* 
* */
```
