<h1>M3. Essentials Notes MD</h1>

<h2>_Our First Page_</h2>

<pre>HTML IS A MARKUP PROGRAMMING LANGUAGE;</pre>
<h3>_Anatomy of an HTML element_</h3>
![Anatomy of html elements](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started/grumpy-cat-small.png)

```html
<p>content</p> element - represents a paragraph of text; </p>
<h1>content</h1> element - represents the main header on a page; </p>
<img src="M3_Topics/TODO.html" alt="alternativ text"> element - embeds an image; </p>
<form>content</form> element -represent a form; </p>
```


```html
The <p> HTML element represents a paragraph. 
Paragraphs are usually represented in visual media as blocks of text 
separated from adjacent blocks by blank lines and/or first-line indentation, 
but HTML paragraphs can be any structural grouping of related content, 
such as images or form fields.</p>
</pre>

<pre>
<p>Paragraphs are block-level elements, and notably will automatically close
if another block-level element is parsed before the closing </p> tag.
</pre>
```

<h3>HTML SKELETON</h3>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML SKELETON</title>
</head>
<body>
<!-- Content goes here -->
</body>
</html>
```

```html
<!DOCTYPE html>
<!--It's a flag for our browser that indicates that we are using HTML5 -->
```

```html
<html lang="en"></html>

<!--
HTML element represents the root (top-level element) of an HTML document, 
so it is also referred to as the root element.
All other elements must be descendants of this element.
Permitted content:
One <head> element, followed by one <body> element.
-->

```

```html
<head>
    <title>Title</title>
    <meta charset="UTF-8">
</head>
<!--
The <head> HTML element contains machine-readable information (metadata) 
about the document, like its title, scripts, and style sheets.
Note: <head> primarily holds information for machine processing, 
not human-readability. For human-visible information, like top-level 
headings and listed authors, see the <header> element.
-->

```

```html

<body>
<p>A paragraph</p>
<img src="M3_Topics/TODO.html" alt="someWhere">
</body>
<!--
The <body> HTML element represents the content of an HTML document. 
There can be only one <body> element in a document.
-->

```

<h3>_List Elements_<h3>
    
```html
<!-- Zero or more <li>, <script> and <template> elements. -->
<p>Ordered List</p>
<ol>
    <li>Item1</li>
    <li>Item2</li>
    <li>Item3</li>
    <li>Item4</li>
    <li>OrderList2<ol>
        <li>OrderList2_Item1</li>
        <li>OrderList2_Item2</li>
        <li>OrderList2_Item3</li>
    </ol></li>
<!--The same can go for Unordered lists.-->
    
```

````html
<!-- Zero or more <li>, <script> and <template> elements. -->
<p>Unordered List</p>
<ul>
    <li>Item1</li>
    <li>Item2</li>
    <li>Item3</li>
    <li>Item4</li>
    <li>unorderList2 <ul>
        <li>unorderList2_Item1</li>
        <li>UnorderList2_Item2</li>
        <li>UnorderList2_Item3</li>
        <li><ul>
            <li>UnorderList3_Item1</li>
            <li>UnorderList3_Item2</li>
        </ul></li>
    </ul></li>
</ul>
<!--The same can go for Unordered lists.-->
    
```

<h3>Anchors</h3>
    
```html
 <!--
Links/Anchors;
It's a inline element != from block elements;

It's a must to contain the attribute href=""
href ->Stands for HyperText Reference
 -->
```

```html

    <a href="google.com">This is an Incorrect link!</a>
    <!-- 
    <a href="google.com">This is a link!</a>
    Cannot GET /google.com -->

    <a href="https://google.com">This is Correct a link!!</a>
<!-- If we want to link another website, it's a must to contain
    the https:// request otherwise, our URL will search for the current directory.
-->
```
```html
 <!--
 Let's say we want to link another .html document that we have created. -->

    <a href="./M3_Practice/m3_Practice1_Pangolin.html">
        Link to m3_Practice1_Pangolin.html</a

```

<h3>Images</h3>
    
```html
    <!--
Here, be careful <img> doesn't have a closing tag and no content in between.
<img> Have 2 Attributes:
src="" -> Stands for Image Source
alt="" -> Stands for Alternative Text in case Image can't be displayed.
-->
<a href="https://www.google.ro/search?source=hp&ei=kfotW5yKA8v76AT23aPoDg&btnG=C%C4%83uta%C8%9Bi&q=chekine+image&oq=best+python+books+for+beginners+&gs_l=psy-ab.3.1.0i203k1l5j0i22i30k1l5.825.4938.0.6777.24.20.0.0.0.0.271.2322.0j11j3.14.0..3..0...1.1.64.psy-ab..10.14.2320.0..0j35i39k1j0i131k1j0i67k1.0.8troR154Fqw" >
    <img src="M3_Images/chiken.jpg" alt = "chicken image"></a>

```

```html
<a
href="https://www.google.ro/search?q=wolf+image&source=lmns&bih=979&biw=1920&hl=ro&sa=X&ved=2ahUKEwjQ7vS8kIbyAhX5wQIHHUf0Ao8Q_AUoAHoECAEQAA">
<img src="https://store-images.s-microsoft.com/image/apps.23285.13992228047138758.dbd3fc41-b78f-4b6a-848d-7815f0fa905c.76ed81a7-e9d3-40be-8b5e-f04319de590f?mode=scale&q=90&h=200&w=200&background=%230078D7"alt="Image wolf from Internet"
/>
</a>
```






