JavaScript Complete Concepts Guide (with Definitions and Examples)
JavaScript is a high-level, interpreted programming language used to create interactive web applications. It runs in browsers and on servers using Node.js.
1. Variables
Variables store data values.
var
Function-scoped variable.
JavaScript
var name = "John";
console.log(name);
let
Block-scoped variable.
JavaScript
let age = 25;
console.log(age);
const
Cannot be reassigned.
JavaScript
const PI = 3.14;
console.log(PI);
2. Data Types
Primitive Data Types
String
JavaScript
let name = "Krishna";
Number
JavaScript
let age = 24;
let price = 99.99;
Boolean
JavaScript
let isLoggedIn = true;
Undefined
JavaScript
let x;
console.log(x);
Null
JavaScript
let data = null;
Symbol
JavaScript
let id = Symbol("id");
BigInt
JavaScript
let large = 12345678901234567890n;
3. Operators
Arithmetic Operators
JavaScript
let a = 10;
let b = 5;

console.log(a+b);
console.log(a-b);
console.log(a*b);
console.log(a/b);
console.log(a%b);
Comparison Operators
JavaScript
console.log(10 > 5);
console.log(10 == "10");
console.log(10 === "10");
Logical Operators
JavaScript
console.log(true && false);
console.log(true || false);
console.log(!true);
4. Conditional Statements
if
JavaScript
let age = 20;

if(age >= 18){
    console.log("Eligible");
}
if-else
JavaScript
if(age >= 18){
    console.log("Adult");
}
else{
    console.log("Minor");
}
else if
JavaScript
let marks = 80;

if(marks >= 90){
    console.log("A");
}
else if(marks >= 75){
    console.log("B");
}
else{
    console.log("C");
}
switch
JavaScript
let day = 1;

switch(day){
    case 1:
        console.log("Monday");
        break;
    default:
        console.log("Invalid");
}
5. Loops
for Loop
JavaScript
for(let i=1;i<=5;i++){
    console.log(i);
}
while Loop
JavaScript
let i = 1;

while(i<=5){
    console.log(i);
    i++;
}
do-while Loop
JavaScript
let i = 1;

do{
    console.log(i);
    i++;
}
while(i<=5);
6. Functions
Function is a reusable block of code.
Function Declaration
JavaScript
function greet(){
    console.log("Hello");
}

greet();
Function with Parameters
JavaScript
function add(a,b){
    return a+b;
}

console.log(add(5,3));
Arrow Function
JavaScript
const add = (a,b) => a+b;

console.log(add(10,20));
7. Arrays
Collection of values.
JavaScript
let fruits = ["Apple","Mango","Orange"];
Common Methods
JavaScript
fruits.push("Banana");
fruits.pop();
fruits.shift();
fruits.unshift("Grapes");
Loop Through Array
JavaScript
fruits.forEach(item=>{
    console.log(item);
});
8. Objects
Stores data in key-value pairs.
JavaScript
let person = {
    name:"Krishna",
    age:24
};

console.log(person.name);
9. String Methods
JavaScript
let text = "JavaScript";

console.log(text.length);
console.log(text.toUpperCase());
console.log(text.toLowerCase());
console.log(text.slice(0,4));
10. Array Methods
map()
JavaScript
let nums = [1,2,3];

let result = nums.map(n=>n*2);

console.log(result);
filter()
JavaScript
let nums = [10,20,30,40];

let result = nums.filter(n=>n>20);
reduce()
JavaScript
let nums = [1,2,3,4];

let sum = nums.reduce((a,b)=>a+b);

console.log(sum);
11. Scope
Global Scope
JavaScript
let name = "Krishna";
Function Scope
JavaScript
function test(){
    let age = 24;
}
Block Scope
JavaScript
if(true){
    let city = "Mysore";
}
12. DOM (Document Object Model)
Used to manipulate HTML elements.
Select Element
JavaScript
document.getElementById("demo");
Change Content
JavaScript
document.getElementById("demo").innerHTML="Hello";
Change Style
JavaScript
document.getElementById("demo").style.color="red";
13. Events
Button Click
JavaScript
button.addEventListener("click",function(){
    alert("Clicked");
});
14. ES6 Features
Template Literals
JavaScript
let name = "Krishna";

console.log(`Hello ${name}`);
Destructuring
JavaScript
let person = {
    name:"Krishna",
    age:24
};

let {name,age} = person;
Spread Operator
JavaScript
let arr1 = [1,2];
let arr2 = [...arr1,3,4];
15. Classes and OOP
Class
JavaScript
class Student{
    constructor(name){
        this.name = name;
    }

    display(){
        console.log(this.name);
    }
}

let s1 = new Student("Krishna");
s1.display();
Inheritance
JavaScript
class Animal{
    sound(){
        console.log("Animal Sound");
    }
}

class Dog extends Animal{
}

let d = new Dog();
d.sound();
16. Promises
Handle asynchronous operations.
JavaScript
let promise = new Promise((resolve,reject)=>{
    resolve("Success");
});

promise.then(result=>{
    console.log(result);
});
17. Async/Await
JavaScript
async function fetchData(){
    return "Data";
}

fetchData().then(console.log);
JavaScript
async function getData(){
    let result = await fetchData();
    console.log(result);
}
18. Error Handling
JavaScript
try{
    let x = y;
}
catch(error){
    console.log(error.message);
}
finally{
    console.log("Finished");
}
19. Local Storage
Store data in browser.
JavaScript
localStorage.setItem("name","Krishna");

let value = localStorage.getItem("name");

console.log(value);
20. JSON
Convert Object to JSON
JavaScript
let person = {
    name:"Krishna"
};

let json = JSON.stringify(person);
Convert JSON to Object
JavaScript
let obj = JSON.parse(json);
21. Fetch API
Used to call APIs.
JavaScript
fetch("https://api.example.com/users")
.then(response=>response.json())
.then(data=>console.log(data));
22. Closures
A function remembers variables from its outer scope.
JavaScript
function outer(){
    let count = 0;

    return function(){
        count++;
        console.log(count);
    };
}

let increment = outer();

increment();
increment();
23. Call, Apply, Bind
JavaScript
let person = {
    name:"Krishna"
};

function greet(city){
    console.log(this.name + city);
}

greet.call(person," Mysore");
24. Event Loop
JavaScript executes code using:
Call Stack
Web APIs
Callback Queue
Event Loop
Example:
JavaScript
console.log("Start");

setTimeout(()=>{
    console.log("Timeout");
},0);

console.log("End");
Output:
Plain text
Start
End
Timeout
25. Higher Order Functions
Functions that take functions as arguments.
JavaScript
function operation(a,b,callback){
    return callback(a,b);
}

function add(x,y){
    return x+y;
}

console.log(operation(5,3,add));
26. Modules
Export
JavaScript
export function add(a,b){
    return a+b;
}
Import
JavaScript
import {add} from "./app.js";
Real-World JavaScript Projects
Calculator
To-Do List
Weather App
E-Commerce Website
Chat Application
Expense Tracker
Student Management System
Online Quiz App
Banking Application
Social Media Dashboard
These 26 topics cover the core JavaScript syllabus from beginner to advanced level and are commonly asked in interviews for Frontend, Full-Stack, and JavaScript developer roles.