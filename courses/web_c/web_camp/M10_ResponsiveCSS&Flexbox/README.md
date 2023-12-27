
<h1>Module 10. Responsive CSS & Flexbox</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[WHAT IS FLEX HTML](/m10_WHATIsFLEXBOX.html)
<>
[WHAT IS FLEX CSS](/m10_WHATIsFLEXBOX.css)
<br>
[MEDIAQ HTML](/m10_MediaQ.html)
<>
[MEDIAQ CSS](/m10_MediaQ.css)
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>
    <li><a href="#u1">1. Flex Model & Flex Direction;</a></li>
    <li><a href="#u2">2. justify-content;</a></li>
    <li><a href="#u3">3. flex-wrap;</a></li>
    <li><a href="#u4">4. align-items;</a></li>
    <li><a href="#u5">5. align-content;</a></li>
    <li><a href="#u6">6. align-self;</a></li>
    <li><a href="#u7">7. FLEX-SIZING Properties;</a></li>
    <li><a href="#u8">8. Responsive Design & Media Queries;</a></li>
</ul>

<h2>HTML BOILERPLATE</h2>

```html
<h1>Let's Play With Flexbox</h1>

<section id="container">
    <div style="background-color: #80ffdb"></div>
    <div style="background-color: #64dfdf"></div>
    <div style="background-color: #48bfe3"></div>
    <div style="background-color: #5390d9"></div>
    <div style="background-color: #6930c3"></div>
</section>
```

<h2 id="u1">1. Flex Model & Flex Direction </h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+|
| What's FLEXBOX?                                                          |
| ** One-dimensional layout to lay items in rows and cols.                 |
+-------------------------------------------------------------------------+|
|THE FLEX MODEL
|
        ^
        |
        |       MAIN AXIS
  <_____|___________________________________________>
        |
        |
        |
        |
        | CROSS AXIS
|
+-------------------------------------------------------------------------+|
|1. FLEX DIRECTION                                                         |
|__________________|                                                       |
|The WAY MAIN AXIS BEHAVES IS DEPEND ON flex-direction;                    |
+-------------------------------------------------------------------------+|
|flex-direction: row; (PUT MAIN AXIS LEFT TO RIGHT)                        |
|flex-direction: row-reverse;  (PUT MAIN AXIS RIGHT TO LEFT)               |
+-------------------------------------------------------------------------+|
*/

#container{
    display: flex;
    flex-direction: row;
    flex-direction: row-reverse;
}

/*
+-------------------------------------------------------------------------+|
|flex-direction: column;                                                   |
|flex-direction: column-reverse;                                           |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    flex-direction: column;
    flex-direction: column-reverse;
}

```

<h2 id="u2">2. justify-content </h2>
<p>|____________________________|</p>

```css
/*
+-------------------------------------------------------------------------+|
|2. JUSTIFY-CONTENT(MAIN AXIS)                                             |
|______________________________|                                           |
|* Center content on the MAIN AXIS                                         |
|justify-content: center;                                                  |
+-------------------------------------------------------------------------+|
*/

#container{
    display: flex;
    justify-content: center;
}

/*
+-------------------------------------------------------------------------+|
|* Position content on the start of MAIN AXIS(LEFT)                        |
|justify-content: flex-start;                                              |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    justify-content: flex-start;
}

/*
+-------------------------------------------------------------------------+|
|* Position content on the end of MAIN AXIS(RIGHT)                         |
|justify-content: flex-end;                                                |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    justify-content: flex-end;
}

/*
+-------------------------------------------------------------------------+|
|* Take the extra space and distribute between the elements;               |
|justify-content: space-between;                                           |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    justify-content: space-between;
}

/*
+-------------------------------------------------------------------------+|
|* Take the extra space and distribute around the elements;                |
|justify-content: space-around;                                            |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    justify-content: space-around;
}

/*
+-------------------------------------------------------------------------+|
|* Take the extra space and distribute evenly to  elements;                |
|justify-content: space-evenly;                                            |
+-------------------------------------------------------------------------+|
*/
#container{
    display: flex;
    justify-content: space-evenly;
}
```

<h2 id="u3">3. flex-wrap </h2>
<p>|_____________________|</p>

```css
/*
|3. FLEX-WRAP (WRAP the elements along the MAIN AXIS)                      |
|____________________________________________________|                     |
| * Into a new line IF HORIZONTAL;                                         |
| * into a new column IF VERTICALLY;                                       |
| ** ALIGN-CONTENT works only when we use FLEX-WRAP also;                  |
+-------------------------------------------------------------------------+|
*/

