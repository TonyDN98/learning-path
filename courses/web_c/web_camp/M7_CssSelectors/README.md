
<h1>Module 7. Css Selectors</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>

[m7_cssSelectors.html HTML File](m7_cssSelectors.html)<br>
[m7_cssSelectors.css CSS File](m7_cssSelectors.css)
<p>|____________________________________|</p>


<h2>II. Practice Content</h2>
[M7_Practice/m7_SelectorPractice.html HTML File](M7_Practice/m7_SelectorPractice.html)<br>
[M7_Practice/m7_SelectorPractice.css CSS File](M7_Practice/m7_SelectorPractice.css)
<p>|____________________________________|</p>

[M7_Practice/m7_PseudoPractice.html HTML File](M7_Practice/m7_PseudoPractice.html)<br>
[M7_Practice/m7_PseudoPractice.css CSS File](M7_Practice/m7_PseudoPractice.css)

<p>|____________________________________|</p>

<br>

[M7_Practice/m7_DescendentSelectorPractice.html HTML File](M7_Practice/m7_DescendentSelectorPractice.html) <br>
[M7_Practice/m7_DescendentSelectorPractice.css CSS File](M7_Practice/m7_DescendentSelectorPractice.css)


<h2>WHAT'S THE MATTER IN THIS SECTION?</h2>
<p>|_____________________________________________________________________|</p>

<p id="goup"></p>
<ul>
    <li><a href="#u1">1. Universal Selector </a></li>
    <li><a href="#u2">2. Element Selector </a></li>
    <li><a href="#u3">3. SELECTOR LIST</a></li>
    <li><a href="#u4">4. ID Selector</a></li>
    <li><a href="#u5">5. CLASS Selector </a></li>
    <li><a href="#u6">6. DESCENDANT SELECTOR</a></li>
    <li><a href="#u7">7. ADJACENT SELECTOR </a></li>
    <li><a href="#u8">8. DIRECT CHILD SELECTOR </a></li>
    <li><a href="#u9">9. ATTRIBUTE SELECTOR</a></li>
    <li><a href="#u10">10. PSEUDO CLASSES </a></li>
    <li><a href="#u11">11. PSEUDO Elements </a></li>
    <li><a href="#u12">12. The CASCADE</a></li>
    <li><a href="#u13">13. The Specifity</a></li>
    <li><a href="#u14">14. !important;</a></li>
</ul>



<h2 id= "u1">1. Universal Selector</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+|
|Universal Selector                                                        |
|* {color:black;}  >- select every element on the page, dont use it!       |
|+-------------------------------------------------------------------------+
*/      
```
<hr>

```css
/*+--------------------------Universal Selector-----------------------------+*/
* {
  color: pink;
  }
/*+-------------------------------------------------------------------------+*/
```
<hr><br>

<h2 id= "u2">2. Element Selector</h2>
<p>|____________________________|</p>

```css
/*
+-----------------------------------+|
|Element Selector                    |                                       
|img { background-color: pink; }     |
|h2 { font-size: 20px; }             |
+-----------------------------------+|
*/
```

```css


/*+------------Element Selector----SELECTOR LIST----------------------------+*/

button {
background-color: purple;
font-size: 20px;
}

h1,h2 {
color: darkslateblue;
letter-spacing: 1px;
text-decoration: underline wavy;
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u3">3. SELECTOR LIST</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
SELECTOR LIST
h1,h2 {font-family: verdana;}
+-------------------------------------------------------------------------+
*/
```

```css


/*+------------Element Selector----SELECTOR LIST----------------------------+*/

button {
background-color: purple;
font-size: 20px;
}

h1,h2 {
color: darkslateblue;
letter-spacing: 1px;
text-decoration: underline wavy;
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u4">4. ID Selector</h2>
<p>|____________________________|</p>


```css
/*
+-------------------------------------------------------------------------+
ID SELECTOR (uniq id per elements;)
#id { font-size: 20px; }
** Don't be scared of using them, but don't use it to style every element separately;
+-------------------------------------------------------------------------+
*/
```

```css

/*+------------------------------ID SELECTOR--------------------------------+*/

#logoutbutton{
background-color: pink;
color: purple;
font-size: 20px;
font-family: Verdana,sans-serif;
}

#loginbutton{
font-family: monospace,sans-serif;
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u5">5. CLASS Selector</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
CLASS SELECTOR (a class can have multiple elements;) ( will be used far more often then ids)
.class {
font-family: verdana;
}
+-------------------------------------------------------------------------+
*/
```

```css
/*+----------------------------CLASS SELECTOR-------------------------------+*/

.tag{
font-size: 15px;
/*color: deeppink;*/
/*background-color: purple;*/
}

/*+-------------------------------------------------------------------------+*/
```

```css

/*+----------------------------CLASS SELECTOR-------------------------------+*/

.tag{
    font-size: 15px;
    /*color: deeppink;*/
    /*background-color: purple;*/
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u6">6. DESCENDANT SELECTOR</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
DESCENDANT SELECTOR (select all y elements that are nested in the x)

** all a elements nested in the li
li a {
color:black;
}

** works with class or ids too:

.post a{
color:blue;
}
+-------------------------------------------------------------------------+
*/
```

<hr><br>

<h2 id= "u7">7. ADJACENT SELECTOR</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
ADJACENT SELECTOR (Select only the first preceded y by x)
h1 + p { color:red;}
x + y { color:red; }
+-------------------------------------------------------------------------+
*/
```

<hr><br>

<h2 id= "u8">8. DIRECT CHILD SELECTOR</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
DIRECT CHILD SELECTOR (Select the direct child on the parent element) (1 level down)
<div>
 <h2>H2</h2>
         <ul>
         <li></li>
               <li></li>
                     <li></li>
                           </ul>
                             </div>

                               div > li{
                                   color:pink;
                               }
+-------------------------------------------------------------------------+
*/
```

```css
/*+---------------------DIRECT CHILD SELECTOR-------------------------------+*/

.post a {
color: #e63946;
}

li a {
color: purple;
}

input + button {
background-color: black;
}

h2 + button {
color: black;
font-size: 25px;
}

footer > nav > ul > li > a {
/*color: #ffd6ff;*/
color: blue;
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u9">9. ATTRIBUTE SELECTOR</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
ATTRIBUTE SELECTOR
(Select all input elements where the type attribute is set to text or password)

input[type = "text"] { color:black;}
input[type = "password"] { background-color: pink;}
+-------------------------------------------------------------------------+
*/
```

```css
/*+------------------------ATTRIBUTE SELECTOR-------------------------------+*/


input[type = "text"] {
color: pink;
}

input[type="password"] {
color: purple;
}

/*+-------------------------------------------------------------------------+*/
```

<hr><br>

<h2 id= "u10">10. PSEUDO CLASSES</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
PSEUDO CLASSES(keyword added to a selector that specifies the state of the element)
:active
:checked
:first
:first-child
:hover
:not()
:nth-child()
:nth-of-type(3 post or 2n(even), 3n)

(Cursor Hover over the element)
#loginbutton:hover{
background-color: pink;
color: purple;
}

(Element clicked)
#loginbutton:active{
background-color: pink;
color: purple;
}
+-------------------------------------------------------------------------+
*/

