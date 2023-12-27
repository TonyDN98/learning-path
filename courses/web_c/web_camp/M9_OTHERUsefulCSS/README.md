
<h1>Module 9. Other Useful Css</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>

[Opacity & Alpha Channel HTML](1.RGBA&AlphaChannel/m9_RGBA&AlphaChannel.html)
<>
[Opacity & Alpha Channel CSS](1.RGBA&AlphaChannel/m9_RGBA&AlphaChannel.css)
<br>
[Position Property HTML](2.PostionProperty/m9_PositionProperty.html)
<>
[Position Property CSS](2.PostionProperty/m9_PositionProperty.css)
<br>
[CSS Transitions YAY HTML](3.Transitions/m9_Transitions.html)
<>
[CSS Transitions YAY CSS](3.Transitions/m9_Transitions.css)
<br>
[CSS Transform HTML](4.Transform/m9_Transform.html)
<>
[CSS Transform CSS](4.Transform/m9_Transform.css)
<br>
[Practice / Fancy Button Hover Effect HTML](5.FancyButtonHoverEffect/m9_fancyButton.html)
<>
[Practice / Fancy Button Hover Effect CSS](5.FancyButtonHoverEffect/m9_fancyButton.css)
<br>
[Background HTML](6.Background/m9_Background.html)
<>
[Background CSS](6.Background/m9_Background.css))
<br>
[Google Fonts HTML](7.GoogleFonts/m9_GoogleFonts.html)
<>
[Google Fonts CSS](7.GoogleFonts/m9_GoogleFonts.css)
<br>
[PhotoBlog HTML](8.PhotoBlog/m9_PhotoBlog.html)
<>
[PhotoBlog CSS](8.PhotoBlog/m9_PhotoBlog.css)
[]()
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>

<p id="goUP"></p>
<ul>
    <li><a href="#u1">1. Opacity & Alpha Channel </a></li>
    <li><a href="#u2">2. Position Property</a></li>
    <li><a href="#u3">3. CSS Transitions YAY</a></li>
    <li><a href="#u4">4. CSS Transform</a></li>
    <li><a href="#u5">5. Practice / Fancy Button Hover Effect</a></li>
    <li><a href="#u6">6. Background</a></li>
    <li><a href="#u7">7. Google Fonts</a></li>
    <li><a href="">8. Practice / PhotoBlog</a></li>
</ul>

<h2 id="u1">1. Opacity & Alpha Channel </h2>
<p>|____________________________|</p>

```html
<section>
    <div id="rgba">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquid at, autem enim eum magnam minima mollitia nam nesciunt nostrum obcaecati odio reiciendis voluptatum. Delectus dignissimos et laborum possimus quos.
    </div>
</section>
<section>
    <div id="opacity">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquid at, autem enim eum magnam minima mollitia nam nesciunt nostrum obcaecati odio reiciendis voluptatum. Delectus dignissimos et laborum possimus quos.
        <button>Click</button>
    </div>

</section>
```

```css
/*
+-------------------------------------------------------------------------+|
|RGBA - Alpha Channel(Affects only the color itself, but not the content); |
|    0-1 value WHERE                                                       |
|    0 >- FULL Transparent;                                                |
|    1 >- NO Transparent;                                                  |
|RGBA(r,g,b, a)                                                            |
|RGBA(255,209,100, 0.5) QUICK LOOK and PREFERABLE;                         |
|HEX FF3311 00 - FF                                                        |
+-------------------------------------------------------------------------+|
|Opacity Property(Affects the color and content);s                         |
|    0-1 value WHERE                                                       |
|    0 >- FULL Transparent;                                                |
|    1 >- NO Transparent;                                                  |
|+-------------------------------------------------------------------------+
 */
section{
    width: 500px;
    height: 500px;
    background-color: magenta;
}

#rgba{
    width: 15%;
    height: 15%;
    /*background-color: rgba(255,255,255, 0.3);*/
    /*background-color: #ff331100;*/
    background-color: #ff3311FF;
}

#opacity{
    width: 500px;
    height: 500px;
    background-color: yellow;
    opacity: 0.5;
}
```


<h2 id="u2">2. Position Property </h2>
<p>|____________________________|</p>

