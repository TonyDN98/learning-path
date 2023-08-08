const express = require('express');
const app = express();


app.use((req,res)=>{
    // request , response; express is making this 2 objects by parsing the hhtp request;
    //everytime a request hit this server; this method will print it out;
    console.log("We got a new request;")

    /*
    * res.send("Hello we got your req its a response;")
    * Response with  a string
    * */

    /*
    * Response with an Object;
    * res.send({
    *   color: "red",
    *   black: "eeee"
    * });
    * */

    /*
    * Reponse with some HTML;
    * res.send('<h2>This is my webpage;');
    *
    *
    * */

    // !!!!!!!!  !!Only one response per REQUEST !!!!!!
    // res.send('<h1>This is  my webpage</h1>');


});


app.get('/cats', (req, res)=>{
    console.log("cat request;")
    res.send("Meaw");
});


app.get('/dogs', (req, res) =>{
    console.log("Dog request");
    res.send("woof");
});


app.post('/cats', (req, res) =>{
    res.send("This is diferent POST REQUEST HERE");
});


app.listen(8080, () =>{ // start the server listening on the port 3000;
    console.log('Listening on port 8080');
})


/*
* Routing
* app.get();
* !!!! Route incoming request to outgoing response; !!!
*
*
* Take incoming request and the path that is requested
* localhost:8080/dogs
*
* /cats => 'meow'
* /dogs => 'woof'
* '/' => Welcome to our home page
* */
