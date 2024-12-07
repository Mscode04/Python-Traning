let num = 2;
for (let i = 1; i <= 4; i++) {
  let row = "";
  for (let j = 1; j <= i; j++) {
    row += num;
    if (j < i) {
      row += " ";
    }
    num++;
  }
  console.log(row);
}
