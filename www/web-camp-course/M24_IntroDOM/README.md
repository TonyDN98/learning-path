<h1>Module 24. Intro DOM</h1>
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
    <li><a href="#u1">1. intro DOM</a></li>
    <li><a href="#u2">2. getElementByID</a></li>
    <li><a href="#u2">3. getElementByTagName</a></li>
    <li><a href="#u2">4. getElementByClassName</a></li>
    <li><a href="#u2">5. querySelector && querySelectorAll</a></li>
    <li><a href="#u2">6. innerHTML,textContent, innerText</a></li>
    <li><a href="#u2">7. Attributes;</a></li>
    <li><a href="#u2">8. classList;</a></li>
</ul>

[DOM MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

<h3>Properties & Methods</h3>
<ul>
    <li><a href="#">getAttribute() </a></li>
    <li><a href="#">setAttribute() </a></li>
    <li><a href="#">append()</a></li>
    <li><a href="#">appendChild()</a></li>
    <li><a href="#">remove()</a></li>
    <li><a href="#">removeChild()</a></li>
    <li><a href="#">classList</a></li>
    <li><a href="#">createElement </a></li>
    <li><a href="#">innerText textContent innerHTML</a></li>
    <li><a href="#">value</a></li>
    <li><a href="#">parentElement</a></li>
    <li><a href="#">child</a></li>

</ul>



<h2 id="u1">1. intro DOM</h2>
<p>|____________________________|</p>

```javascript
/*
* Intro DOM
* Document Object Model
* Incoming HTML CSS -> Js Object come out
* Every element in HTML will become a object;
* SELECTING  --> MANIPULATE
* 
* SELECTING:
*   getElementById
*   getElementByTagName
*   getElementByClassName
* */

```

<h2 id="u2">2. getElementByID</h2>
<p>|____________________________|</p>

```javascript
/*
* SELECTING THINGS USING JS;
* Retrive the DOM Object coresponding to a element;
* 
* */

document.dir();
document.getElementById('banner');

const bannerVar = document.getElementById('banner');
console.dir(bannerVar);

// Write your code in here:
let image = document.getElementById('unicorn');

let heading = document.getElementById('mainheading');
```

<h2 id="u3">3. getElementByTagName</h2>
<p>|____________________________|</p>

```javascript
/*
* 
* 
* 
* */

const allImages = document.getElementsByTagName('img');

for (let img of allImages){
    console.log(img.src);
}

```

<h2 id="u4">4. getElementByClassName</h2>
<p>|____________________________|</p>

```javascript
/*
* 
* 
* 
* */

const squareImages = document.getElementsByClassName('square');

for (let img of squareImagesImages){
    img.src = 'https://SomewhereElse';
}
```

<h2 id="u5">5. querySelector && querySelectorAll</h2>
<p>|____________________________|</p>

```javascript
// querySelector returns only the first encouterd element;
// querySelectorAll return a collection of  macking elements;

// by element
document.querySelector('h1');

// by class or id
document.querySelector('#red');


document.querySelector('.big');


document.querySelectorAll('p'); // 22

document.querySelectorAll('p a'); // using css selectors;

const links = document.querySelectorAll('p a');
for (let link of links){
    console.log(link.href);
}


const doneTodos = document.querySelectorAll('.done');

const checkbox = document.querySelector("input[type='checkbox']");

```

<h2 id="u6">6. innerHTML,textContent, innerText</h2>
<p>|____________________________|</p>

```javascript
/*
* 
* 
* */


document.querySelector('p').innerText = 'lolololo';

// format comes code format , dosent matter css
document.querySelector('p').textContent = 'lolololo';


// innerHTML, give full access to control the element itself too;
document.querySelector('p').innerHTML = '<i>Something</i>';

```

<h2 id="u7">7. Attributes;</h2>
<p>|____________________________|</p>

```javascript
/*
* firstLink.getAttribute('href');
* THE WHOLE POINT OF getting an atrrbiute and manupate it, maybe at some point we wanna
* change that atrribute, from an inpute text to a password dunno;
* */

// .id atribute
const bannerVar = document.querySelectorAll('banner').id;

// .src
const bannerVar = document.querySelectorAll('img').src;

// .href
const bannerVar = document.querySelector(a).href;

// .title
const bannerVar = document.querySelector('a').id;


const firstLink = document.querySelector(a).href;
firstLink.getAttribute('href');


const img = document.querySelector('img');

img.getAttribute('href');
img.src = 'https://devsprouthosting.com/images/chicken.jpg';
img.alt = 'chicken';

// setAttribute

img.getAttribute('class');
img.setAttribute('class', 'purpleClass');


```

<h2 id="u8">8. classList;</h2>
<p>|____________________________|</p>

```javascript
/*
* ClasList is used to retrive and set the element class attribute;
* */

const img = document.querySelector('img');
img.classList; // square;
// much better then setAttribute()
img.classList.add('purple'); // adding another class to the current class and so on;
img.classList.remove('purple'); // remove another class to the current class and so on;
img.classList.toggle('purple'); // useful when we have another toggle classes;
```



<h2 id="u8">0. Styles;</h2>
<p>|____________________________|</p>

```javascript
/*
* We can change styles also using DOM manipulation but its not ideal to  do it
* one style at a tme, especially inline styling;
* 
* */
```

