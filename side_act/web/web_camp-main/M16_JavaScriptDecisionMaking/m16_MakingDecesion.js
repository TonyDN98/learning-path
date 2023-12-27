console.log("Before condition");
let rand = Math.floor(((Math.random() * 10) + 1));
if(rand < 5){
    console.log(`Your random number ${rand} < 5`);
}else if (rand === 5){
    console.log(`Your random number ${rand} is 5`);

}else{
    console.log(`Your random number ${rand} > 5`);
}

console.log("After condition");

/*
* Exercise;
* 0 - 4 Free  child Ticket
* 5 - 10 10$  kid Ticket
* 11 - 18 15$  Teen Ticket
* 19 - 65 20$  Sention Ticket
* 
* */

let age = parseInt(prompt("Age:"));
let fee = 0;

if(age >= 0 && age <=4){
    console.log(`Child 0 - 4 fee ${fee}`);
}else if (age >= 5 && age <=10){
    fee = 10;
    console.log(`Kid 5 - 10 fee ${fee}$`);
}else if (age >= 11 && age <=18){
    fee = 15;
    console.log(`Teen 11 - 18 fee ${fee}$`);
}else {
    fee = 20;
    console.log(`Senior19 - 65 fee ${fee}$`);
}

//Password 6+ without space;
let password = prompt("Enter Pass:");

if (password.length >= 6){
    if (password.indexOf(" ") === -1){
        console.log("GJ! No space");
    }else{
        console.log("Can't contain spaces;")
    }
}
