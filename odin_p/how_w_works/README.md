# How does the Web works
[odin how does the internet works](https://www.theodinproject.com/lessons/foundations-how-does-the-web-work#additional-resources)  

[How does internet works MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work)

[MDN Client Server DNS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works#clients_and_servers)

  
[DNS Explained YT](https://www.youtube.com/watch?v=72snZctFFtA&t=45s)

### Simple Networks

![Network](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work/internet-schema-6.png)

So we are connected to the telephone `infrastructure`. The next step is to send the messages from our network to the network we want to reach. To do that, we will connect our network to an ``Internet Service Provider (ISP)``. An `ISP` is a company that manages some special routers that are all linked together and can also access other `ISPs`' routers. So the message from our network is carried through the network of `ISP` networks to the destination network. The Internet consists of this whole infrastructure of networks.

![with isp](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work/internet-schema-7.png)

---

### Finding computers
Thus any computer linked to a network has a unique address that identifies it, called an "`IP address`" (where `IP` stands for `Internet Protocol`). It's an address made of a series of four numbers separated by dots, for example: `192.0.2.172.`
  
`google.com` is the domain name used on top of the IP address `142.250.190.78`

![google dns](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work/dns-ip.png)

> **NOTE! 2 Servers can be connected with wires, and the content that we accessing from them are stored directly on their harddrive.**

> **When files travel across the interet, they are breaked into smaller pieces that are called `packages`, and when they arive at destination, are assambled in the correct order.** 
>

--- 

### What is the difference between webpage, website, web server, and search engine?

> `web page`
A document which can be displayed in a web browser such as Firefox, Google Chrome, Opera, Microsoft Edge, or Apple Safari. These are also often called just "pages."

  
>`website`
A collection of web pages which are grouped together and usually connected together in various ways. Often called a "website" or a "site."

>`web server`
A computer that hosts a website on the Internet.
---

### Clients and servers

![client-server](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works/simple-client-server.png)

`Computers` connected to the `internet` are called `clients` and `servers`.

> `Clients` are the typical web user's internet-connected devices (for example, your computer connected to your Wi-Fi, or your phone connected to your mobile network.

>`Servers` are computers that store `webpages`, `sites`, or `apps`. When a client device wants to access a webpage, a copy of the webpage is downloaded from the server onto the client machine to be displayed in the user's web browser.
---
### Components 

>Your `internet connection`: Allows you to send and receive data on the web. It's basically like the street between your house and the shop.
  
>`TCP/IP: Transmission Control Protocol` and `Internet Protocol` are communication protocols that define how data should travel across the internet. This is like the transport mechanisms that let you place an order, go to the shop, and buy your goods. In our example, this is like a car or a bike (or however else you might get around).
  
>`DNS: Domain Name System` is like an address book for websites. When you type a web address in your browser, the browser looks at the DNS to find the website's IP address before it can retrieve the website. The browser needs to find out which server the website lives on, so it can send HTTP messages to the right place (see below). This is like looking up the address of the shop so you can access it.
  
>`HTTP: Hypertext Transfer Protocol` is an application protocol that defines a language for clients and servers to speak to each other. This is like the language you use to order your goods.
  
>`Component files`: A website is made up of many different files, which are like the different parts of the goods you buy from the shop. These files come in two main types:
  
>`Code files`: Websites are built primarily from HTML, CSS, and JavaScript, though you'll meet other technologies a bit later.
  
>`Assets`: This is a collective name for all the other stuff that makes up a website, such as images, music, video, Word documents, and PDFs.
---

### So what happens, exactly?

```
When browsers send requests to servers for HTML files, those HTML files often contain <link> elements referencing external CSS stylesheets and <script> elements referencing external JavaScript scripts. It's important to know the order in which those files are parsed by the browser as the browser loads the page:
```

```
The browser parses the HTML file first, and that leads to the browser recognizing any <link>-element references to external CSS stylesheets and any <script>-element references to scripts.
```

```
As the browser parses the HTML, it sends requests back to the server for any CSS files it has found from <link> elements, and any JavaScript files it has found from <script> elements, and from those, then parses the CSS and JavaScript.
```

```
The browser generates an in-memory DOM tree from the parsed HTML, generates an in-memory CSSOM structure from the parsed CSS, and compiles and executes the parsed JavaScript.
```

```
As the browser builds the DOM tree and applies the styles from the CSSOM tree and executes the JavaScript, a visual representation of the page is painted to the screen, and the user sees the page content and can begin to interact with it.
```


> !NOTE First it gets back the HTML page, and as it progress and find external links to stylesheet and functionality it request back to the server.
---