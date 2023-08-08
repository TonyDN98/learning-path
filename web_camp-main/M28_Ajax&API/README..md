<h1>Module 28. Ajax & API</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[]()
<>
[]()
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>`
    <li><a href="#u1">1. preventDefault Form</a></li>
    <li><a href="#u2">2. extractDataFrom Form</a></li>
</ul>




<h2 id="u1">1. Intro Ajax& API & JSON</h2>
<p>|____________________________|</p>

```javascript
/*
* AJAX;
* Asynchronus
* JavaScript
* And
* XML;
* 
* * AJAJ;
* Asynchronus
* JavaScript
* And
* JSON;
* 
* 
* making Requests behind the scens;
* Making Request when we already have our page loaded; Async definition;
* 
* 
* API(Aplication Program Interface)-> Requesting External Data;
* We dont want HTML or CSS or JS file, we want data to fetch;
* Web based, http based;
*
* 
* JSON
* - JS Object Notation;
* It's a format of sharing information;
* "every key" : value
* 
* 
* There is a way to transform JSON into Js using a buillt-in method;
* JSON->Js
* 
* JSON.parse(text);
* 
* Js- JSON
* 
* JSON.strigify();
* 
* */


```

[JSON Format Validator](https://jsonformatter.curiousconcept.com/)



<h2 id="u2">2. Postman</h2>
<p>|____________________________|</p>

[Postman Download](https://www.postman.com/downloads/)

```javascript
/*
* Tool for developers to test API requests;
* Visualize the JSON data retrived and understand the API:
* */
```

<h2 id="u3">3. HTTP Verbs; </h2>
<p>|____________________________|</p>

```javascript
/*
* Types of Request
* GET Req - > Get or Retrive Information from an API;
* Post Req -> Send Data somewhere;
* */
```

<h2 id="u4">4. HTTP Status Codes; </h2>
<p>|____________________________|</p>

```javascript
/*
* Status codes;
* 200 OK;
* 404 NOT FOUND;
* 
* 
* */
```

<h2 id="u5">5. QueryString; </h2>
<p>|____________________________|</p>

```javascript
/*
* URL: https://developer.mozilla.org/en-US/search  
*                                                   ?q=somethig& --> Query String
* 
* */
```

<h2 id="u6">6. HTTP Headers; </h2>
<p>|____________________________|</p>

```javascript
/*
* Header full of  key values information;
* */

/*
* Accept header*
* API Response Format:
* text/html -> HTML;
* applications/json - > JSON Respoonse;
* text/plain -> text;
* */
```

<h2 id="u7">7. XHR, ; </h2>
<p>|____________________________|</p>


```javascript
// making request with js;
// OLD VERSION

const req = new  XMLHttpRequest();

req.onload= function (){
    console.log("IT LOEADED;")
   const data =  JSON.parse(this.responseText); // JSON parse 
    console.log(data.name);
    
}

req.onerror = function (){
    console.log('EROORR');
    console.log(this);
}

req.open('GET', "https://swaoi.dev/api/people/1/");
req.send();


```

<h2 id="u8">8. FETCH XHR NEW, ; </h2>
<p>|____________________________|</p>

```javascript
// Newer version;

fetch("https://swaoi.dev/api/people/1/")
    .then(res => {
        console.log("RESOLVED", res);
        res.json().then(data) =>
        console.log(data, "JSON done"); // added to fetch response obj
    } )
    .catch(e =>{
        console.log("Error",e);
    });
```

<h2 id="u9">9. AXIOS LIBRARY USE IT; </h2>
<p>|____________________________|</p>

```javascript
/*
* 
* 
* */
```

