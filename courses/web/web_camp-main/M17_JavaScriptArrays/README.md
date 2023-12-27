<h1>Module 17. JavaScript Arrays</h1>
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
    <li><a href="#u1">1. Intro</a></li>
    <li><a href="#u2">2. Access Index Positions</a></li>
    <li><a href="#u3">3. Array Methods </a></li>
    <li><a href="#u4">4. Concat & IndexOf, includes & reverse </a></li>
    <li><a href="#u5">5. </a></li>
    <li><a href="#u6">6.  </a></li>
    <li><a href="#u7">7. </a></li>
</ul>

[MDN Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

<h2 id="u1">1. Intro</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* INTRO Arrays
* +-------------------------------------------------------------------------+|
*  ** Ordered collections of values (order of a playlist)
*  ** Index starts from 0 to n - 1
*  ** array.length
 */
```

```javascript
// Make a empty string;
let student = [];

// Array of strings ;
let colors = ['red', 'green', 'blue'];

// Array of numbers ;
let colors = [1,100, 200, 30001];

// Mixed Array;
let mixedArr = ['123', 24, 'name', 50, null];

// typeof
typeof(color); //object


```


<h2 id="u2">2. Access Index Positions</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* Access Index Arrays
* +-------------------------------------------------------------------------+|
* Just like Strings, Arrays start from index 0 to n - 1;
* array.length;

 */

 mixedArr[0]; //'123'
 mixedArr[1]; //  24
 mixedArr[2]; // 'name'
 mixedArr[3]; // 50
```

<h2 id="u3">3. Array Methods</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* Array Methods
* +-------------------------------------------------------------------------+|
* Push - add to end;
* Pop - remove from end;
* Shift - remove from  start;
* Unshift - add to start;
*  +-------------------------------------------------------------------------+|
* */
// add to start
movieLine.unshift("thomas", 'edison');


// add to end
let movieLine = ['tom', 'nancy'];
movieLine.push('dodo');
movieLine.push('marry');
movieLine.push('harry', 'hermione'); // multiple elements add;

// remove from start
movieLine.shift(); // remove from the start of  array and returns that elemenet
let firstElement = movieLine.shift(); // tom

// remove from end;
movieLine.pop(); // remove from end of array and returns that elemenet
let lastElement = movieLine.pop(); // hermione
```

<h2 id="u4">4. Concat & IndexOf, includes & reverse</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
* More Methods
* concat - merge arrays;
* includes - look for a value and return TRUE OR FALSE;
* indexOf - indexOf
* join - create a string from an array; IMP
* reverse - reverse an array;
* slice - copy a portion on an array;
* splice - remove replace elements;
* sort - sort an array;
 */

```


```javascript
/*
* CONCAT
* array1.concat(array2)
* */

let array1 = [1,2,3];
let array2 = [4,5,6];
let array3 = array1.concat(array2); // 1 2 3 / 4 5 6
let array4 = array2.concat(array1); // 4 5 6 / 1 2 3


/*
* Includes;
* Return true of there is a perfect match, false if not!
* */

let pets = ['doggo', 'kitty', 'alpaca', 'lionkitty'];
pets.includes("doggo"); // true
pets.includes("dog"); // false


/*
* indexOf(element);
* Return de index of the element in the array;
* */

pets.indexOf("kitty"); // 1
pets.indexOf("alpaca"); // 2
pets.indexOf("kitytyty"); // -1 not found

/*
* reverse(element);
* Reverse the array;
* array.reverse();
* */

array.reverse(); // 3, 2, 1

/*
* array.slice(indexStart, indexStop);
* Includes the stat, but not the stop index element;
* Slice a portion of an array;
* Both index are optional;
* */

let newArray = [1,2,3,4,5,6,7,8,9,10];
let sliceArray = newArray.slice(); // 1 .. 10
let sliceArray = newArray.slice(2,4); // 3, 4
let sliceArray = newArray.slice(4); // 5 .. 10

/*
* array.splice(startPos, deleteElements, replaceElement);
* Destructive to the original array'
* */

let months = ['Jan', 'March', 'April', 'June'];
months.splice(1,0,'Feb');
// ['Jan','Feb' 'March', 'April', 'June']


/**/
```

<h2 id="u5">4. Constant Arrays</h2>
<p>|____________________________|</p>

```javascript
// CONSTANT ARRAY;

const array1 = [1, 2, 3, 4, 5];
```

<h2 id="u5">5. Multi Dimensional Arrays</h2>
<p>|____________________________|</p>

```javascript
/* Multi Dimenisonals Arrays;
     0       1      2     3    4
|0   [0.0] [0.1] [0.2] [0.3] [0.4]
|1   [1.0] [1.1] [1.2] [1.3] [1.4]
|2   [2.0] [2.1] [2.2] [2.3] [2.4]
|3   [3.0] [3.1] [3.2] [3.3] [3.4]
|4   [4.0] [4.1] [4.2] [4.3] [4.4]
* */

const array1 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
];
```


