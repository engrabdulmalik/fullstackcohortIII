// console.log(age)
var age = 2;
// var age2 = 2
// console.log(age == age2)

// console.log(age === age2)

//single alternative

// if(age > 1)
// {
//     console.log("Age is greater than 1")
// }

//double alternative

// if(age > 1)
// {
//     console.log("Age is greater than 1")
// }
// else
// {
//     console.log("Age is less than 1")
// }

// (age > 1) ? True: False;

// ternary operator
// if (typeof age === "number") {
//   age > 1
//     ? console.log("Age is greater than 1")
//     : console.log("Age is less than 1");
// } else {
//   console.log("Age is not defined or not a number");
// }

// switch case

// switch (age) {
//   case 1:
//     console.log("Age is 1");
//     break;
//   case 2:
//     console.log("Age is 2");
//     break;
//   default:
//     console.log("Age is not 1 or 2");
//     break;
// }

// multiple alternative using nested if else

if (age > 1 && age <= 2) {
  console.log("Age is greater than 1");
} else if (age == 2) {
  console.log("Age is less than 2");
} else {
  console.log("Age is not 1 or 2");
}
