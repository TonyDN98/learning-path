<h1>M4.HTML Semantics Notes MD</h1>

<h2>_I. Block Elements vs Inline Elements_</h2>

![](https://pbs.twimg.com/media/EdOQGgTXgAE5QdB.jpg:large)
<pre>
INLINE ELEMENTS:
Inline elements fit in alongside other elements;
Block Level elements take up a whole "block" of space.
</pre>

```html
<!-- Immediately after the first <a> which is a inline element, <p> tag takes his own line -->
<a href="https://google.com">FirstLink</a>
<p>SomeText</p> 
<a href="https://google.com">SecondLink</a>

<!--<p> is gonna take his own whole line</p>-->
```

<h3>_div element_</h3>
```html
<div></div> is a way of grouping content together; Later on we can style this whole group with  CSS;
The <div> HTML element is the generic container for flow content. It has no effect on the content or
layout until styled in some way using CSS (e.g. styling is directly applied to it, or some kind of
layout model like Flexbox is applied to its parent element).
```
```html
<div class="warning">
    <img src="/media/examples/leopard.jpg"
         alt="An intimidating leopard.">
    <p>Beware of the leopard</p>
</div>
```
<h3>_span element_</h3>
```html
<span></span>, like div is a container but this time <span> is a inline elmenet;
The <span> HTML element is a generic inline container for phrasing content, which does not inherently represent anything.
It can be used to group elements for styling purposes (using the class or id attributes), or because they share attribute values, such as lang. 
It should be used only when no other semantic element is appropriate. <span> is very much like a <div> element, but <div> is a block-level element whereas a <span> is an inline element.
```

```html
<p>Add the <span class="ingredient">basil</span>, <span class="ingredient">pine nuts</span> and <span class="ingredient">garlic</span> to a blender and blend into a paste.</p>

<p>Gradually add the <span class="ingredient">olive oil</span> while running the blender slowly.</p>
```

<h3>_br: The Like Break Element_</h3>
```html
The <br> HTML element produces a line break in text (carriage-return). 
It is useful for writing a poem or an address, 
where the division of lines is significant.

```
```html
<p> O’er all the hilltops<br>
    Is quiet now,<br>
    In all the treetops<br>
    Hearest thou<br>
    Hardly a breath;<br>
    The birds are asleep in the trees:<br>
    Wait, soon like these<br>
    Thou too shalt rest.
</p>
```

<h3>sup/sub The Superscript/SubScript</h3>
```html
<!--
<sup> SuperScript / <sub> SubScript
The <sup> or <sub> HTML element specifies inline text which is to be displayed as superscript/subscript for solely typographical reasons.
Superscripts are usually rendered with a raised baseline using smaller text.
-->
```
```html
<p>The <b>Pythagorean theorem</b> is often expressed as the following equation:</p>
<span>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></span>
<br>
<span>a<sub>2</sub> + b<sub>2</sub> = c<sub>2</sub></span>
```

<hr><hr>

<h2>_II. Entity Codes_</h2>
```html
<!--
Entity Codes
Special codes or specific sequences that we can use that will refer to specific characters;
Starts with ampersand(&) ends with semicolon (;)
Used to display reserved characters;
-->
```
```html
<h2>1 &lt; &gt; 6</h2>
<p> Different kind of character: &amp; &therefore; &times; &equals; &lang; &hearts; &middot; &ApplyFunction;</p>
```

<hr>

<h3>_SnowMan Practice Entity Code;_</h3>
![](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/m4_snowman.png?raw=true)

```html
<h1>&#9731;Snowman Production<sup> &reg;</sup></h1>
```

<hr>

<h3>_Semnatic MarkUP_</h3>
<pre>
Semantic - relating to meaning;
<hr>
"What purpose or role does that HTML element have?"
Header, footer, navs, article, main, they all behave just like divs except they have some meaning;
And the question is now why? Why is this matter?
Making your content more applicable for other applications or search engines;
Accessibility and making your code more accessible for other ppl;
<hr>
Makes your markup or your code more navigable for yourself and other developers;
Adding meaning into our markup is ht idea behind writing semantic markup;

</pre>

<h2>Playing with semantics</h2>

```html
Instead of DIVS, use more specific elements like:
<section></section>
<article></article>
<nav></nav>
<main></main>
<header></header>
<footer></footer>
<aside></aside>
<summary></summary>
<details></details>
```

<h3>_&lt;main&gt;&lt;/main&gt;_</h3>
```html
The <main> HTML element represents the dominant content of the <body> of a document. 
The main content area consists of content that is directly related to or expands upon the central 
topic of a document, or the central functionality of an application.
```
```html
<header>Gecko facts</header>

<main>
    <p>Geckos are a group of usually small, usually nocturnal lizards. They are found on every continent except Australia.</p>
 
    <p>Many species of gecko have adhesive toe pads which enable them to climb walls and even windows.</p>
</main>

```
![mainoutput](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/main%20output%20dmn.png?raw=true)


<h3> &lt;nav&gt;: The Navigation Section element</h3>

```html
The <nav> HTML element represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. 
Common examples of navigation sections are menus, tables of contents, and indexes.
```
```html
<nav class="crumbs">
    <ol>
        <li class="crumb"><a href="#">Bikes</a></li>
        <li class="crumb"><a href="#">BMX</a></li>
        <li class="crumb">Jump Bike 3000</li>
    </ol>
</nav>

<h1>Jump Bike 3000</h1>
<p>This BMX bike is a solid step into the pro world. It looks as legit as it rides and is built to polish your skills.</p>

```
![nav out](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/navout.png?raw=true)

<h3>_&lt;section&gt;: The Generic Section element_</h3>
```html
The <section> HTML element represents a generic standalone section of a document, 
which doesn't have a more specific semantic element to represent it. 
Sections should always have a heading, with very few exceptions.

As mentioned above, <section> is a generic sectioning element,
and should only be used if there isn't a more specific element to represent it. 
As an example, a navigation menu should be wrapped in a <nav> element,
but a list of search results or a map display and its controls don't have specific elements, 
and could be put inside a <section>.
```

```html
<h1>Choosing an Apple</h1>
<section>
    <h2>Introduction</h2>
    <p>This document provides a guide to help with the important task of choosing the correct Apple.</p>
</section>

<section>
    <h2>Criteria</h2>
    <p>There are many different criteria to be considered when choosing an Apple — size, color, firmness, sweetness, tartness...</p>
</section>

```

![sectionout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/sectionout.png?raw=true)


<h3>&lt;article&gt;: The Article Contents element</h3>
```html
The <article> HTML element represents a self-contained composition in a document,
page, application, or site, which is intended to be independently
distributable or reusable (e.g., in syndication). 
Examples include: a forum post, a magazine or newspaper article, 
or a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, 
or any other independent item of content.
```

```html
<article class="forecast">
    <h1>Weather forecast for Seattle</h1>
    <article class="day-forecast">
        <h2>03 March 2018</h2>
        <p>Rain.</p>
    </article>
    <article class="day-forecast">
        <h2>04 March 2018</h2>
        <p>Periods of rain.</p>
    </article>
    <article class="day-forecast">
        <h2>05 March 2018</h2>
        <p>Heavy rain.</p>
    </article>
</article>
```
![articleout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/articleout.png?raw=true)

<h3>&lt;aside&gt;: The Aside element</h3>

```html
The <aside> HTML element represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.
```

```html
<p>Salamanders are a group of amphibians with a lizard-like appearance, including short legs and a tail in both larval and adult forms.</p>

<aside>
    <p>The Rough-skinned Newt defends itself with a deadly neurotoxin.</p>
</aside>

<p>Several species of salamander inhabit the temperate rainforest of the Pacific Northwest, including the Ensatina, the Northwestern Salamander and the Rough-skinned Newt. Most salamanders are nocturnal, and hunt for insects, worms and other small creatures.</p>
```

![asideout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/asideout.png?raw=true)


<h3>&lt;header&gt;</h3>

```html
The <header> HTML element represents introductory content, 
typically a group of introductory or navigational aids. 
It may contain some heading elements but also a logo, a search 
form, an author name, and other elements.
```

```html
<header class="page-header">
    <h1>Cute Puppies Express!</h1>
</header>

<main>
    <p>I love beagles <em>so</em> much! Like, really, a lot. They’re adorable and their ears are so, so snuggly soft!</p>
</main>
```


![headerout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/headerout.png?raw=true)


<h3>&lt;footer&gt;</h3>

```html
The <footer> HTML element represents a footer for its nearest ancestor sectioning content or 
sectioning root element. A <footer> typically contains information about the author of the section, 
copyright data or links to related documents.
```


```html
<article>
    <h1>How to be a wizard</h1>
    <ol>
        <li>Grow a long, majestic beard.</li>
        <li>Wear a tall, pointed hat.</li>
        <li>Have I mentioned the beard?</li>
    </ol>
    <footer>
        <p>© 2018 Gandalf</p>
    </footer>
</article>
```

![footerout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/footerout.png?raw=true)




<h3>&lt;time&gt;: The (Date) Time element</h3>
```html
The <time> HTML element represents a specific period in time. It may include the datetime attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

It may represent one of the following:
```

```html
<p>The Cure will be celebrating their 40th anniversary on <time datetime="2018-07-07">July 7</time> in London's Hyde Park.</p>

<p>The concert starts at <time datetime="20:00">20:00</time> and you'll be able to enjoy the band for at least <time datetime="PT2H30M">2h 30m</time>.</p>
```


![timeout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/timeout.png?raw=true
)

<h3>&lt;figure&gt;: The Figure with Optional Caption element</h3>

```html
The <figure> HTML element represents self-contained content, potentially with an optional caption, which is specified using the <figcaption> element. The figure, its caption, and its contents are referenced as a single unit.
```

```html
<figure>
    <img src="/media/cc0-images/elephant-660-480.jpg"
         alt="Elephant at sunset">
    <figcaption>An elephant at sunset</figcaption>
</figure>
```

![figureout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/figureout.png?raw=true)


<h3>&lt;data&gt;: The Data element</h3>

```html
The <data> HTML element links a given piece of content with a machine-readable translation. If the content is time- or date-related, the <time> element must be used.
```

```html
<p>New Products:</p>
<ul>
    <li><data value="398">Mini Ketchup</data></li>
    <li><data value="399">Jumbo Ketchup</data></li>
    <li><data value="400">Mega Jumbo Ketchup</data></li>
</ul>

```

![dataout](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/dataout.png?raw=true)




