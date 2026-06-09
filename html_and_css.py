HTML & CSS Complete Concepts with Detailed Examples
1. What is HTML?
HTML (HyperText Markup Language) is used to create the structure of a web page.
Real-World Example
Think of a house:
HTML = Structure (walls, doors, windows)
CSS = Design (paint, furniture, decoration)
Basic HTML Structure
HTML
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>Hello World</p>
</body>
</html>
2. HTML Elements
An HTML element consists of:
HTML
<tagname>Content</tagname>
Example:
HTML
<p>This is a paragraph</p>
3. Headings
HTML
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>
<h4>Small Heading</h4>
<h5>Smaller Heading</h5>
<h6>Smallest Heading</h6>
4. Paragraphs
HTML
<p>This is a paragraph.</p>
5. Text Formatting
HTML
<b>Bold</b>

<strong>Important Text</strong>

<i>Italic</i>

<em>Emphasized</em>

<u>Underline</u>

<mark>Highlighted</mark>

<small>Small Text</small>

<del>Deleted Text</del>

<ins>Inserted Text</ins>

<sub>Subscript</sub>

<sup>Superscript</sup>
Example:
HTML
H<sub>2</sub>O

x<sup>2</sup>
6. Links
HTML
<a href="https://google.com">
    Visit Google
</a>
Open in new tab:
HTML
<a href="https://google.com" target="_blank">
    Google
</a>
7. Images
HTML
<img src="image.jpg" alt="Nature">
Set size:
HTML
<img src="image.jpg"
     width="300"
     height="200">
8. Lists
Ordered List
HTML
<ol>
    <li>Python</li>
    <li>Django</li>
    <li>React</li>
</ol>
Output:
Python
Django
React
Unordered List
HTML
<ul>
    <li>Apple</li>
    <li>Mango</li>
</ul>
9. Tables
HTML
<table border="1">
<tr>
    <th>Name</th>
    <th>Age</th>
</tr>

<tr>
    <td>Hari</td>
    <td>25</td>
</tr>
</table>
10. Forms
Forms collect user data.
HTML
<form>

Name:
<input type="text">

Password:
<input type="password">

<input type="submit">

</form>
11. Input Types
HTML
<input type="text">

<input type="password">

<input type="email">

<input type="number">

<input type="date">

<input type="radio">

<input type="checkbox">

<input type="file">

<input type="submit">
12. Buttons
HTML
<button>Click Me</button>
13. Text Area
HTML
<textarea rows="5" cols="30">
</textarea>
14. Dropdown
HTML
<select>
    <option>Python</option>
    <option>Django</option>
</select>
15. Semantic HTML
Provides meaning to content.
HTML
<header></header>

<nav></nav>

<section></section>

<article></article>

<aside></aside>

<footer></footer>
Example:
HTML
<header>
    My Website
</header>

<nav>
    Home About Contact
</nav>

<footer>
    Copyright 2026
</footer>
16. Div and Span
Div
Block element
HTML
<div>
    Content
</div>
Span
Inline element
HTML
<span>Hello</span>
CSS (Cascading Style Sheets)
Used for designing web pages.
17. CSS Syntax
CSS
selector{
    property:value;
}
Example:
CSS
h1{
    color:red;
}
18. Ways to Add CSS
Inline CSS
HTML
<h1 style="color:red;">
    Welcome
</h1>
Internal CSS
HTML
<style>

h1{
color:red;
}

</style>
External CSS
HTML:
HTML
<link rel="stylesheet"
      href="style.css">
style.css
CSS
h1{
    color:red;
}
19. CSS Selectors
Element Selector
CSS
p{
color:blue;
}
Class Selector
CSS
.title{
color:red;
}
HTML:
HTML
<h1 class="title">
Welcome
</h1>
ID Selector
CSS
#header{
color:green;
}
HTML:
HTML
<h1 id="header">
Hello
</h1>
20. Colors
CSS
color:red;

color:#FF0000;

color:rgb(255,0,0);
21. Background
CSS
background-color:yellow;
Background Image
CSS
background-image:url("bg.jpg");
22. Fonts
CSS
font-size:20px;

font-family:Arial;

font-weight:bold;
23. Text Styling
CSS
text-align:center;

text-decoration:underline;

text-transform:uppercase;

letter-spacing:2px;
24. Box Model
Every element consists of:
Plain text
Margin
Border
Padding
Content
Example:
CSS
div{

width:200px;

padding:20px;

border:2px solid black;

margin:30px;

}
25. Borders
CSS
border:2px solid red;
Different Borders
CSS
border-style:dashed;

border-style:dotted;

border-style:double;
26. Margin
Outside spacing.
CSS
margin:20px;
27. Padding
Inside spacing.
CSS
padding:20px;
28. Display Property
CSS
display:block;

display:inline;

display:inline-block;

display:none;
29. Position
Static
Default
CSS
position:static;
Relative
CSS
position:relative;
left:20px;
Absolute
CSS
position:absolute;
top:50px;
Fixed
CSS
position:fixed;
Sticky
CSS
position:sticky;
top:0;
30. Flexbox
Used for layouts.
HTML:
HTML
<div class="container">

<div>1</div>
<div>2</div>
<div>3</div>

</div>
CSS:
CSS
.container{

display:flex;

justify-content:center;

align-items:center;

}
Properties:
CSS
flex-direction:row;

flex-direction:column;

justify-content:space-between;

justify-content:space-around;

align-items:center;
31. CSS Grid
CSS
.container{

display:grid;

grid-template-columns:
1fr 1fr 1fr;

gap:20px;

}
32. Pseudo Classes
Hover Effect
CSS
button:hover{

background:red;

}
Focus
CSS
input:focus{

border:2px solid blue;

}
33. Transitions
CSS
button{

transition:0.5s;

}

button:hover{

background:red;

}
34. Animations
CSS
@keyframes move{

from{
left:0;
}

to{
left:200px;
}

}
Use:
CSS
div{

animation:move 3s;

}
35. Responsive Design
Mobile-Friendly Website
HTML
<meta name="viewport"
content="width=device-width,
initial-scale=1.0">
Media Query
CSS
@media(max-width:768px){

h1{
font-size:20px;
}

}
36. Z-Index
Controls stacking order.
CSS
z-index:10;
Higher value appears on top.
37. Overflow
CSS
overflow:hidden;

overflow:scroll;

overflow:auto;
38. Complete Login Form Example
HTML
HTML
<form>

<h2>Login</h2>

<input type="text"
placeholder="Username">

<input type="password"
placeholder="Password">

<button>
Login
</button>

</form>
CSS
CSS
form{

width:300px;

padding:20px;

margin:auto;

border:1px solid gray;

}

input{

width:100%;

margin:10px 0;

padding:10px;

}

button{

width:100%;

padding:10px;

background:blue;

color:white;

}
Important Interview Topics
HTML
Semantic HTML
Forms and Validation
Tables
Lists
Audio & Video
Local Storage
Session Storage
Meta Tags
CSS
Box Model
Selectors
Specificity
Positioning
Flexbox
Grid
Responsive Design
Media Queries
Animations
Transitions
Pseudo Classes
Z-Index