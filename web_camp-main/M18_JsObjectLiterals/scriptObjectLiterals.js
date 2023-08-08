const kitchenSink = {
    favNum : 9321232,
    isFUnny: true,
    colors: ['red', 'orange']
};

const product = {
    name:  "Gummy Bear",
    inStock: true,
    price : 1.99,
    flavors: ["cherry", "grapes", "apples"]
};

const restaurant = {
    name: 'Ichiran Ramen',
    address: `${Math.floor(Math.random() * 100) + 1} Johnson Ave`,
    city: 'Brooklyn',
    state: 'NY',
    zipcode: '11206',
}

//YOUR CODE GOES DOWN HERE:
let fullAddress = `${restaurant.address}, ${restaurant.city}, ${restaurant.state}, ${restaurant.zipcode}`;


// Modify
const midterms = {dany : 55, thomas:78};

// change thomas to 79
midterms.thomas = 79;
midterms.dany = 55;

//Add a new element to object;
midtterms.ezz = '88';
midtterms.antonio = '98';


// Array of Obj
// Array of objects;

const shoppingCard = [
    {
        product: 'Jenga',
        price: 9.99,
        quantity: 3
    },{
        product: 'benga',
        price: 9.99,
        quantity: 4
    },{
        product: 'daih',
        price: 9.99,
        quantity: 22
    },{
        product: 'Jenga',
        price: 9.99,
        quantity: 3
    }
];

let vars = shoppingCard[0].product;
//benga