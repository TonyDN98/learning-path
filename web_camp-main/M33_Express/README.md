<h1>Module 33. Express</h1>
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


<h2 id="u1">1. Intro </h2>
<p>|____________________________|</p>

```javascript
/*
* Express Intro
* Startup server to listen for requests;
* Parse Income request;
* Craft https response;
* 
* */
```

<h2 id="u1">2. NPM Express </h2>
<p>|____________________________|</p>

```javascript
// npm i express;

// Initial package.JSON;
// npm init; 


// require express;
const express = require('express');

const app = express();


// Everytime our server will get a request this () will be executed;
app.use(()=>{
    console.log("We got a request again;")
})


// Express port server;
app.listen(3000, ()=>{
    console.log("Listen on port 3000;")
})
```
