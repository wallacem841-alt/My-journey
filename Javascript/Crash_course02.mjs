/*map()
The map() method creates a new array populated with the results of calling a provided 
function on every element in the calling array.
*/
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(number => number * 2); // this is a way to make a function
console.log(doubled); // [2, 4, 6, 8, 10]

/*filter()
The filter() method creates a new array with all elements that pass the test
implemented by the provided function.
*/
const even = numbers.filter(number => number % 2 === 0);
console.log(even); // [2, 4]

/*reduce()
The reduce() method executes a reducer function on each element of the array,
resulting in a single output value.
*/
const sum = numbers.reduce((total, number) => total + number, 0);
console.log(sum); // 15
/*
array.reduce((accumulator, currentValue) => {
  // operation on accumulator and currentValue
}, initialValue);
*/

/*forEach()
The forEach() method executes a provided function once for each array element.
*/
numbers.forEach(number => console.log(number * 2));
// Outputs: 2 4 6 8 10 (each on a new line)

//Export/import
//unlike in py, the module runs the intire code from Crash_course01.mjs 
import {wifus2} from "./Crash_course01.mjs";

console.log(wifus2)