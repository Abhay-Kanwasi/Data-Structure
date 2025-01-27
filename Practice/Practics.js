// Write a program to create a dictionary and add, update, and delete key-value pairs.
const readline = require('readline');

const input = (question) => new Promise((resolve) => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.question(question, (answer) => {
    rl.close();
    resolve(answer);
  });
});

const dictionary_function = async () => {
  let dictionary = {};

  while (true) {
    const choice = await input(
      "Enter your choice (add/update/delete/show/exit): "
    );

    if (choice === "add") {
      const key = await input("Enter the key to add: ");
      dictionary[key] = await input("Enter the value to add: ");
      console.log("Key-value pair added successfully.");
    } else if (choice === "update") {
      const key = await input("Enter the key to update: ");
      if (dictionary.hasOwnProperty(key)) {
          dictionary[key] = await input("Enter the new value: ");
          console.log("Key-value pair updated successfully.");
      } else {
        console.log("Key not found in the dictionary.");
      }
    } else if (choice === "delete") {
      const key = await input("Enter the key to delete: ");
      if (dictionary.hasOwnProperty(key)) {
        delete dictionary[key];
        console.log("Key-value pair deleted successfully.");
      } else {
        console.log("Key not found in the dictionary.");
      }
    } else if (choice === "show") {
      console.log("Current Dictionary:", dictionary);
    } else if (choice === "exit") {
      console.log("Exiting program. Final Dictionary:", dictionary);
      break;
    } else {
      console.log("Invalid choice. Please try again.");
    }
  }
};

// dictionary_function();


// Accessing Methods
const fees = {
  abhay: 100, smay: 200, total: function () {
    return 100 + 200
  }
};
// console.log(fees.total())
// console.log(fees['abhay'])

// Private variables
var Mobile = function(model_no, sprice) {
  this.model_no = model_no;
  this.color = 'white';
  var price = 3000;
  this.sp = sprice;
  this.selling_price = function () {return (price)};
  var show = function () { return "Hello World" };
};

var Samsung = new Mobile('Galaxy', 2000);
var Nokia = new Mobile('3310', 1000);
console.log(Nokia.model_no)
console.log(Samsung.selling_price())