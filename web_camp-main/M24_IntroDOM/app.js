// document.dir();

document.getElementById('banner');

const bannerVar = document.getElementById('banner');
console.dir(bannerVar);



// getElementByTagName
const allImages = document.getElementsByTagName('img');

for (let img of allImages){
    console.log(img.src);
}


// element.querySelector

const links = document.querySelectorAll('p a');
for (let link of links){
    console.log(link.href);
}


