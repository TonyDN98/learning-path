
<h1>Module 12. Boostrap Framework</h1>
<p>|_____________________________________________________|</p>



<h2>_LINKS TO OFFICIAL BOOTSTRAP DOCS_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>
    <li><a href="https://getbootstrap.com/docs/4.6/layout/overview/#containers">1. BOOTSTRAP Containers;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/layout/grid/">2. BOOTSTRAP  Grid System;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/utilities/spacing/">3. MARGIN AND PADDING;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/forms/">4. BOOTSTRAP Forms;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/navbar/">5. BOOTSTRAP NavBars;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/input-group/">6. BOOTSTRAP Input Group;</a></li>
    <li><a href="https://icons.getbootstrap.com/">7. BOOTSTRAP ICONS;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/alerts/">8. BOOTSTRAP Alerts;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/buttons/">9.BOOTSTRAP Buttons;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/components/badge/">10. BOOTSTRAP Badges;</a></li>
    <li><a href="https://getbootstrap.com/docs/4.6/utilities/borders/">11. BOOTSTRAP Borders;</a></li>





</ul>


<h2 id="u1">_1. Including Bootstrap TEMPLATE_</h2>
<p>|______________________________________________________|</p>

```html

<!--
|------------------------------------------------------------------------------------------|
| Including Bootsrap CSS via Remoted Host File;
| CSS	https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css
| JS    https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js
|------------------------------------------------------------------------------------------|
-->
```

```html

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">

```

 
```html

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>

```

<h2 id="u2">2. Containers;</h2>
<p>|_______________________|</p>

<h3>All-in-one Container;</h3>

```html
<!--
Our default .container class is a responsive, 
fixed-width container, meaning its max-width changes
at each breakpoint.
-->
<div class="container">
    <!-- Content goes here!  -->
    <h1>Heading</h1>
    <p>lorem</p>
</div>
```
<h3>Responsive Containers;</h3>
<p>|_____________________________|</p>

```html
<div class="container-sm">100% wide until small breakpoint</div>
<div class="container-md">100% wide until medium breakpoint</div>
<div class="container-lg">100% wide until large breakpoint</div>
<div class="container-xl">100% wide until extra large breakpoint</div>
```


<h2>3. Grid System</h2>
<p>|_______________________|</p>


<h3>Auto-layout columns Equal-Width</h3>
<p>|_______________________________________|</p>


```html
<div class="container">
<!-- First Row -->
  <div class="row">
    <div class="col">
      1 of 2
    </div>
    <div class="col">
      2 of 2
    </div>
  </div>
    
<!-- Second Row -->
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col">
      2 of 3
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
</div>
```


<h3>Setting one column width</h3>
<p>|_______________________________|</p>


```html
<div class="container">
<!--First Row-->
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-6">
      2 of 3 (wider)
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
<!--Second Row-->
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-5">
      2 of 3 (wider)
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
</div>
```

<h3>Variable width content</h3>
<p>|___________________________|</p>

```html
<div class="container">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
</div>
```

<h3>Stacked to Horizontal</h3>
<p>|__________________________|</p>


```html
<div class="container">
<!--First Row-->
  <div class="row">
    <div class="col-sm-8">col-sm-8</div>
    <div class="col-sm-4">col-sm-4</div>
  </div>
<!--Second Row-->
  <div class="row">
    <div class="col-sm">col-sm</div>
    <div class="col-sm">col-sm</div>
    <div class="col-sm">col-sm</div>
  </div>
</div>
```

<h2>4. Grid Alignment align-items-*</h2>
<p>|_______________________________________________|</p>

<h3>Vertical Alignment</h3>
<p>|_______________________|</p>

```html
<div class="container">
<!--align-items-start-->
  <div class="row align-items-start">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>

    
    <!--align-items-center-->
    <div class="row align-items-center">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>

    
    <!--align-items-end-->
    <div class="row align-items-end">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
</div>
```

<h3>Vertical Alignment SELF</h3>
<p>|____________________________|</p>


```html
<div class="container">
  <div class="row">
<!--SELF-->
    <div class="col align-self-start">
      One of three columns
    </div>
      <!--SELF-->
      <div class="col align-self-center">
      One of three columns
    </div>
      <!--SELF-->
      <div class="col align-self-end">
      One of three columns
    </div>
  </div>
</div>
```


<h3>Horizontal Alignment</h3>
<p>|_________________________|</p>

```html
<div class="container">
<!--ROW START 4/4//12-->
  <div class="row justify-content-start">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
    
    <!--ROW CENTER 4/4//12-->
    <div class="row justify-content-center">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
    
    <!--ROW END 4/4//12-->
    <div class="row justify-content-end">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>

    <!--ROW AROUND 4/4//12-->
    <div class="row justify-content-around">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>

    <!--ROW BETWEEN 4/4//12-->
    <div class="row justify-content-between">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
</div>
```
