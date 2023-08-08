<h1>Module 19. JavaScript Loops</h1>
<p>|__________________________________________|</p>

<h2>I. Course Content</h2>
[]()
<>
[]()
<p>|____________________________________|</p>


<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>


<p id="goUP"></p>
<ul>
    <li><a href="#u1">1. Intro LOOPS</a></li>
    <li><a href="#u2">2. Looping over Arrays</a></li>
    <li><a href="#u3">3. Nested Loops</a></li>
    <li><a href="#u4">4. While Loop </a></li>
    <li><a href="#u5">5. For of LOOPing over Arrays </a></li>
    <li><a href="#u6">6. For in LOOPing over OBJECTS Uncommon </a></li>
    <li><a href="#u7">7. Object methods </a></li>
</ul>


<h2 id="u1">1. Intro LOOPS</h2>

<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* INTRO LOOPS
* FOR
* WHILE
* FOR..OF
* FOR..IN
* +-------------------------------------------------------------------------+|
 */

/*
* FOR Syntax;
* for(
*   [intitialExp];
*   [Condition];
*   [incrementExp]
* )
* 
* */


for (let i = 1; i <= 10 ; i++) {
    console.log(i); // 1 .. 10
}


// Even Numbers;

for (let i = 0; i < 20; i+=2) {
    console.log(i); // 0,2,4 .. 20
}



// Count down from 100

for (var i = 100; i >= 1 ; i--) {
    console.log(i); // 100, 99, 98 .. 1
}



for (let i = 25; i >=0 ; i-=5) {
    console.log(i); // 25,20 ... 0
}
```

<h2 id="u1">2. Looping over Arrays</h2>
<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* Looping Over Arrays;
* +-------------------------------------------------------------------------+|
* 
*/

const animalNames = ["Canidae","Felidae","Cat","Cattle","Dog","Donkey","Goat","Horse","Pig","Rabbit","Aardvark","Aardwolf","Albatross","Alligator","Alpaca","Amphibian","Anaconda","Angelfish","Anglerfish","Ant","Anteater","Antelope","Antlion","Ape","Aphid","Armadillo","Asp","Baboon","Badger","Bandicoot","Barnacle","Barracuda","Basilisk","Bass","Bat","Bear","Beaver","Bedbug","Bee","Beetle","Bird","Bison","Blackbird","Boa","Boar","Bobcat","Bobolink","Bonobo","Booby","Bovid","Bug","Butterfly","Buzzard","Camel","Canid","Capybara","Cardinal","Caribou","Carp","Cat","Catshark","Caterpillar","Catfish","Cattle","Centipede","Cephalopod","Chameleon","Cheetah","Chickadee","Chicken","Chimpanzee","Chinchilla","Chipmunk","Clam","Clownfish","Cobra","Cockroach","Cod","Condor","Constrictor","Coral","Cougar","Cow","Coyote","Crab","Crane","Crawdad","Crayfish","Cricket","Crocodile","Crow","Cuckoo","Cicada","Damselfly","Deer","Dingo","Dinosaur","Dog","Dolphin","Donkey","Dormouse","Dove","Dragonfly","Dragon","Duck","Eagle","Earthworm","Earwig","Echidna","Eel","Egret","Elephant","Elk","Emu","Ermine","Falcon","Ferret","Finch","Firefly","Fish","Flamingo","Flea","Fly","Flyingfish","Fowl","Fox","Frog","Gamefowl","Galliform","Gazelle","Gecko","Gerbil","Gibbon","Giraffe","Goat","Goldfish","Goose","Gopher","Gorilla","Grasshopper","Grouse","Guan","Guanaco","Guineafowl","Gull","Guppy","Haddock","Halibut","Hamster","Hare","Harrier","Hawk","Hedgehog","Heron","Herring","Hippopotamus","Hookworm","Hornet","Horse","Hoverfly","Hummingbird","Hyena","Iguana","Impala","Jackal","Jaguar","Jay","Jellyfish","Junglefowl","Kangaroo","Kingfisher","Kite","Kiwi","Koala","Koi","Krill","Ladybug","Lamprey","Landfowl","Lark","Leech","Lemming","Lemur","Leopard","Leopon","Limpet","Lion","Lizard","Llama","Lobster","Locust","Loon","Louse","Lungfish","Lynx","Macaw","Mackerel","Magpie","Mammal","Manatee","Mandrill","Marlin","Marmoset","Marmot","Marsupial","Marten","Mastodon","Meadowlark","Meerkat","Mink","Minnow","Mite","Mockingbird","Mole","Mollusk","Mongoose","Monkey","Moose","Mosquito","Moth","Mouse","Mule","Muskox","Narwhal","Newt","Nightingale","Ocelot","Octopus","Opossum","Orangutan","Orca","Ostrich","Otter","Owl","Ox","Panda","Panther","Parakeet","Parrot","Parrotfish","Partridge","Peacock","Peafowl","Pelican","Penguin","Perch","Pheasant","Pig","Pigeon","Pike","Pinniped","Piranha","Planarian","Platypus","Pony","Porcupine","Porpoise","Possum","Prawn","Primate","Ptarmigan","Puffin","Puma","Python","Quail","Quelea","Quokka","Rabbit","Raccoon","Rat","Rattlesnake","Raven","Reindeer","Reptile","Rhinoceros","Roadrunner","Rodent","Rook","Rooster","Roundworm","Sailfish","Salamander","Salmon","Sawfish","Scallop","Scorpion","Seahorse","Shark","Sheep","Shrew","Shrimp","Silkworm","Silverfish","Skink","Skunk","Sloth","Slug","Smelt","Snail","Snake","Snipe","Sole","Sparrow","Spider","Spoonbill","Squid","Squirrel","Starfish","Stingray","Stoat","Stork","Sturgeon","Swallow","Swan","Swift","Swordfish","Swordtail","Tahr","Takin","Tapir","Tarantula","Tarsier","Termite","Tern","Thrush","Tick","Tiger","Tiglon","Toad","Tortoise","Toucan","Trout","Tuna","Turkey","Turtle","Tyrannosaurus","Urial","Vicuna","Viper","Vole","Vulture","Wallaby","Walrus","Wasp","Warbler","Weasel","Whale","Whippet","Whitefish","Wildcat","Wildebeest","Wildfowl","Wolf","Wolverine","Wombat","Woodpecker","Worm","Wren","Xerinae","Yak","Zebra","Alpaca","Cat","Cattle","Chicken","Dog","Donkey","Ferret","Gayal","Goldfish","Guppy","Horse","Koi","Llama","Sheep","Yak"];

for (let i = 0; i < animalNames.length; i++) {
    console.log(animalNames[i])
}

for (var i = 0; i < people.length ; i++) {
    console.log(`${people[i]}`.toUpperCase());
}

```

