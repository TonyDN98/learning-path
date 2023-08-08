
<h1>Module 6. CSS Basics</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[|<<m6_CSSTextPropertiess HTML File>>|](m6_CSSBasics.html) <br>
[|<<m6_CssBasics CSS File>>|](CSSBasics.css)
<p>|____________________________________|</p>

[|<<m6_CssTextProperties HTML File>>|](m6_CSSTextPropertiess.html) <br>
[|<<m6_textproperties CSS File>>|](textproperties.css)
<p>|____________________________________|</p>


<h2>II. Practice Content</h2>
[|<<m6_CSSPractice1 HTML File>>|](M6_Practice/m6_CSSPractice1.html) <br>
[|<<m6_CSSPractice1 CSS File>>|](M6_Practice/styles.css)
<p>|____________________________________|</p>

[|<<m6_CSSPractice2 HTML File>>|](M6_Practice/m6_CSSPractice2.html) <br>
[|<<m6_CSSPractice2 CSS File>>|](M6_Practice/cssPractice2.css)
<p>|____________________________________|</p>


<h2>1. WHAT'S THE MATTER IN THIS SECTION?</h2>
<p>|_____________________________________________________________________|</p>

<p id="goup"></p>
<ul>
    <li><a href="#u2">2. Basic Css Syntax;</a></li>
    <li><a href="#u3">3'. Include External CSS File</a></li>
    <li><a href="#u31">3```. Different types of styling;</a></li>
    <li><a href="#u4">4. Color/Background-color Scheme: RGB, Hex</a></li>
    <li><a href="#u41">4.1 Named Colors</a></li>
    <li><a href="#u42">4.2 RGB Colors[RGB(R,G,B)]</a></li>
    <li><a href="#u43">4.3 HEX Colors[#FFFF00] </a></li>
    <li><a href="#u5">5. Common Text Properties_ </a></li>
    <li><a href="#u6">6. Font-Family</a></li>
</ul>

```css
/*
|-----------------------------------|
|CRUCIAL:                           |
|2. Basic CSS Syntax;               |
|-----------------------------------|
|3. Including Styles Correctly;     |
|                                   |
|4. Color Scheme: RGB, Hex, etc;    |
|-----------------------------------|
|5. Common Text Properties;         |
|-----------------------------------|
|6. font-family property;           |
|-----------------------------------|
*/
```

<h2 id="u2">2. Basic Css Syntax;</h2>
<p>|_________________________________|</p>

```css
/*BASIC SYNTAX OF CSS*/

selector {
    color : blue;
}

h1 {
    color : purple;
}

img {
    width : 100px;
    height: 200px;
}
```
<hr><br>


<h2 id="u3">3'. Include External CSS File</h2>
<p>|_____________________________________________|</p>

[Link to m6_CssBasics](CSSBasics.css)
```html
Link external css files with link element;
<link rel="stylesheet" href="CSSBasics.css">
<!-- 
+-------------------------------------------------------------------------+
Always use an external style sheet it's the recommended way;
+-------------------------------------------------------------------------+
-->
```

<h2 id="u31">3```. Different types of styling;</h2>
<p>|_______________________________________________|</p>

```html
<!----------------------->
<!---INLINE STYLES BAD!-->
<!----------------------->

<h1 style="color: purple;">Hello World!</h1>
<button style="background-color: aquamarine;">I'm button</button>

<!----------------------->
<!--- STYLE ELEMENT BAD!-->
<!----------------------->
<style>
    h2 {
       color: blue;
    }
</style>
<h2>I'm H2</h2>
<!-- ------------------------------------------------------------------------- -->
```

<hr><hr>



<h2 id="u4">4. Color/Background-color Scheme: RGB, Hex</h2>
<p>|_______________________________________________________________________|</p>

[Link 4. Color/Background-color Scheme: RGB, Hex](CSSBasics.css)

