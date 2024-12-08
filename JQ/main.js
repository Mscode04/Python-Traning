let currentDate = new Date();


let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];


let dayName = days[currentDate.getDay()];
let hours = currentDate.getHours();
let minutes = currentDate.getMinutes();
let seconds = currentDate.getSeconds();

// Format the time in AM/PM format
let period = hours >= 12 ? "PM" : "AM";
hours = hours % 12;
hours = hours ? hours : 12;
minutes = minutes < 10 ? "0" + minutes : minutes;
seconds = seconds < 10 ? "0" + seconds : seconds;


console.log(`Today is: ${dayName}.`);
console.log(`Current time is: ${hours} ${period} : ${minutes} : ${seconds}`);
