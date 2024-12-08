function calculate() {

    let num1 = parseFloat(prompt("Enter the first number:"));
    let num2 = parseFloat(prompt("Enter the second number:"));

 
    if (isNaN(num1) || isNaN(num2)) {
        console.log("Invalid input! Please enter valid numbers.");
        return;
    }


    let multiplication = num1 * num2;
    let division = num2 !== 0 ? num1 / num2 : "undefined (division by zero)";


    console.log(`Multiplication of ${num1} and ${num2} is: ${multiplication}`);
    console.log(`Division of ${num1} by ${num2} is: ${division}`);
}


calculate();