```css
/* Changing Text Color */
h2 {
    color: red;
}

/* Changing Background Color */
h2 {
    background-color: blue;
}

/* Changing background */
h3 {
    background: green;
}

/*+-------------------------------------------------------------------------+*/

```
<hr>

<h3 id="u41">4.1 Named Colors</h3>
<p>|_____________________|</p>


```css
/* Named colors: green, magenta; Browsers support 140 names colors; */

h2 {
    color: purple;
/*  color: hotpink;
    color: pink;
*/
}
/*+-------------------------------------------------------------------------+*/
```

<hr>

<h3 id="u42">4.2 RGB Colors[RGB(R,G,B)]</h3>
<p>|________________________________|</p>

```css
/*
|------------------------------------------|
|RGB Colors(Red,Green,Blue):               |
|------------------------------------------|
|    * Each channel ranges from 0-255      |
|        * Red >- rgb(255,0,0);            |
|        * Blue >-  rgb(0,0,255);          |
|        * Black >- rgb(0,0,0);            |
|        * White >- rgb(255,255,255);      |
|------------------------------------------|
 */

h2 {
    color: rgb(255, 0, 0);
    background: rgb(0, 255, 0);
}
```
<hr>

<h3 id="u43">4.3 HEX Colors[#FFFF00]</h3>
<p>|_____________________________|</p>

```css
/*
|-----------------------------------------------------------------------|
|HEX Colors |Generally use hex-codes|                                   |
|    *Hexadecimal Colors: same as RGB BUT represented in hexadecimal;   |
|        #ff     ff      00                                             |
|        #red   green   blue                                            |
|-----------------------------------------------------------------------|
*/
```

```css
h2 {

    color: indigo;
    /*RGB code*/
    background-color: rgb(2, 161, 158);
}

button {
    color: magenta;
    background-color: cyan;
}

p {
    /*hexdecimal code*/
    color: #ff3311;
    background: orange;
}
```

<h2 id="u5">5. Common Text Properties</h2>
<p>|____________________________________________|</p>


```css
/*
CSS Text Properties
---------------------

|--------------------------------------------------|
|                                                  |
text-align >- text aligning                        |
|--------------------------------------------------|
|                                                  |
font-weight >- 100,200,300, normal(400),bold(700)  |
|--------------------------------------------------|
|                                                  |
text-decoration >- decorative lines on text;       |
|--------------------------------------------------|
|                                                  |
line-height >- set distance between lines of text  |
|--------------------------------------------------|
|                                                  |
letter-spacing >- set space between the letters;   |
|--------------------------------------------------|

|------------------------------|
|ABSOLUTE UNITS                |
|font-size >- the font size    |
|------------------------------|
|font-size: 15px;              |
|------------------------------|
*/
```
<hr>

```css
h1 {
    text-align: center;
    color: red;
    font-weight: normal;
    /*text-decoration: overline;*/
    /*text-decoration: blue underline;*/
    text-decoration: #ff3311 underline wavy;
    letter-spacing: 15px;
    /*font-size: 15px;*/
    /*font-size: 100px;*/

    /*backup fonts if the first choices in order its not available on the machine*/
    /*font-family: Verdana,sans-serif;*/
    font-family: fantasy;
}

p {
    text-align: center;
    font-weight: normal;
    line-height: 2; /* 2 x font size*/
    font-family: sans-serif;
}

a{
    text-decoration: none;
}

```

```css
/*
|---------------------------------------------------|
|ABSOLUTE UNITS                                     |
|PX >- By far the most commonly used absolute unit  |
|1px != with the width of exactly 1pixel            |
|NOT RECOMMENDED FOR RESPONSIVE WEBSITES;           |
|---------------------------------------------------|
*/

h2 {
    letter-spacing: 15px;
}
```

<h2 id="u6">6. Font-Family</h2>
<p>|______________________|</p>

```css
/*
FONT-FAMILY: Verdana,monospace; Every font-family has to have at least 1 backup font if the first one it's not found on the machine;
*/

h2{
    font-family: Verdana, monospace,sans-serif;
}
```
