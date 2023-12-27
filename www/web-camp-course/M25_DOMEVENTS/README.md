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
    <li><a href="#u1">1. preventDefault Form</a></li>
    <li><a href="#u2">2. extractDataFrom Form</a></li>
</ul>

[DOM MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)



<h2 id="u1">1. preventDefault Form</h2>
<p>|____________________________|</p>

```javascript
/*
Prevent Default of submiting a form and staying on the same page;
* */


const form = document.querySelector(form);

form.addEventListener('submit', function (e){
    e.preventDefault(); // prevent default;
    console.log("Submited Form!");
})
```


<h2 id="u2">2. extractDataFrom</h2>
<p>|____________________________|</p>

```html

<form action="/somewhere" id="#form">
    <label for="catName">Enter Something: </label>
    <input type="text" name="catName" id="catName">
</form>
```

```javascript
const input = document.querySelector('#catName');

const form = document.querySelector('#form');

const list = document.querySelector("#list");

form.addEventListener('submit',function (e){
    e.preventDefault();
    console.log("Submited;");
    console.log(input.value);
    const catName  = input.value;
    const newLLi = document.createElement('LI');
    
    newLLi.innerText = catName;
    
    list.append(newLLi);
})



// input.value; important property;

```


<h2 id="u3">3. Change  / Input Event</h2>
<p>|____________________________|</p>

```javascript
/*
* Change event ,when we click away  something;
* This even will be triggered when the data is different, and click away;
* */

//Real time changing h1

const input = document.querySelector('input');
const h1 = document.querySelector('h1');

input.addEventListener('change', function (c){
    console.log(c);
});



input.addEventListener('input', function (e){
    h1.innerText = e.value;
})


```