# Introduction

Welcome to the Web Basics Skills Pack. This document contains the fundamental ideas of how the web works and how to build websites. There will be no code, but you will get a decent understanding about how the web works. It should take about 20 minutes to read this for the first time, assuming you click through on some of the links and do some outside research as well.

# Table of Contents

1. [How does the internet work?](#how-does-the-internet-work)
1. [How do HTML, CSS and JS work together?](#how-do-html-css-and-js-work-together)
1. [Website example](#website-example)

# How does the internet work?

The internet is basically a big network of computers. There are big computers and small computers, powerful computers and puny computers. Some spend their whole lives collecting information (think: [Google Analytics](http://google.com/analytics/)), some are highly specialized (think: [Roku](https://www.roku.com/)), and some are multi-talented (think: your laptop).

For the purposes of this introduction, let's say that there are two basic kinds of computers: personal devices and servers.

Personal devices are desktops, laptops, tablets, mobile phones or any other device you use to surf the web.

Servers, on the other hand, are computers that specialize in serving the websites that you pull up on your personal devices. These computers usually have operating systems made for servers that are different from what are on your laptop or phone. 

Some servers have a [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) and some require you to use a [command line](https://en.wikipedia.org/wiki/Command-line_interface).

You can buy server space from a number of companies that offer a wide range of services. Some, like [HostGator](http://www.hostgator.com/apps/wordpress-hosting) will set up the server to fit your exact needs, say if you needed to host a WordPress website. Others, like [Amazon Web Services](https://aws.amazon.com/websites/?nc2=h_l3_wa) offer dozens of customized or customizable services and tools. [Here is a good intro video](https://aws.amazon.com/websites/?nc2=h_l3_wa) to AWS, one of the most popular hosting services.

### So, how does that all work in the real world?

Let's say you want to take a quick study break to check Facebook. You pop open a new tab and type in [facebook.com](https://facebook.com) into your browser. When you do that, your personal device sends a request out into the internet. That request is to load the Facebook homepage on your device.

When that request is sent out into the internet, it gets directed to Facebook's servers. [Somewhere](http://projects.registerguard.com/turin/2016/jul/31/lumber-town-rides-digital-wave-to-rally/), a Facebook server receives your request, looks up the files you want and sends them back into the internet. That response is routed back to your personal device which renders out the documents and data as a website and you get to scroll through your timeline.

In reality, there are several other things that happen when you request a website. If you want to learn more about that you can read about that [here](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm). 

# How do HTML, CSS and JS work together?

While websites can be created using many different programming languages, they all boil down to HTML, CSS and JavaScript by the time they get to your computer. In other words, the response from the server that your personal device receives is almost certainly one of those three types of documents.

I call them documents because they contain code but are just simple text documents. While it's theoretically possible, you would not want to write HTML/CSS/JS in a program like Microsoft Word, instead, there are text editors like [Sublime Text](http://www.sublimetext.com/3) or [TextWrangler](http://www.barebones.com/products/TextWrangler/) for writing code. Of course, there are many more text editors out there, but those are the two best free text editors available.

### HTML

HTML is the foundation of any webpage. It provides the structure and content for the entire page and is absolutely necessary for any website.

In fact, when you request a website from a server, you're actually requesting the default HTML file from the website.

That HTML file will contain all of the text on the page, all of the images and all of the links as well as other things.

If you were to think about building a website as building a house, the HTML would be the base house with bare walls, cement floors and zero furniture. 

### CSS

CSS provides the style and helps with the design of a website. Think fonts, colors, grid, etc. 

In the house metaphor, CSS is the carpet and paint, as well as some of the things that make your house feel like home. No two websites are identical ([although some are very similar](http://adventurega.me/bootstrap/)) and CSS helps make them unique.

CSS is included in a webpage via a link in the HTML document. So, when you request a website, an HTML document is downloaded and rendered by your browser. That HTML document will include a link to a CSS document that applies styles to your HTML content.

### JavaScript

JavaScript can do a lot of different things, but at the most basic level it provides useful functionality to you website. 

One example of useful JavaScript is analytics tracking. Whether you use Google Analytics or [Chartbeat](https://chartbeat.com), those features use JavaScript to track users. 

Another example is a photo slideshow. It's possible to build a photo slideshow in only HTML and CSS, but often JavaScript will manipulate the HTML and apply CSS to a slideshow to make it work properly.

Going back to the house metaphor, JS would be the fridge or washer and dryer. These are very useful tools that have specific functions. Similarly, JS libraries that you build into your website often do one thing and one thing only.

Like CSS, JS is loaded into a web page via a link in the HTML. Without HTML, JS would have nothing to manipulate or interact with.

*Please note:* [JavaScript has nothing to do with Java](http://javascriptisnotjava.io/).

# Website example

Examples are helpful because they help put things you've learned into perspective. So, let's think about a personal portfolio website and talk through what you would need to do to make one.

### Domain and hosting

First things first, you need a domain name and hosting service (think servers). Domain names are easy to purchase. There are number of reputable companies ([Google Domains](https://domains.google/#/), [Name](https://name.com), etc.) that will sell you a domain name for one year at a time. This is normal, and I would suggest you set up auto-renewal because the last thing you want is to build a nice website for yourself and then lose it after one year to some [squatter](https://en.wikipedia.org/wiki/Cybersquatting).

Next, you need to point that domain name somewhere, AKA: you need server space for your website. There are a lot of good hosting services out there and I suggest you do some research before picking the best one for you. If you just need a simple website (probably a good place to start), your school may offer free server space or you can use [Github](https://pages.github.com/) to host a site for free. *Note: Github has a high barrier of entry, but is a [good tool to know](https://github.com/uohack/github-basics). More on this in later Digital Media Boot Camp posts.*

### HTML

After you have that set up, you need something to put on your server. I'd start with the HTML. 

If it's a personal portfolio website (let's say you're a photographer) all you really need is a single page with introductory text, some photos (you should edit tight) and some contact info.

That's a pretty simple page so it should be pretty easy to visualize and create. 

Don't worry about the code right now, we'll get into that in a later post.

### CSS

Now that you have your foundation down (HTML), you need to add some style. After all, Times New Roman and blue links are very 1992. 

For you designers out there, this is the fun part. You get to choose fonts, colors and all sorts of other good stuff to make this page your own.

### JavaScript

My personal belief is that you should avoid JS unless it's absolutely necessary. Other people feel differently, and that's fine. Even if you don't like a ton of JS (like me), there are certainly a few utilities that you need to build into your site.

One is analytics. Setting up a Google Analytics account is free with your Google login and plugging in the code is even easier. That way you can see how many folks are looking at your site.

Another helpful utility would be a photo slideshow. There are [a](https://galleria.io/) [lot](https://owlcarousel2.github.io/OwlCarousel2/) of different slideshows out there so you have to pick the best one for you.

Other than that, I don't think you need any other JS for this basic website.

### Wrap up

When you build your first website this process might take weeks. After a few years, you could probably build this in a few hours. 

What I'm trying to say is that this is a skill that takes practice to get good at. There's a lot to remember but you always have Google to help you out. And I promise, someone out there has had the same question you have so don't be afraid to look.