```html

<h1>Position Property</h1>
<section id="static">
    <h2>Static</h2>
    <div></div>
    <div id="middle"></div>
    <div></div>
</section>

<section id="relative">
    <h2>Relative</h2>
    <div></div>
    <div id="middle-r"></div>
    <div></div>
</section>

<section id="absolute">
    <h2>Absolute</h2>
    <div></div>
    <div id="middle-a"></div>
    <div></div>
</section>

<section id="fixed">
    <h2>Fixed</h2>
    <div></div>
    <div id="middle-f"></div>
    <div></div>
</section>

<div>
    <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus adipisci, amet beatae commodi corporis
        dicta dolor dolore ea exercitationem expedita incidunt magni, mollitia obcaecati officiis quibusdam recusandae
        rem repellendus unde!
    </div>
    <div>Accusantium aliquam animi aspernatur commodi delectus dicta dolor error est exercitationem explicabo illo ipsa
        minus molestiae molestias mollitia nam nisi perspiciatis possimus, quasi quo rerum sit veritatis vitae
        voluptatibus voluptatum!
    </div>
    <div>Dolorem expedita explicabo illo incidunt maiores, sit vel? Animi assumenda at doloremque doloribus et
        excepturi, exercitationem facilis nesciunt obcaecati repudiandae. Distinctio facere fuga natus odit reiciendis
        saepe! Impedit sed, ut?
    </div>
</div>
```

```css

/*
|-----------------------------------------------------------------------------------|
|Position Property;                                                                 |
|-----------------------------------------------------------------------------------|
|** The position CSS property sets how an element is positioned in a document.      |
|** The top, right, bottom,left determine the final location of positioned elements |
|-----------------------------------------------------------------------------------|
|position: static; (by default);                                                    |
|** Positioned to the normal flow on the document;                                  |
|** top,right, bottom, left have no effect;                                         |
|-----------------------------------------------------------------------------------|
|position: relative; (top:x px;, left: x px; ,right: x px; , bottom: x px;)         |
|** The offset doesn't affect other elements positioning;                           |
|** The offset is relative to itself based on t,l,b,r values;                       |
|-----------------------------------------------------------------------------------|
|position: absolute;                                                                |
|** Remove the element from his normal flow and no space is created for it;         |
|** It's positioned  closest relative ancestor \  static will be ignored;           |
|** The final position it's determined by top,right,bottom,left                     |
|-----------------------------------------------------------------------------------|
|position: fixed; (Cool for navigation bars)                                        |
|* No space is created for the element;                                             |
|* It's positioned relative to the initial containing block;                        |
|* Its final position is determined by the values of top, right, bottom, and left.  |
|* It's gone a stay there;                                                          |
|-----------------------------------------------------------------------------------|
position: sticky; (pretty cool for navigation bars too); CHECK IT LATER;            |
|-----------------------------------------------------------------------------------|
*/

div{
    width: 100px;
    height: 100px;
    background-color: #3d405b;
    border: 2px solid black;
    margin: 10px;
    display: inline-block;
}

#middle {
    background-color: #81b29a;
}
#middle-r {
    background-color: #81b29a;
}

#middle-a {
    background-color: #81b29a;
}
#middle-f {
    background-color: #81b29a;
}
#static #middle{
    position: static;
    top: 100px;
}

#relative #middle-r{
    position: relative;
    /*Here the space is still there is not gone a be removed*/
    top: 50px;
    left: 50px;
}

#absolute #middle-a {
    position: absolute;
    top: 50px;
    left: 50px;
}

#fixed #middle-f {
    position: fixed;
}
```

<h2 id="u3">3. CSS Transitions YAY </h2>
<p>|____________________________|</p>

```html
<h1>Transitions</h1>

<div class="cirle">

</div>

<section>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</section>
```

```css

.cirle{
    width: 300px;
    height: 300px;
    background-color: magenta;
    transition: 2s;
}

.cirle:hover{
    background-color: cyan;
    /*border-radius: 50%;*/ 
}

section div{
    width: 100px;
    height: 100px;
    background-color: turquoise;
    margin: 20px 0;
    transition: margin-left 3s;

}

section:hover div{
    margin-left: 500px;
}

div:nth-of-type(1){
    transition-timing-function: ease-in;
}

div:nth-of-type(2){
    transition-timing-function: ease-out;
}

div:nth-of-type(3):hover{
transition: transform 0.6s cubic-bezier(0.32, 0, 0.67, 0);
}
```

