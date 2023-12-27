const express = require('express');
const app = express();

//path is built in Node

const path = require("path");


app.set('view engine', 'ejs');

// run nodemon from a different path, not current directory;
app.set('views', path.join(__dirname, '/views'));


app.get('/', (req, res) =>{
    // sending back the ejs file as response;
    res.render('home.ejs');
})

app.get('/rand', (req, res)=>{
    const num =  Math.floor((Math.random() * 10) + 1);
    res.render('random.ejs', {bubbles: num}); //bubbles will be used in the ejs file; also the second arg it's an object;
})


app.listen(3000, () =>{
    console.log("Listen on PORT 3000");
})