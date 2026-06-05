// var(Global variable), let(variable), const(constant);

// always use const unless you're reasining it later;

let age = 29;

age = 31;

console.log(age);

const hello = 'Hello, world!';

const wifus = 'Shenhe, Rapi, Evelynn, Clara, Moikaloop';

const wifus1 = wifus.split(', ');

console.log(hello.length);
console.log(hello.toUpperCase());
console.log(hello.substring(0, 5));
console.log(wifus.split(', '));
console.log(wifus1);

// Arrays in JS == list in py;

wifus1.push('Android 18', 'Shylily');
console.log(wifus1);
console.log(wifus1.length)

for (let x = 0;x < wifus1.length; x += 1) {
    console.log(wifus1[x])
}

let number = 0;
while (number < wifus1.length) {
    console.log(wifus1[number]);
    number += 1
}

// Object literals

const Shenhe = {
    firstname: 'Shenhe',
    Height: 165.1,
    age1: 30,
    foods: ['Noodles', 'Lasanha']
}

console.log(Shenhe.foods[1]);

// if statments

const age2 = 18;

if (age2 < 13) {
  console.log("You're a child.");
} else if (age2 >= 13 && age < 20) {
  console.log("You're a teenager.");
} else {
  console.log("You're an adult.");
}

// switch - case

const fruit = "apple";

switch (fruit) {
  case "banana":
    console.log("This is a banana.");
    break;
  case "apple":
    console.log("This is an apple.");
    break;
  case "orange":
    console.log("This is an orange.");
    break;
  default:
    console.log("Unknown fruit.");
}

// || = or
// && = and
// ? = then (in python: x = "red" if toro else "blue" ) ex.:

const x = 10;

const color = x == 10 ? "red" : 'blue';

// switch - case inside of a function

function describeFruit(fruit) {
  switch (fruit) {
    case 'apple':
      return 'This is an apple.';
    case 'banana':
      return 'This is a banana.';
    default:
      return 'Unknown fruit.';
  }
}

console.log(describeFruit('apple')); // This is an apple.
console.log(describeFruit('banana')); // This is a banana.
console.log(describeFruit('cherry')); // Unknown fruit.

//Template literals
const name = 'John';
const greeting = `Hello, ${name}!`;
console.log(greeting); // Hello, John!

// Deconstructing

const [first, second] = wifus1;
console.log(first); // Shenhe
console.log(second); // Rapi

const { firstname, age1 } = Shenhe;
console.log(firstname); // Shenhe
console.log(age1); // 30

//Export/import

export const wifus2 = wifus1