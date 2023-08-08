<h1>Module 18. JavaScript Object Literals</h1>
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
    <li><a href="#u1">1. INTRO OBJECTS</a></li>
    <li><a href="#u2">2. Accessing Data </a></li>
    <li><a href="#u3">3. Modify Data</a></li>
    <li><a href="#u4">4. Nesting Arrays & Objects  </a></li>
</ul>


<h2 id="u1">1. INTRO OBJECTS</h2>
<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* INTRO OBJECTS
* +-------------------------------------------------------------------------+|
* Just like arrays, objects will help us store multiple pieces of data together;
* Objects are collections of properties;
* Accesing data using custom keys; Value pair;
* Objects are not ordered;
* !!! PROPERTY = 
*       KEY 
*        +
*       VALUE
* 
* userName: -----> 'crazyCatLady'
* upVotes: ------> 7
* text: ------> 'great post'
* 
 */

//Using an object;

const someObject = {
    totalSteps : 308727,
    totalMiles : 211.7,
    avgCalories : 5755,
    workoutThisWeek: '5 of 7',
    avgGoodSleep : '2:13'
};

/*
* When we create an object, all datatypes are welcome;
* */


const product = {
    name:  "Gummy Bear",
    inStock: true,
    price : 1.99,
    flavors: ["cherry", "grapes", "apples"]
};

```

<h2 id="u2">2. Accessing Data</h2>
<p>|____________________________|</p>

```javascript
/*
* ACCESSING DATA:
*
const someObject = {
    totalSteps : 308727,
    totalMiles : 211.7,
    avgCalories : 5755,
    workoutThisWeek: '5 of 7',
    avgGoodSleep : '2:13'
};
* 
* SYNTAX: 
*  OBJECT.KEY
* someObject.totalSteps;
* someObject.avgGoodSleep;
* someObject.totalMiles;
* 
* Using IT DINAMIC (a var for example);
* object[variable];
* 
* */

//PLEASE DON'T TOUCH THIS LINE!
const restaurant = {
    name: 'Ichiran Ramen',
    address: `${Math.floor(Math.random() * 100) + 1} Johnson Ave`,
    city: 'Brooklyn',
    state: 'NY',
    zipcode: '11206',
}

//YOUR CODE GOES DOWN HERE:
let fullAddress = `${restaurant.address}, ${restaurant.city}, ${restaurant.state}, ${restaurant.zipcode}`;
```


<h2 id="u3">3. Modify Data</h2>
<p>|____________________________|</p>

```javascript
const midterms = {dany : 55, thomas:78};

// change thomas to 79
midterms.thomas = 79;
midterms.dany = 55;

//Add a new element to object;
midtterms.ezz = '88';
midtterms.antonio = '98';

```

<h2 id="u4">4. Nesting Arrays & Objects</h2>
<p>|_____________________________________________|</p>

<h4>Array of Objects </h4>

```javascript
// Array of objects;

const shoppingCard = [
    {
        product: 'Jenga',
        price: 9.99,
        quantity: 3
    },{
        product: 'benga',
        price: 9.99,
        quantity: 4
    },{
        product: 'daih',
        price: 9.99,
        quantity: 22
    },{
        product: 'Jenga',
        price: 9.99,
        quantity: 3
    }
];

shoppingCard[0].product; //benga
```

<h4>Objects having array</h4>

```javascript
// obj of arrays;

const student = {
    firstName: "David",
    strengths : ['Music', 'Art'],
    exams:{
        midterm: 88,
        final: 92
    }
    
};
```