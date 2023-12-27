
<h1>M5_Section Forms&Tables</h1>

![Section 5](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/M5_SectionModule.png?raw=true)
[m5_table HTML](E:\Dev\web_camp\M5_HTMLForms&Tables\m5_HTML_Tables.html)

```html
<!--
HTML Tables
WHAT ARE TABLES?
Structured sets of data made up of rows and columns;
They can be a great way of displaying data clearly;

LOTS OF ELEMENTS!
To create a table, you will use 5-10 different elements!
It can be tricky to remember them;

ELEMENTS:
<table>
<td>  >- table data (represent a single cell)
<tr> >- table row
<th> >- table header
<thead> >- table header
<tbody> >- table body
<tfoot> >- table footer not rly used;
<rowspan> >- row span 2 rows
<colspan> >- col span  2 cols
<caption> >- bottom caption
-->
```

```html
<h1>Heavies Birds</h1>
<table>
    <thead>
    <tr>
        <th>Animal</th>
        <th>Average mass [kg (lb)]</th>
        <th>Maximum mass [kg (lb)]</th>
        <th>Flighted</th>
    </tr>
    </thead>

    <tbody>
    <tr>
        <td>Common ostrich</td>
        <td>104 (230)</td>
        <td>156.8 (346)</td>
        <td>No</td>
    </tr>

    <tr>
        <td>Somali ostrich</td>
        <td>90 (200)</td>
        <td>130 (287)</td>
        <td>No</td>
    </tr>

    <tr>
        <td>Domestic turkey/wild turkey</td>
        <td>13.5 (29.8)</td>
        <td>39 (86)</td>
        <td>Yes</td>
    </tr>
    </tbody>
</table>
```

```html
<!-- 
colspan \ rowspan usage;
-->
<h2>V2</h2>

<table>
    <thead>
    <tr>
        <th rowspan="2">Animal</th>
        <th colspan="2">Avarage Mass</th>
        <th rowspan="2">Flighted</th>
    </tr>
    <tr>
        <th>[kg]</th>
        <th>(lb)</th>
    </tr>
    </thead>

    <tbody>
    <tr>
        <td>Common ostrich</td>
        <td>104</td>
        <td>(230)</td>
        <td>No</td>
    </tr>

    <tr>
        <td>Somali ostrich</td>
        <td>90</td>
        <td>(200)</td>
        <td>No</td>
    </tr>

    <tr>
        <td>Domestic turkey/wild turkey</td>
        <td>13.5</td>
        <td>(29.8)</td>
        <td>Yes</td>
    </tr>
    </tbody>
</table>
```

<h2>Table Practice 1</h2>
[m5_TablePractice1.html](E:\Dev\web_camp\M5_HTMLForms&Tables\M5_Practice1.html)

```html
<!-- You can use your own content, or use the following to help get started -->
<!--  just make sure to use the same number of data points -->

Subscription | Price | Support 
Free | Free | N/A 
Personal | $9.99 | Weekdays 
Business | $49.99 | 24/7 
```


```html
<table>
    <thead>
        <tr>
            <th>Subscription</th>
            <th>Price </th>
            <th>Support</th>
        </tr>
    </thead>

    <tbody>
    <tr>
        <td>Free</td>
        <td>Free</td>
        <td>N/A</td>
    </tr>

    <tr>
        <td>Personal</td>
        <td>$9.99</td>
        <td>Weekdays</td>
    </tr>

    <tr>
        <td>Business</td>
        <td>$49.99</td>
        <td>24/7</td>
    </tr>
    </tbody>
</table>
```

![M5TablePractice1](https://github.com/KheopS98/HyperSkill/blob/master/ss/webss/m5_TablePractice1.png?raw=true)

<h3>HTML Forms</h3>

```html
<!--
Form it's a container for input elements; Like inputs, checkboxes, buttons etc;
The <form> itself is a container that doesn't have any visual impact;
Represent a document section containing interactive controls for submitting  information;
* action attribute specifies WHERE the farm data should be sent(www.reddit.com);
* method attribute specifies which HTTP method sound be used;
* When submitting a form an HTTP request will be sent, and we control where that request goes to with ACTION ATTRIBUTE and what method will be used GET or POST;
-->

<!--
<input>
Common type of Inputs
<input type= "" attribute>
<input type= "text" attribute>
<input type= "password" attribute>
<input type= "color" attribute>

placeholder attribute >- specifies a placeholder text util user starts to type something

-->

<!--
Labels
Linking text with an input
Or making the whole text and checkbox clickable;
We're making links between labels and inputs with label for ="x"  input id = "x"
-->
```

```html
<h1>HTML_Forms</h1>
<form action="/search">

    <div>
    <label for="username">Enter a UserName:</label>
    <input id = "username" type="text" placeholder="username">
    </div>

    <div>
    <label for="password">Enter a password:</label>
    <input id="password" type="password" placeholder="************">
    </div>

    <div>
    <label for="color">Pick a color: </label>
    <input  id="color" type="color">
    </div>

    <div>
    <label for="number">Pick a number: </label>
    <input id= "number" type="number" placeholder="Enter a number">
    </div>

    <div>
    <label for="time">Pick Time:</label>
    <input id="time" type="time">
    </div>

</form>
```


