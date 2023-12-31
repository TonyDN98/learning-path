# HTML Fundamentals

[HTML/CSS/JS Diffs](https://brytdesigns.com/html-css-javascript-whats-the-difference)  
[MDN element references](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)  
[devdocs REF](https://devdocs.io/)

## HTML
*`HTML` (`HyperText Markup Language`) defines the structure and content of webpages. We use HTML elements to create all of the paragraphs, headings, lists, images, and links that make up a typical webpage. In this lesson, we will explore how HTML elements work.*

### Main differences
![differences](https://brytdesigns.com/_next/image?url=https%3A%2F%2Fadmin.brytdesigns.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fhtml_css_javascript_infographic-1024x614.png&w=1080&q=75)


### Elements and tags
![wrap elements](./images/html-element.png)

**You can think of elements as containers for content.**  
*Almost all elements on an HTML page are just pieces of content wrapped in opening and closing HTML tags.*

```html
<p> Content here </p>
```

## [HTML Boilerplate](https://www.theodinproject.com/lessons/foundations-html-boilerplate)

*All `HTML` documents have the same basic structure or boilerplate that needs to be in place before anything useful can be done. In this lesson, we will explore the different parts of this boilerplate and see how it all fits together.*

### Creating an HTML file

```bash
mkdir html-boilerplate
touch index.html
```

*We should always name the `HTML` file that will contain the homepage of our websites index.html. This is because web servers will by default look for an `index.html` page when users land on our websites - and not having one will cause big problems.*

### The DOCTYPE

*Every HTML page starts with a doctype declaration. The doctype’s purpose is to tell the browser what version of HTML it should use to render the document. The latest version of HTML is HTML5, and the doctype for that version is simply `<!DOCTYPE html>`*

```html
<!DOCTYPE html>
```

### HTML element
*After we declare the doctype, we need to provide an `<html`> element. This is what’s known as the root element of the document, meaning that every other element in the document will be a descendant of it.*

```html
<!DOCTYPE html>
<html lang="en">

</html>
```

#### What is the lang attribute?

*`lang` specifies the language of the text content in that element. This attribute is primarily used for improving accessibility of the webpage.*

### Head element
*The `<head>` element is where we put important `meta-information` about our webpages, and stuff required for our webpages to render correctly in the browser.*

#### The charset meta element
```html
<meta charset="utf-8">
```
*We should always have the meta tag for the charset encoding of the webpage in the head element: `<meta charset="utf-8">`*

*Setting the encoding is very important because it ensures that the webpage will display special symbols and characters from different languages correctly in the browser.*

#### Title element

```html
<title> My learning page  </title>
```

*The title element is used to give webpages a human-readable title which is displayed in our webpage’s browser tab.*

### Body element

*The final element needed to complete the HTML boilerplate is the `<body>` element. This is where all the content that will be displayed to users will go - the text, images, lists, links, and so on*

### Complete the boilerplate

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My First Webpage</title>
  </head>

  <body>
  </body>
</html>
```

### Open in Browser the document

```bash
google-chrome index.html
```

## [Working with Text](https://www.theodinproject.com/lessons/foundations-working-with-text)

*Most content on the web is `text-based`, so you will find yourself needing to work with HTML text elements quite a bit.*

### Paragraphs

```html
<html>
  <head>
  </head>
  <body>
    Lorem ipsum dolor sit ames, conceptsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
  </body>
 </html>
```

*When the browser encounters new lines like this in your HTML, it will compress them down into one single space.*

```html
<html>
  <head>
  </head>
  <body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua.</p>

    <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat.</p>
  </body>   
 </html>
```

### Headings

*Headings are different from other HTML text elements: they are displayed larger and bolder than other text to signify that they are headings.*

*There are 6 different levels of headings starting from `<h1>` to `<h6>`. The number within a heading tag represents that heading’s level. The largest and most important heading is h1, while h6 is the tiniest heading at the lowest level*

```html
<html>
  <head>
  </head>
  <body>
    <h1>This is a heading 1</h1>
    <h2>This is a heading 2</h2>
    <h3>This is a heading 3</h3>
    <h4>This is a heading 4</h4>
    <h5>This is a heading 5</h5>
    <h6>This is a heading 6</h6>
  </body>
 </html>
```

*Using the ``correct`` level of heading is important as levels provide a hierarchy to the content. An h1 heading should always be used for the heading of the overall page, and the lower level headings should be used as the headings for content in smaller sections of the page.*

### Strong & Em elements

```html
<!-- SEMANTIC TAGS -->
<strong>STRONG</strong>
<em>empathize</em>
<b>bold text</b>
<i>italic text</i>
```

## [Lists](https://www.theodinproject.com/lessons/foundations-lists)
### Unordered lists

*Unordered lists are created using the `<ul> `element, and each item within the list is created using the list item element `<li>`.*

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```


### Ordered lists

*Ordered lists are created using the `<ol>` element. Each individual item in them is again created using the list item element `<li>`.*

```html
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
```

#### Assignment

*To get some practice using lists, create a new HTML document and create the following lists:*

* An unordered shopping list of your favorite foods  
* An ordered list of todo’s you need to get done today  
* An unordered list of places you’d like to visit someday  
* An ordered list of your all time top 5 favorite video games or movies

```html
<ul>
  <li>Orez cu pui</li>
  <li>Orzo cu pui</li>
  <li>Tocanita</li>
  <li>Ciorba de pui ala greek</li>
  <li>Mazare cu pui</li>
</ul>
```

```html
<ol>
  <li>Work</li>
  <li>Gift</li>
  <li>Nothing</li>
</ol>
```

```html
<ul>
  <li>Egypt</li>
  <li>Bali</li>
</ul>
```

```html
<ol>
  <li>COD</li>
  <li>LOL</li>
  <li>Warframe</li>
</ol>
```
### [Links and Images](https://www.theodinproject.com/lessons/foundations-links-and-images)

### Anchor elements

*To create a link in `HTML`, we use the anchor element. An anchor element is defined by wrapping the text or another HTML element we want to be a link with an `<a>` tag.*

```html
<a href="https://www.theodinproject.com/about">click me</a>
```

*While `href` specifies the `destination` link, `target` specifies where the linked resource will be opened. If it is not present, then, by default, it will take on the `_self` value which opens the link in the current tab. To open the link in a new tab or window (depends on browser settings) you can set it to `_blank`*

```html
<a href="https://www.theodinproject.com/about" target="_blank" rel="noopener noreferrer">click me</a>
```

### Absolute and relative links

#### Absolute links

*A typical absolute link will be made up of the following parts: `protocol://domain/path`. An absolute link will always contain the protocol and domain of the destination.*

```html
https://www.theodinproject.com/about
```

#### Relative links

*Links to other pages within our own website are called relative links. Relative links do not include the domain name, since it is another page on the same site, it assumes the domain name will be the same as the page we created the link on.*

*Relative links only include the file path to the other page, relative to the page you are creating the link on. This is quite abstract, let’s see this in action using an example.*

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Odin Links and Images</title>
  </head>

  <body>
    <h1>About Page</h1>
  </body>
</html>
```

```html
<body>
  <h1>Homepage</h1>
	<a href="https://www.theodinproject.com/about">click me</a>

	<a href="about.html">About</a>
</body>
```

*This works because the index and about page are in the same directory. That means we can simply use its name (`about.html`) as the link’s href value.*

```html
<body>
  <h1>Homepage</h1>
  <a href="./pages/about.html">About</a>
</body>
```

* Prepending `./` before the link will in most cases prevent such issues. By adding `./` you are specifying to your code that it should start looking for the file/directory relative to the current directory.*

### A metaphor !!!!

Absolute and relative links are a tricky concept to build a good mental model of, a metaphor may help:

Think of your `domain name (town.com)` as a town, the directory in which your website is located `(/museum) as a museum`, and each page on your website as a `room` in the museum `(/museum/movie_room.html and /museum/shops/coffee_shop.html)`. Relative links like ./shops/coffee_shop.html are directions from the current room (the museum movie room /museum/movie_room.html) to another room (the museum shop). Absolute links, on the other hand, are full directions including the protocol (https), domain name (town.com) and the path from that domain name (/museum/shops/coffee_shop.html): `https://town.com/museum/shops/coffee_shop.html.`


## Images

*To display an image in HTML we use the `<img>` element. Unlike the other elements we have encountered, the `<img>` element is self-closing. Empty, self-closing HTML elements do not need a closing tag.*

```html
 <img src="https://www.theodinproject.com/mstile-310x310.png">
```

#### Assignment
*Create a new directory named images within the odin-links-and-images project.*

*Next, download this image and move it into the images directory we just created.*

*Rename the image to dog.jpg*

```html
<body>
  <h1>Homepage</h1>
	<a href="https://www.theodinproject.com/about">click me</a>

	<a href="./pages/about.html">About</a>

	<img src="./images/dog.jpg">
</body>
```

### Parent directories

*To go to the parent directory we need to use two dots in the relative filepath like this: `../ `*

```html
<img src="../images/dog.jpg">
```

### Alt attribute
*The `alt` attribute is used to describe an image. It will be used in place of the image if it cannot be loaded. It is also used with screen readers to describe what the image is to visually impaired users.*

```html
 <img src="https://www.theodinproject.com/mstile-310x310.png" alt="The Odin Project Logo">
```

### [Diffs between jpg, gif, png, svg](https://internetingishard.netlify.app/html-and-css/links-and-images/#image-formats)

![dif-img](https://internetingishard.netlify.app/image-formats-62b23d.df203a3f.png)

### jpg images

*``JPG`` images are designed for handling large color palettes without exorbitantly increasing file size. This makes them great for photos and images with lots of gradients in them.*

### gif images

*``GIFs`` are the go-to option for simple animations, but the trade off is that they’re somewhat limited in terms of color palette—never use them for photos. Transparent pixels are a binary option for GIFs, meaning you can’t have semi-opaque pixels. This can make it difficult to get high levels of detail on a transparent background. For this reason, it’s usually`` better to use PNG images if you don’t need animation``.*

### png images
*``PNGs`` are great for anything that’s not a photo or animated. For photos, a PNG file of the same quality (as perceived the human eye) would generally be bigger than an equivalent JPG file. However, they do deal with opacity just fine, and    they don’t have color palette limitations. This makes them an excellent fit for ``icons, technical diagrams, logos``, etc.*

### svg images
*Unlike the pixel-based image formats above, ``SVG`` is a ``vector-based graphics`` format, meaning it can scale up or down to any dimension without loss of quality. This property makes SVG images a wonderful tool for responsive design. They’re good for pretty much all the same use cases as PNGs, and you should use them whenever you can.*

## [Commit Messages](https://www.theodinproject.com/lessons/foundations-commit-messages)

### Subject
*A `brief` summary of the change you made to the project. Note: GitHub has a 72-character limit so we recommend keeping your commits’ subject to within this amount.*

```html
This is the change I made to the codebase.
```

### Body

*A concise yet clear description of what you did. Describe the problem your commit solves and how.*

```html
Add missing link and alt text to the company's logo

Screen readers won't read the images to users with disabilities without this information.
```

*Provides a subject that specifies your code’s action (e.g., “Add missing link and alt text to the company’s logo”)
Contains a body that provides a concise yet clear description of why the commit needed to be made (e.g., “Screen readers won’t read the images to users with disabilities without this information”)
Separates the subject from the body with a new/blank line. This is a best practice we highly recommend following. It makes commit messages easier for other developers to read.*

### When to commit

A good way to view a commit is like a “snapshot” of your code at the moment that it was made. That version of your code up to that point will be saved for you to revert back to or look back at.

When writing code, it’s considered best practice to commit every time you have a meaningful change in the code. This will create a timeline of your progress and show that your finished code didn’t appear out of nowhere.

In other words, make a commit if you get a piece of code you are working on to function like you want it to, fix a typo, or fix a bug. As you gain experience, you will develop a better feel for what should be committed!



