<h1>Module 29. OOP</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[]()
<>
[]()
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>`
    <li><a href="#u1">1. Class</a></li>
    <li><a href="#u2">2. Constructor Function</a></li>
    <li><a href="#u3">3. Extends Keyword</a></li>
    <li><a href="#u4">4. Super Keyword;</a></li>
</ul>



<h2 id="u1">1. Class;</h2>
<p>|____________________________|</p>

```javascript
// Class Declaration
class Rectangle {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
}

```



<h2 id="u1">2. Constructor Function;</h2>
<p>|____________________________|</p>


```javascript
/*
* Specific () of a class;
* Used to create and initialize objects;
* Custom initlialization using and having multiple parameters;
* */

// default constructor if not specified; and creating a new object;

constructor();

class Polygon {
    constructor() {
        this.name = 'Polygon';
    }
}

const poly1 = new Polygon();

console.log(poly1.name);
// expected output: "Polygon"


```

<h4> Constructor Multiple Arguments;</h4>

```javascript

constructor() { /* … */ }
constructor(argument0) { /* … */ }
constructor(argument0, argument1) { /* … */ }
constructor(argument0, argument1, /* … ,*/ argumentN) { /* … */ }


```


<h2 id="u1">3. Extends Keyword;</h2>
<p>|____________________________|</p>


```javascript
// Extending a subclass of a superclass;

class Square extends Polygon {
  constructor(length) {
    // Here, it calls the parent class' constructor with lengths
    // provided for the Polygon's width and height
    super(length, length);
    // Note: In derived classes, super() must be called before you
    // can use 'this'. Leaving this out will cause a reference error.
    this.name = 'Square';
  }

  get area() {
    return this.height * this.width;
  }
}

```


<h2 id="u1">4. Super Keyword;</h2>
<p>|____________________________|</p>

```javascript
// Used for accesing content of the super Class that is extended;
class Rectangle {
    constructor(height, width) {
        this.name = 'Rectangle';
        this.height = height;
        this.width = width;
    }
    sayName() {
        console.log('Hi, I am a ', this.name + '.');
    }
    get area() {
        return this.height * this.width;
    }
    set area(value) {
        this._area = value;
    }
}

class Square extends Rectangle {
    constructor(length) {
        this.height; // ReferenceError, super needs to be called first!

        // Here, it calls the parent class's constructor with lengths
        // provided for the Rectangle's width and height
        super(length, length);

        // Note: In derived classes, super() must be called before you
        // can use 'this'. Leaving this out will cause a reference error.
        this.name = 'Square';
    }
}

```

