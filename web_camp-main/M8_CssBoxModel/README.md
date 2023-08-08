
<h1>Module 8. Css BoxModel</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>


[m8_cssBoxModel.html HTML File](m8_cssBoxModel.html)<br>
[m8_cssBoxModelStyle.css CSS File](m8_cssBoxModelStyle.css)

<p>|____________________________________|</p>


<h2>II. Practice Content</h2>

<p>|____________________________________|</p>



<p>|____________________________________|</p>



<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>

<p id="goUP"></p>
<ul>
    <li><a href="">1. BoxModel Width & Height</a></li>
    <li><a href="">2. Border \ Border-Radius</a></li>
    <li><a href="">3. Padding</a></li>
    <li><a href="">4. Margin </a></li>
    <li><a href="">5. Display Property IMPORTANT </a></li>
    <li><a href="">6. CSS UNITS IMPORTANT</a></li>
    <li><a href="">7. CSS UNITS: ems </a></li>
    <li><a href="">8. CSS UNITS: rems </a></li>
</ul>



<h2>1. Width & Height</h2>
<p>|____________________________|</p>

```css

/*
+-------------------------------------------------------------------------+|
| WIDTH & HEIGHT                                                           |
| Width (LEFT / RIGHT)                                                     |
| Height (UP / DOWN)                                                       |
|+-------------------------------------------------------------------------+
```

```html
<div class = "divclass"></div>
<div class = "divclass"></div>

```

```css
.divclass {
    width: 200px;
    height: 200px;
}
```

<h2>2. Border / Border-Radius</h2>
<p>|__________________________________|</p>

```css
/*
+--------------------------------------------------------------------------------------------------+|
|BORDER                                                                                             |
+--------------------------------------------------------------------------------------------------+|
|border-width >- control thickness of the border                                                    |
|border-color >- color of border                                                                    |
|border-style >- style - dashed, solid, etc;                                                        |
+--------------------------------------------------------------------------------------------------+|
|Shorthand Border:                                                                                  |
|border: border-width border-color border-style                                                     |
+--------------------------------------------------------------------------------------------------+|
|border-radius(rounded corners): use relative values, px it's not a good idea for this situation;   |
+--------------------------------------------------------------------------------------------------+|

 */
```

```html
<div id="three">
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
        Accusantium eum eveniet, illo iure laudantium magnam nesciunt non quia voluptas?
        A consequuntur debitis distinctio eum ipsum laboriosam mollitia odit velit voluptatem.
    </p>
</div>
```

```css
#three {
    background: #6d6875;
    /*width | style | color*/
    border: 2px dashed red ;
    border-radius: 15%;
}
```

<h2>3. Padding</h2>
<p>|_________________|</p>

```css
/*
+--------------------------------------------------------------------------------------------------+|
|PADDING                                                                                            |
+--------------------------------------------------------------------------------------------------+|
|Padding is the space between the content and thr border;                                           |
+--------------------------------------------------------------------------------------------------+|
|
border
|---------------------------------------|border
|              PADDING                  |
|        -------------------            |
|PADDING|     CONTENT      |  PADDING   |
|       |     BOX          |            |
|       ---------------------           |
|             PADDING|                  |
|---------------------------------------|
border
|
+--------------------------------------------------------------------------------------------------+|
|padding-left                                                                                       |
|padding-right                                                                                      |
|padding-bottom                                                                                     |
|padding-top                                                                                        |
+--------------------------------------------------------------------------------------------------+|
|Shorthand Padding:                                                                                 |
|padding: 10px; All 4 sides                                                                         |
+--------------------------------------------------------------------------------------------------+|
|Vertical | Horizontal                                                                              |
|padding 5px 10px;                                                                                  |
+--------------------------------------------------------------------------------------------------+|
|Top | Right | Bottom | Left | around the clock                                                     |
|padding: 1px 2px 3px 4px;                                                                          |
+--------------------------------------------------------------------------------------------------+|
 */
```


```html
<div>
    <button>Click me</button>
</div>
```