<h2 id="u4">4. CSS Transform </h2>
<p>|____________________________|</p>

```html
<section>
    <h1>Transform me! <button>Click me h1</button></h1>
    <h1>Transform me!  <button>Click me h1</button></h1>
    <h1>Transform me! <button>Click me h1</button></h1>
    <h1>Transform me! <button>Click me h1</button></h1>
</section>

<section>
    <h1>Transform me! <button>Click me h1</button></h1>
    <h1>Transform me! <button>Click me h1</button></h1>
    <h1>Transform <button>Click me h1</button> me!</h1>
    <h1>Transform  <button>Click me h1</button> me!</h1>
</section>
```

```css
/*
|-------------------------------------------------------------------------------------------------------------|
|margin: auto; keep it center in his container;                                                               |
|-------------------------------------------------------------------------------------------------------------|
|***4.Transform(Everything we gone a do, will apply not only on parent element, but also the content)         |
|The transform CSS property lets you rotate, scale, skew, or translate an element;                            |
|It modifies the coordinate space of the CSS                                                                  |
|-------------------------------------------------------------------------------------------------------------|
|The transform-origin CSS property sets the origin for an element's transformations;                          |
|transform-origin: center;                                                                                    |
|transform-origin: top left;                                                                                  |
|-------------------------------------------------------------------------------------------------------------|
|The rotate() CSS function defines a transformation that rotates an element                                   |
|around a fixed point on the 2D plane, without deforming;                                                     |
|                                                                                                             |
|transform: rotate(0);                                                                                        |
|transform: rotate(45deg);                                                                                    |
|transform: rotate(-0.25turn);                                                                                |
|-------------------------------------------------------------------------------------------------------------|
|scale() defines a transformation that resizes an element on the 2D plane;                                    |
|transform: scale(2);                                                                                         |
|transform: scale(0.7);                                                                                       |
|transform: scale(1.3, 0.4);                                                                                  |
|-------------------------------------------------------------------------------------------------------------|
|translate() repositions an element in the horizontal and/or vertical directions;                             |
|transform:translate(x,y);                                                                                    |
|transform:translateX(x);                                                                                     |
|transform:translateY(y);                                                                                     |
|-------------------------------------------------------------------------------------------------------------|
|skew() defines a transformation that skews an element on the 2D plane;                                       |
|transform: skew(30deg);                                                                                      |
|-------------------------------------------------------------------------------------------------------------|
|Multiple function values:                                                                                    |
|transform: translateX(x) rotate(x deg) scale(2);                                                             |
|-------------------------------------------------------------------------------------------------------------|

*/

h1{
    background-color: #2a9d8f;
    border: 5px solid #264653;
    color: #eae2b7;
    padding: 0.7em;
    width: 300px;
    font-size: 1.8em;
    text-align: center;
    margin: 20px auto;
    font-weight: lighter;
}

h1:nth-of-type(2n){
    background-color: #e0c46a;
}

h1:nth-of-type(3n){
    background-color: #f4a261;
}
h1:nth-of-type(4n) {
    background-color: #e76f51;
}

/*First section first h1*/
section:first-of-type h1:nth-of-type(1){
    transform-origin: center;
    transform: rotate(45deg);
}

/*First section second h1*/
section:first-of-type h1:nth-of-type(2){
    transform: scale(0.5);
}

/*First section 3*h1*/
section:first-of-type h1:nth-of-type(3){
    transform: translatex(300px);
}
/*First section 4*h1*/
section:first-of-type h1:nth-of-type(4){
transform: translate(-100px, 50px);
}

/*Second section first h1*/
section:nth-of-type(2) h1:nth-of-type(1){
transform: skew(30deg);
}

/*Second section second h1*/
section:nth-of-type(2) h1:nth-of-type(2){
transform: skew(10deg,30deg);
}
/*Second section 3*h1*/
section:nth-of-type(2) h1:nth-of-type(3){
transform: rotate(20deg) scale(1.2) ;
}

/*Second section 4*h1*/
section:nth-of-type(2) h1:nth-of-type(4){
transform: translateX(-400px) rotate(180deg) scaleY(1.5);
}

/*Second Section all content*/
section:nth-of-type(2){
    transform: translate(300px) scale(0.6) rotate(45deg);
}
```