<h2 id="u3">3. Nested Loops</h2>
<p>|____________________________|</p>


```javascript
/*
* +-------------------------------------------------------------------------+|
* 
* +-------------------------------------------------------------------------+|
* 
*/

// For each i iteration, j will do a full execution; i1, j(1,2,3,4)  i2, j(1,2,3,4)
for (var i = 1; i <= 10; i++) {
    console.log(`i is : ${i}`);
    
    //other loop
    for (var j = 1; j <= 4; j++) {
        console.log(`j is ${j}`);
    }
}
```

![nestelooops](https://github.com/TonyDN98/web_camp/blob/main/M19_Loops/ss/nestedLoops.png?raw=true)


```javascript

// Nested Loops on MD Arrays
const seatingChart = [
    ['DAA','DAS','DAW'],
    ['FAA','FAS','FAW'],
    ['GAA','GAS','GAW']
];

for (var i = 0; i < seatingChart.length; i++) {
    for (var j = 0; j < seatingChart; j++) {
        console.log(seatingChart[i][j])
    }
}
```


<h2 id="u4">4. While Loop</h2>
<p>|____________________________|</p>

```javascript
/*
* +-------------------------------------------------------------------------+|
WHILE LOOP
* While we are not knowing the number of iterations;
* +-------------------------------------------------------------------------+|
 */

let count = 0;
while (count < 10){
    console.log(count);
    i+=1
}

// Maybe a board game;

const SECRET = "babyHippo";

let guess= prompt("ENter the secret Code:");

while (guess !== SECRET){
    guess= prompt("ENter the secret Code:");
}

```

<h2 id="u5">5. For of LOOPing over Arrays</h2>
<p>|____________________________|</p>


```javascript

const animalNames = ["Canidae","Felidae","Cat","Cattle","Dog","Donkey","Goat","Horse","Pig","Rabbit","Aardvark","Aardwolf","Albatross","Alligator","Alpaca","Amphibian","Anaconda","Angelfish","Anglerfish","Ant","Anteater","Antelope","Antlion","Ape","Aphid","Armadillo","Asp","Baboon","Badger","Bandicoot","Barnacle","Barracuda","Basilisk","Bass","Bat","Bear","Beaver","Bedbug","Bee","Beetle","Bird","Bison","Blackbird","Boa","Boar","Bobcat","Bobolink","Bonobo","Booby","Bovid","Bug","Butterfly","Buzzard","Camel","Canid","Capybara","Cardinal","Caribou","Carp","Cat","Catshark","Caterpillar","Catfish","Cattle","Centipede","Cephalopod","Chameleon","Cheetah","Chickadee","Chicken","Chimpanzee","Chinchilla","Chipmunk","Clam","Clownfish","Cobra","Cockroach","Cod","Condor","Constrictor","Coral","Cougar","Cow","Coyote","Crab","Crane","Crawdad","Crayfish","Cricket","Crocodile","Crow","Cuckoo","Cicada","Damselfly","Deer","Dingo","Dinosaur","Dog","Dolphin","Donkey","Dormouse","Dove","Dragonfly","Dragon","Duck","Eagle","Earthworm","Earwig","Echidna","Eel","Egret","Elephant","Elk","Emu","Ermine","Falcon","Ferret","Finch","Firefly","Fish","Flamingo","Flea","Fly","Flyingfish","Fowl","Fox","Frog","Gamefowl","Galliform","Gazelle","Gecko","Gerbil","Gibbon","Giraffe","Goat","Goldfish","Goose","Gopher","Gorilla","Grasshopper","Grouse","Guan","Guanaco","Guineafowl","Gull","Guppy","Haddock","Halibut","Hamster","Hare","Harrier","Hawk","Hedgehog","Heron","Herring","Hippopotamus","Hookworm","Hornet","Horse","Hoverfly","Hummingbird","Hyena","Iguana","Impala","Jackal","Jaguar","Jay","Jellyfish","Junglefowl","Kangaroo","Kingfisher","Kite","Kiwi","Koala","Koi","Krill","Ladybug","Lamprey","Landfowl","Lark","Leech","Lemming","Lemur","Leopard","Leopon","Limpet","Lion","Lizard","Llama","Lobster","Locust","Loon","Louse","Lungfish","Lynx","Macaw","Mackerel","Magpie","Mammal","Manatee","Mandrill","Marlin","Marmoset","Marmot","Marsupial","Marten","Mastodon","Meadowlark","Meerkat","Mink","Minnow","Mite","Mockingbird","Mole","Mollusk","Mongoose","Monkey","Moose","Mosquito","Moth","Mouse","Mule","Muskox","Narwhal","Newt","Nightingale","Ocelot","Octopus","Opossum","Orangutan","Orca","Ostrich","Otter","Owl","Ox","Panda","Panther","Parakeet","Parrot","Parrotfish","Partridge","Peacock","Peafowl","Pelican","Penguin","Perch","Pheasant","Pig","Pigeon","Pike","Pinniped","Piranha","Planarian","Platypus","Pony","Porcupine","Porpoise","Possum","Prawn","Primate","Ptarmigan","Puffin","Puma","Python","Quail","Quelea","Quokka","Rabbit","Raccoon","Rat","Rattlesnake","Raven","Reindeer","Reptile","Rhinoceros","Roadrunner","Rodent","Rook","Rooster","Roundworm","Sailfish","Salamander","Salmon","Sawfish","Scallop","Scorpion","Seahorse","Shark","Sheep","Shrew","Shrimp","Silkworm","Silverfish","Skink","Skunk","Sloth","Slug","Smelt","Snail","Snake","Snipe","Sole","Sparrow","Spider","Spoonbill","Squid","Squirrel","Starfish","Stingray","Stoat","Stork","Sturgeon","Swallow","Swan","Swift","Swordfish","Swordtail","Tahr","Takin","Tapir","Tarantula","Tarsier","Termite","Tern","Thrush","Tick","Tiger","Tiglon","Toad","Tortoise","Toucan","Trout","Tuna","Turkey","Turtle","Tyrannosaurus","Urial","Vicuna","Viper","Vole","Vulture","Wallaby","Walrus","Wasp","Warbler","Weasel","Whale","Whippet","Whitefish","Wildcat","Wildebeest","Wildfowl","Wolf","Wolverine","Wombat","Woodpecker","Worm","Wren","Xerinae","Yak","Zebra","Alpaca","Cat","Cattle","Chicken","Dog","Donkey","Ferret","Gayal","Goldfish","Guppy","Horse","Koi","Llama","Sheep","Yak"];

for(let animal of animalNames){
    console.log(animal);
}
```

![](https://github.com/TonyDN98/web_camp/blob/main/M19_Loops/ss/FOR%20OF%20LOOP.png?raw=true)


```javascript
// FOR OF NESTED
const seatingChart = [
    ['DAA','DAS','DAW'],
    ['FAA','FAS','FAW'],
    ['GAA','GAS','GAW']
];

for(let row of seatingChart){
    for (let element of row){
        console.log(element);
    }
}
    
```

<h2 id="u6">6. For in LOOPing over OBJECTS Uncommon</h2>
<p>|____________________________|</p>


```javascript
// Iterate through object will just going for keys;

const obj = {
    ken : 33,
    ben : 34,
    pen : 35,
    men : 36
};

// for..in

for(let person in obj){
    console.log(person); // ken, ben, pen, men
    console.log(`${person} scored ${obj[person]}`); // 33, 34,35,36;
}

```


<h2 id="u7">7. Object methods</h2>
<p>|____________________________|</p>

```javascript
//Object.keys(object); // return an array of keys

// Object.values(obj); // return an array of values of keys;

// Object.entries()
```