```css
div button {
    /*padding: 20px;*/
    /*padding: 10px 20px;*/
    padding: 10px 20px 30px 40px;
}
```

<h2>3. Margin</h2>
<p>|_________________|</p>

```css
/*
+---------------------------------------------------------------------------------------------------------------------------+|
|Margin                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------+|
|Margin is the space between other elements;                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------+|
|                                                                                                                            |
|                ELEMENT 1                                                   ELEMENT 2                                       |
|-------------------------------------------------------| |-------------------------------------------------------|          |
|                   MARGIN                              | |                   MARGIN                              |          |
|      |----------border------------------------| MARGIN| |      |----------border------------------------| MARGIN|          |
|MARGIN|              PADDING                   |       | |MARGIN|              PADDING                   |       |          |
|      |        -------------------             |       | |      |        -------------------             |       |          |
|      |PADDING|     CONTENT      |  PADDING    |       | |      |PADDING|     CONTENT      |  PADDING    |       |          |
|      |       |     BOX          |             |       | |      |       |     BOX          |             |       |          |
|      |       ---------------------            |       | |      |       ---------------------            |       |          |
|      |             PADDING|                   |       | |      |             PADDING|                   |       |          |
|      |---------------border-------------------|       | |      |---------------border-------------------|       |          |
|                   MARGIN                              | |                   MARGIN                              |          |
|-------------------------------------------------------| |-------------------------------------------------------|          |
|                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------+|
|margin-left;                                                                                                                |
|margin-right;                                                                                                               |
|margin-bottom;                                                                                                              |
|margin-top;                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------+|
|Shorthand Margin:                                                                                                           |
|margin: 10px; all 4 sides                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------+|
|Vertical | Horizontal                                                                                                       |
|margin: 5px 10px;                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------+|
|Top | Right | Bottom | Left | around the clock                                                                              |
|margin: 1px 2px 3px 4px;                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------+|
*/
```


```css
/*It's a good idea to take your margin off for body, to get that extra space;*/
body{
margin:0px;
}
```

<h2>4. display</h2>
<p>|____________________________|</p>

```css
/*
+---------------------------------------------------------------------------------------------------------------------------+|
|display:none >- hide an element;                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------+|
|display:inline                                                                                                              |
|    >- WIDTH & HEIGHT are ignored. Margin & Padding push elements away horizontally but not vertically;                     |                
+---------------------------------------------------------------------------------------------------------------------------+|
|display: block                                                                                                              |
|   >- WIDTH & HEIGHT , Margin & Padding are respected;                                                                      |
+---------------------------------------------------------------------------------------------------------------------------+|
|display: inline-block                                                                                                       |
|    >- Behave like inline elements except  WIDTH & HEIGHT , Margin & Padding are respected;                                 |
+---------------------------------------------------------------------------------------------------------------------------+|

*/
```

```html
<div class="divdisplay"></div>
<div class="divdisplay"></div>
<div class="divdisplay"></div>

<div class="displaynone">
    <p>This will disappear;</p>
</div>
```

```css
.divdisplay{
    height: 200px;
    width: 200px;
    background-color: olive;
    border: 5px solid black;
    display: inline-block;
    margin: 10px;
    padding: 10px;
}

.displaynone{
    display: none;
}
```


<h2>6. Absolute & Relative Units</h2>
<p>|____________________________|</p>

```css
/*
+--------------------------------------------------------------------------------------------------------------------------------------+|
| Absolute Units (px,mm,cm) (this sized are fixed length)                                                                               |
| Units that are absolute are the same size regardless of the parent element or windows size;                                           |
+--------------------------------------------------------------------------------------------------------------------------------------+|
|Relative Units (%, em,rem)                                                                                                             |
|This units are useful for styling responsive sites because the scale relative with parent or windows size(depending on the unit);      |
|
|% >- Relative to the parent element;                                                                                                   |
|em >- Relative to the font size of the element                                                                                         |
|rem >- Relative to the font size of the root element;                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------+|
*/
```