<h2 id="u5">5. Practice / Fancy Button Hover Effect</h2>
<p>|____________________________|</p>

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Fancy Button</title>
    <link rel="stylesheet" href="m9_fancyButton.css">
    <link href="https://fonts.gooogleapis.com/css2?family=Roboto+Mono:wght@300&display=swap">
</head>
<body>
<button>Hover ME</button>
</body>
</html>
```

```css
/*
/* offset-x | offset-y | blur-radius | spread-radius | color
box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
*/

body{
    margin: auto;
    font-family: 'Roboto Light', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #151b29;
}

button{
    background: none;
    color: #ffa260;
    border: 2px solid;
    padding: 1em 2em;
    font-size: 1em;
}

button:hover{
    border-color: #f1ff5c;
    color: white;
    box-shadow: 0 0.5em 0.5em -0.4em  #f1ff5c;
    transform: translateY(-0.25em);
    transition: all 0.25s;
    cursor: pointer;
}
```

<h2 id="u6">6. Background</h2>
<p>|____________________________|</p>

```html
<section>
    <h1>Heading</h1>
</section>
```

```css
section{
    width: 80%;
    height: 800px;
    margin: auto;
    
    /*Background Shorthand */
    background: center/cover url("https://images.unsplash.com/photo-1519865885898-a54a6f2c7eea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=758&q=80") no-repeat;
}

h1{
    font-size: 100px;
    color: white;
}
```

```css
background-size: cover;
background-image: url("https://images.unsplash.com/photo-1519865885898-a54a6f2c7eea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=758&q=80");
```
<h2 id="u7">6. Google Fonts</h2>
<p>|____________________________|</p>

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Google Fonts</title>
    <link rel="stylesheet" href="m9_GoogleFonts.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Raleway:wght@100&display=swap" rel="stylesheet">

</head>
<body>
<main>
<h1>Google Fonts</h1>
<h2>Subheading goes here</h2>

<h3>Chicken Nugget Goes Here</h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid aperiam aspernatur deleniti deserunt dolore doloremque
    dolores doloribus dolorum earum eveniet impedit maxime nesciunt nobis pariatur praesentium, quasi, quos temporibus voluptatem.</p>
</main>

</body>
</html>
```

```css
body{
    /*Referring to GoogleFont */
    font-family: 'Open Sans', sans-serif;

}

main{
    width: 60%;
    margin: 0 auto;
}

h1{
    font-size: 2rem;
    margin-bottom: 0;
}

h1+h2{
    margin-top: 10px;
}


h1,h2,h3{
    /*Referring to GoogleFont */
    font-family: 'Raleway', sans-serif;
}
```


<h2 id="u8">8. PhotoBlog</h2>
<p>|____________________________|</p>

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Photo Blog</title>
    <link rel="stylesheet" href="m9_PhotoBlog.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Smooch&display=swap" rel="stylesheet">
</head>
<body>
<!--PUT YOUR NAME IN HERE-->
<nav>TONY/DN</nav>

<img src="https://images.unsplash.com/photo-1652203106991-f21f915237b9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmxhY2slMjZ3aGl0ZSUyMHBob3RvZ3JhcGh5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60" alt="IMG1">
<img src="https://images.unsplash.com/photo-1603512284607-faab31e24606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YmxhY2slMjZ3aGl0ZSUyMHBob3RvZ3JhcGh5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60" alt="IMG2">
<img src="https://images.unsplash.com/photo-1602857656420-967326d63423?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGJsYWNrJTI2d2hpdGUlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="IMG2">


<img src="https://images.unsplash.com/photo-1527615731013-10fdd6d3c532?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fGJsYWNrJTI2d2hpdGUlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="ee">
<img src="https://images.unsplash.com/photo-1633228059898-d35c4f608bbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGJsYWNrJTI2d2hpdGUlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="ee2">
<img src="https://images.unsplash.com/photo-1615999452307-8babf494d226?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGJsYWNrJTI2d2hpdGUlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt="ee3">
</body>
</html>
```

```css
/*calc() function css*/
img{
    width: 30%;
    /*margin:1.6666%*/
    margin: calc(10%/6);
}

nav{
    text-transform: uppercase;
    border-bottom: 2px solid #f1f1f1;
    width: 30%;
    margin-left: calc(10%/6);
    padding: 1.2em 0;
    /*Google Font Family*/
    font-family: 'Smooch', cursive;
    font-size: 1.5em;
}
```

