const { readFile } = require("fs");

function partOne(data) {
  // part 1
  const splitLines = data.toString().split("\n");
  const list1 = [];
  const list2 = [];
  splitLines.forEach((st) => {
    const split = st.split("   ");
    list1.push(Number(split[0]));
    list2.push(Number(split[1]));
  });

  // sort
  list1.sort();
  list2.sort();

  let finalSum = 0;

  for (let i = 0; i < list1.length; i++) {
    finalSum += Math.abs(list1[i] - list2[i]);
  }
  console.log(finalSum);
}

function partTwo(data) {
  // part 2
  const splitLines = data.toString().split("\n");
  const list1 = [];
  const list2 = [];
  const mapped = new Map();

  splitLines.forEach((st) => {
    const split = st.split("   ");
    list1.push(Number(split[0]));
    const numInListTwo = Number(split[1]);
    list2.push(numInListTwo);

    // if not in map add w frequency 1, else increment freq
    mapped.set(
      numInListTwo,
      mapped.has(numInListTwo) ? mapped.get(numInListTwo) + 1 : 1
    );
  });

  console.log(
    list1.reduce((total, num) => total + num * (mapped.get(num) || 0), 0)
  );
}

function main() {
  readFile("input1.txt", (err, data) => {
    if (err) throw err;
    partOne(data);
    partTwo(data);
  });
}
main();