#container{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap:wrap;                                                           |
    flex-wrap:wrap-reverse;
}
```

<h2 id="u4">4. align-items</h2>
<p>|_____________________|</p>

```css
/*
|4. ALIGN-ITEMS(ALIGN ITEMS ALONG THE CROSS AXIS)                          |
|_________________________________________________|                        |
|align-items: center;                                                      |
|align-items: baseline;                                                    |
+-------------------------------------------------------------------------+|
|align-items: flex-start;                                                  |
|align-items: flex-end;                                                    |
+-------------------------------------------------------------------------+|
*/

#container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    align-items: flex-end;
    align-items: center;
    align-items: baseline;
}
```

<h2 id="u5">5. align-content </h2>
<p>|_____________________|</p>

```css
/*
5. ALIGN-CONTENT                                                           |
|_________________|                                                        |
| * CONTROL AND DISTRIBUTE space along the CROSS AXIS;                     |
| ** ALIGN-CONTENT works only when we use FLEX-WRAP also;                  |
| align-content: space-between;                                            |
| align-content: flex-start;                                               |
+-------------------------------------------------------------------------+|
*/

#container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-content: flex-start;
    align-content: flex-end;
    align-content: space-between;
    align-content: space-around;
    align-content: space-evenly;

```

<h2 id="u6">6. align-self </h2>
<p>|_____________________|</p>

```css
/*
6. ALIGN-SELF(works only with SINGLE ELEMENTS;)                            |
|_______________________________________________|                          |
|align-self: center;                                                       |
+-------------------------------------------------------------------------+|
*/

#container div:nth-of-type(3){
    /*SELF*/
    align-self: center;
}
```


<h2 id="u7">7. FLEX-SIZING Properties;</h2>
<p>|_________________________________________|</p>

<h3>flex-basis</h3>
<p>|____________|</p>

```css
/*
|----------------------------------------------------------------------------------|
| 1. FLEX-BASIS
| * Define initial size of an element before additional space distribution;
|----------------------------------------------------------------------------------|
*/

#container div:nth-of-type(2){
    flex-basis: 400px;
}
```

<h3>flex-grow</h3>
<p>|____________|</p>

```css
/*
|----------------------------------------------------------------------------------|
| 2. FLEX-GROW
| * Control the amount of available space an element should take up; 
| * We telling how much to grow according to the other elements;  
| * Accepts a unit-less number value: 1, 2, 3
|----------------------------------------------------------------------------------|
*/

#container div:nth-of-type(2){
    flex-basis: 400px;
    flex-grow: 1;
}
```


<h3>flex-shrink</h3>
<p>|____________|</p>

```css
/*
|----------------------------------------------------------------------------------|
| 3. FLEX-SHRINK
| * If items are larger then the container , they shrink according to flex-shrink;
| * We telling how much to shrink according to the other elements;  
| * Accepts a unit-less number value: 1, 2, 3
|----------------------------------------------------------------------------------|
*/

#container div:nth-of-type(3){
    flex-basis: 400px;
    flex-grow: 1;
    flex-shrink: 2;
}
```


```html
<main>
    <div class="sidebar"></div>
    <div class="maincontent"></div>
</main>
```

<h3>Flex Shorthand</h3>
<p>|___________________|</p>

```css
/*
|----------------------------------------------------------------------------------|
| 4. FLEX SHORTHAND;
|flex : flex-grow | flex-shrink | flex-basis;
|----------------------------------------------------------------------------------|
*/

main{
    width: 80%;
    margin: 0 auto;
    border: 5px solid black;
    height: 500px;
    /*Starting flex*/
    display: flex;
}

main .sidebar{
    background-color: #6930c3;
    flex: 1 2 300px;
}

main .maincontent{
    background-color: #80ffdb;
    flex: 2 600px;
}
```


<h2 id="u8">8. Responsive Design & Media Queries ;</h2>
<p>|_______________________________________________________________|</p>

```css
/*
|----------------------------------------------------------------------------------|
| MEDIA QUERIES
| * MQ allow to modify our style depending on parameters like screen width or device type;
|
| Syntax:
| @media(parameter) and (parameter) {
|   h1{
        something;    }
|   }
|
|----------------------------------------------------------------------------------|
*/

/*768px media responsive*/
@media(max-width: 768px){
    h1{
        font-size: 4em;
    }
}

/*576px media responsive*/

@media(max-width: 576px){
    h1{
        font-size: 2em;

    }
    nav{
        flex-direction: column;
        align-items: center;
    }
}
```

