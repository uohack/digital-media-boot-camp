Most developers work off of some sort of template when making a new web page, but when you're learning it's often best to start from scratch to really get a handle on HTML structure and syntax. So let's step through a *very* simple web page from scratch.

## 1. Download a text editor

[Sublime Text](https://www.sublimetext.com/3) is a great option, or [Atom](https://atom.io/). These two text editors are free for the base-level. There are others that cost money and provide more features. But while you're starting, you just need a basic text editor.

Once you have one of those downloaded, create a new document called index.html and save it to your desktop.

## 2. Basic HTML structure and syntax

Every HTML document has the same basic structure:

```html
<html>
	<head>
		<!-- This is the head tag, meta stuff goes in here. -->
		<!-- btw, this is a comment tag -->
	</head>
	<body>
		<!-- this is the body tag, all of your content goes in here -->
	</body>
</html>
```

Those lines with angle brackets are called **tags**. HTML tags are how computers are able to read and render a web page. There are lots of different kinds of tags that we'll get into later.

Some tags are children to other parent tags. Like the head and body are children to the html tag.

Almost all HTML tags have to open and close. You can see that they open and then close with a forward slash before the tag name.

## 3. Content

HTML documents are all about the content. You do very little design work via HTML, but it does hold all of your stuff. Like words, pictures and video. Of course, HTML also dictates the structure of you page, like we talked about earlier.

There are specific tags for headlines (`<h1>`, `<h2>`, `<h3>`, ...) and specific tags for paragraphs (`<p>`) and [all sorts of other stuff](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

So let's add some content to our page. Like we said earlier, the content that gets generated on the web page can be found in the body tag. Everything in the head is metadata.

```html
<html>
	<head>
		<!-- This is the head tag, meta stuff goes in here. -->
		<!-- btw, this is a comment tag -->
	</head>
	<body>
		<!-- this is the body tag, all of your content goes in here -->
		<h1>Hello, world</h1>
		<h3>This is a sub-headline</h3>
		<p>This is one paragraph.</p>
		<p>This is another.</p>
	</body>
</html>
```

## 4. Open in browser

One neat trick about working with simple HTML is that you can see it rendered through your browser on your laptop. We call this working locally, as opposed to remotely. That's because you're doing development work locally on your laptop, instead of remotely on a server somewhere else.

In any case, the point that I'm trying to make is that your computer can "serve" HTML just like a server would.

Find your index.html file on your desktop and double click it. Your favorite browser should open up and you should be able to see that text, with minor styling, in a browser.

Congratulations, you just creatd your first web page!

## 5. More content

Let's add some more good stuff to your page.

How about an image? Image tags are "[empty elements](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#Empty_elements)" or "self-closing tags" which means there's only a single tag. If you think about it, that makes sense because there is no content that can go inside an image, besides the image.

Go ahead and add this puppy photo to your file after the last paragraph.

```html
<img src="https://c1.staticflickr.com/5/4004/4405653593_3abf2f3ddc_b.jpg">
```

Your page should look a little like this...

![screen shot 2017-04-02 at 8 37 56 pm](https://cloud.githubusercontent.com/assets/4853944/24594674/536a0436-17e4-11e7-91cd-234552415104.png)

Cute pup, but the image is a little big and the text is a bit dull. Let's spice things up a bit.

## 6. Some CSS

CSS stands for Cascading Style Sheets, which is a complicated way of saying, this is how your will style/design your web page.

For instance, you can set your fonts, colors, widths, heights, borders, spacing and just about everything else with CSS. Let's do some minor tweaking to your page.

Up in the head add a `<style> ... </style>` tag. Inside that style tag, let's add some CSS.

There are a number of ways to target styles to HTML elements, but the easiest way is by tag type.

```html

	<style>
		html {
			font-family: Arial, sans-serif;
		}
		h1 {
			font-size: 48px;
			font-weight: bold;
			color: #ccc;
			text-transform: uppercase;
		}
		p {
			font-family: Georgia, serif;
		}
		img {
			width: 400px;
			margin: 0 auto;
		}
	</style>

```


<details>
	<summary><small>Feeling a little lost? Click here to see how your HTML document should look right now.</small></summary>

	```html

	<html>
		<head>
			<!-- This is the head tag, meta stuff goes in here. -->
			<!-- btw, this is a comment tag -->
				<style>
				html {
					font-family: Arial, sans-serif;
				}
				h1 {
					font-size: 48px;
					font-weight: bold;
					color: #ccc;
					text-transform: uppercase;
				}
				p {
					font-family: Georgia, serif;
				}
				img {
					width: 400px;
					margin: 0 auto;
				}
		</style>
		</head>
		<body>
			<!-- this is the body tag, all of your content goes in here -->
			<h1>Hello, world</h1>
			<h3>This is a sub-headline</h3>
			<p>This is one paragraph.</p>
			<p>This is another.</p>
			<img src="https://c1.staticflickr.com/5/4004/4405653593_3abf2f3ddc_b.jpg">
		</body>
	</html>

	```

</details>

### Wait, what?
Ok, that was a lot, go take a look at how the page looks in your browser.

You see some changes? Let's look at what we did there:

* First we target the `html` tag and set the font family to Arial (or a sans-serif if they computer doesn't have Arial). This font is applied to all of the children elements, which is everything, because `html` is the highest level you can go.
* Then we set the `h1` to be way bigger, bold, gray and uppercase.
* Then we set the `p` to be a serif font, because we don't want them to be Arial in this example.
* Finally, we set the width of the image and center it with a CSS trick.

## 7. MDN help

If you are confused by anything you've seen so far, I highly recommend you go and look it up at the [Mozilla Developer Network](https://developer.mozilla.org/en-US/) (MDN).

If you google any HTML, CSS or JavaScript topic, followed by " + mdn" you'll see some documentation pop up that will answer all of your questions.

For example, if you google ["margin 0 auto + mdn"](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=margin+0+auto+%2B+mdn&*) the first link that pops up is to MDN for the [margin documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) and on that page it talks specifically about [`margin: 0 auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin#Horizontal_centering_with_margin_0_auto).

## Recap

Your file should look something like this right now:

```html
<html>
	<head>
		<!-- This is the head tag, meta stuff goes in here. -->
		<!-- btw, this is a comment tag -->
			<style>
			html {
				font-family: Arial, sans-serif;
			}
			h1 {
				font-size: 48px;
				font-weight: bold;
				color: #ccc;
				text-transform: uppercase;
			}
			p {
				font-family: Georgia, serif;
			}
			img {
				width: 400px;
				margin: 0 auto;
			}
	</style>
	</head>
	<body>
		<!-- this is the body tag, all of your content goes in here -->
		<h1>Hello, world</h1>
		<h3>This is a sub-headline</h3>
		<p>This is one paragraph.</p>
		<p>This is another.</p>
		<img src="https://c1.staticflickr.com/5/4004/4405653593_3abf2f3ddc_b.jpg">
	</body>
</html>
```

## Bonus. Some JavaScript

In keeping with the simplicity of this demo, here's the simplest explanation of JavaScript I can think of: JavaScript allows you to manipulate your web page in fun and interesting ways.

Here's the simplest demo I can give. Right before the end of your `body` tag, make a new `<script>...</script>` tag, we're going to change the color of the page's background to yellow.

```html
<script>
	document.onclick = function(){
		document.documentElement.style.background = "#ff0";
	};
</script>
```

Now, when you click anywhere on the page, the background changes to yellow.

With this code, your file should look something like this:

```html
<html>
	<head>
		<!-- This is the head tag, meta stuff goes in here. -->
		<!-- btw, this is a comment tag -->
			<style>
			html {
				font-family: Arial, sans-serif;
			}
			h1 {
				font-size: 48px;
				font-weight: bold;
				color: #ccc;
				text-transform: uppercase;
			}
			p {
				font-family: Georgia, serif;
			}
			img {
				width: 400px;
				margin: 0 auto;
			}
	</style>
	</head>
	<body>
		<!-- this is the body tag, all of your content goes in here -->
		<h1>Hello, world</h1>
		<h3>This is a sub-headline</h3>
		<p>This is one paragraph.</p>
		<p>This is another.</p>
		<img src="https://c1.staticflickr.com/5/4004/4405653593_3abf2f3ddc_b.jpg">
		<script>
			document.onclick = function(){
				document.documentElement.style.background = "#ff0";
			};
		</script>
	</body>
</html>
```

With a bit more code, you can make it change into a random color.

```html
<script>
	// Reusable function to get random colors
	// Courtesy: http://stackoverflow.com/a/1484514
	function getRandomColor() {
		var letters = '0123456789ABCDEF';
		var color = '#';
		for (var i = 0; i < 6; i++ ) {
			color += letters[Math.floor(Math.random() * 16)];
		}
		return color;
	}

	// When you click on the page, let's change the text color
	document.onclick = function(){
		//console.log("hello");
		// Get the container div
		var page = document.documentElement;
		// Set variable to new color on each click
		var newColor = getRandomColor();
		// Print out that new color to the console
		console.log(newColor);
		// Set the CSS color of everything in #container to the new color
		page.style.background = newColor;
	};
</script>
```

Your final file might look something like this:

```html
<html>
	<head>
		<!-- This is the head tag, meta stuff goes in here. -->
		<!-- btw, this is a comment tag -->
			<style>
			html {
				font-family: Arial, sans-serif;
			}
			h1 {
				font-size: 48px;
				font-weight: bold;
				color: #ccc;
				text-transform: uppercase;
			}
			p {
				font-family: Georgia, serif;
			}
			img {
				width: 400px;
				margin: 0 auto;
			}
	</style>
	</head>
	<body>
		<!-- this is the body tag, all of your content goes in here -->
		<h1>Hello, world</h1>
		<h3>This is a sub-headline</h3>
		<p>This is one paragraph.</p>
		<p>This is another.</p>
		<img src="https://c1.staticflickr.com/5/4004/4405653593_3abf2f3ddc_b.jpg">
		<script>
			// Reusable function to get random colors
			// Courtesy: http://stackoverflow.com/a/1484514
			function getRandomColor() {
				var letters = '0123456789ABCDEF';
				var color = '#';
				for (var i = 0; i < 6; i++ ) {
					color += letters[Math.floor(Math.random() * 16)];
				}
				return color;
			}

			// When you click on the page, let's change the text color
			document.onclick = function(){
				//console.log("hello");
				// Get the container div
				var page = document.documentElement;
				// Set variable to new color on each click
				var newColor = getRandomColor();
				// Print out that new color to the console
				console.log(newColor);
				// Set the CSS color of everything in #container to the new color
				page.style.background = newColor;
			};
		</script>
	</body>
</html>
```

I know this file seems simple, but it contains all of the building blocks to a more complicated website. And, FWIW, you could put this file up on a server and it would act like a real, full-blown, regular website.

To prove that, I've put it up [here](http://uohack.com/digital-media-boot-camp/web/examples/02-starting-from-scratch.html).
