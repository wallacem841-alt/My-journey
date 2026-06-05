function addnums(num1, num2){
    console.log(num1 + num2);
}

addnums(5,4);

function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Alice"); // Output: Hello, Alice!

function add(a, b) {
    return a + b;
}

let result = add(5, 3); 
console.log(result); // Output: 8

//Arrow Functions
const add1 = (a, b) => a + b;

console.log(add1(5, 3)); // Output: 8