// Ex. 1
const array1 = [1,2,3,4];

let total1 = 0;

for (let x = 0; x < array1.length; x += 1) {
    total1 += array1[x]
}

console.log(total1);

// Ex. 2
const name2 = 'John';

const Greeting = `Hello, ${name2}!`;

console.log(Greeting);

//Ex. 3

const array2 = [];

function printEvenNumbers(n) {
    for (let x = 1;x <= n;x += 1) {
        if (x % 2 == 0){
            array2.push(x)
        }

    }
    console.log(`These numbers are even: ${array2}`);
}

printEvenNumbers(10);

// Ex. 4
// I don't know what continue does but if it stops the loop than the output is (0, 1)
//  if it skips the iteration the output is (0, 1, 3, 4)
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        continue;
    }
    console.log(i); // the output is (0, 1, 3, 4)
}

// Ex. 5

function checkAge(age) {
    if (age >= 18) {
        return "Adult"
    } else {
        return "Minor"
    }
}

console.log(checkAge(20)); // Output should be "Adult"
console.log(checkAge(16)); // Output should be "Minor"

// Ex. 6
let x = 10;
let y = '10';

if (x == y) {
    console.log("Equal"); // this is the output
} else {
    console.log("Not Equal");
}

if (x === y) {
    console.log("Strictly Equal");
} else {
    console.log("Not Strictly Equal"); // this is the output
}
// Ex. 7
function getDayName(dayNumber) {
    switch(dayNumber) {
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        default:
            return "Invalid day number"; // Added default case for invalid inputs
    }
}

console.log(getDayName(1)); // Output should be "Monday"
console.log(getDayName(7)); // Output should be "Sunday"
// Ex. 8
function reverseString(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}
// this function reverses a sting
//Ex.: 'hello' becomes 'olleh'
console.log(reverseString('hello')) // Output olleh