```
````css
/*+-----------------------PSEUDO CLASSES------------------------------------+*/
#loginbutton:hover{
background-color: pink;
color: purple;
}

#loginbutton:active{
background-color: green;
color: purple;
}

#logoutbutton:hover{
background-color: black;
color: pink;
}

a:hover {
text-decoration: underline wavy;
font-size: 15px;
font-family: Verdana,monospace;
}

/*.post:nth-of-type(3n){
background-color:#ff4d6d ;
}*/

/*+-------------------------------------------------------------------------+*/
````

<hr><br>


<h2 id= "u11">11. PSEUDO ELEMENTS</h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+
PSEUDO ELEMENTS(Let's you style a particular part of the selected element)
::after
::before
::first-letter >- first letter on an h2 or
::first-line
::selection >- when we highlight a paragraph or some text;

h2::first-letter{
color:black;
}
+-------------------------------------------------------------------------+
*/
```

```css
/*+--------------------------PSEUDO ELEMENTS--------------------------------+*/
h2::first-letter{
font-size: 50px;
}
*::selection{
background-color: green;
}


a::before{
content: "->";
}

a::after{
content: "<-";
}
/*+-------------------------------------------------------------------------+*/

```

<h2 id= "u12">12. THE CASCADE</h2>
<p>|____________________________|</p>

```css
/*
|---------------------------------------------------------|
|The order your styles are declared and lined to matter!  |
|---------------------------------------------------------|
*/

h1 {
    color: red;
}

h1 {
    color: purple;
}

/* PURPLE WIN!! */
```


<h2 id= "u13">13. THE Specifity</h2>
<p>|____________________________|</p>

```css
/*
|-------------------------------------------------------------------------------------|
|Specifity is how the browser decides which rules to apply when there is a conflict;  |
|-------------------------------------------------------------------------------------|
| SELECTORS have levels or priority                                                   |
|    ID > CLASS > ELEMENT                                                             |
|-------------------------------------------------------------------------------------|    
|    Specifity calculator in case of conflict;                                        |
|                                                                                     |
|    ID   |   CLASS   |   ELEMENT                                                     |
|-------------------------------------------------------------------------------------|    
|    1    |    0      |       0                                                       |
|-------------------------------------------------------------------------------------|    
|    0    |    2      |       1                                                       |
|-------------------------------------------------------------------------------------|
*/
```

<hr>

<h2 id= "u14">14. !important;</h2>
<p>|____________________________|</p>

```css
/*
|--------------------------------------!important;--------------------------------------------------|
|---------------------------------------------------------------------------------------------------|
|!important; use it when don't have necessarily controlrol over and you are trying to change        |
|or override something using an external library;                                                   |
|---------------------------------------------------------------------------------------------------|
|!important; will make the style high priority in terms of specifityl                               |
|---------------------------------------------------------------------------------------------------|
*/
```

```css
h1,h2,h3 {
    color:red;
}

h2 {
    color: pink !important;
} 
/* pink  wins */
```
<hr>

<h2 id= "u15">15. Css Inheritance</h2>
<p>|____________________________|</p>

```html



<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CSS Inheritance</title>
</head>
<body>
<main>
    <h1>Heading 1</h1>
    <p>lorem</p>
</main>

<section>
    <h2>Heading 2</h2>
    <p>Lorem</p>
    <p>Lorem</p>
</section>

<section>
    <form action="">
        <label for="user">Username:</label>
        <input type="text" name="user" id="user">
        <button>Click me!</button>
    </form>
</section>

<footer>
    <span>Something here &copy;</span>
</footer>

</body>
</html>
```

```css
/*
This will pass for subchild elements automatically color blue;
<body>
    <main>
        <h1>;
        <p>; 
    <section>
        <h2>
        <p>
        <form>
    <footer>
        <span>
*/

body{
    color: blue;
}

/*From here being more specific h1 will be red;*/
h1 {
    color:red;
}

/*All child elements of section;*/
section {
    color: magenta;
}

/*Specify to the attribute to inherit from his parent element;*/
button, input{
    color: inherit;
}
```
