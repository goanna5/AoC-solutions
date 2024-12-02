const { readFile } = require("fs");

function checkIncDec(line) {
  let setInc;
  let setDec;

  for (let j = 0; j < line.length; j++) {
    if (j + 1 < line.length && Number(line[j + 1]) < Number(line[j])) {
      setDec = true;
      // if its set increase already then bad
      if (setInc) {
        return false;
      }
    } else if (j + 1 < line.length && Number(line[j + 1]) > Number(line[j])) {
      setInc = true;
      // if its set decrease already then bad
      if (setDec) {
        return false;
      }
    }
    // check if at least one and at most three.
    let diff = Math.abs(Number(line[j + 1]) - Number(line[j]));
    if (j + 1 < line.length && (diff < 1 || diff > 3)) {
      return false;
    }

    // if gets to end and hasnt broken, all good, is safe
    if (j + 1 === line.length) {
      return true;
    }
  }
}

function removeAtIndex(line, index) {
  let newArr = [];
  for (let idx = 0; idx < line.length; idx++) {
    if (idx === index) {
      continue;
    }
    newArr.push(line[idx]);
  }
  return newArr;
}

function partOne(data) {
  // part 1
  let total = 0;
  const splitLines = data.toString().split("\n");

  for (let i = 0; i < splitLines.length; i++) {
    if (checkIncDec(splitLines[i].split(" "))) {
      total++;
    }
  }
  console.log(total);
}

function partTwo(data) {
  // part 2
  let total = 0;
  const splitLines = data.toString().split("\n");

  for (let i = 0; i < splitLines.length; i++) {
    let line = splitLines[i].split(" ");
    if (checkIncDec(line)) {
      total++;
    } else {
      // if it failed check while removing every number once
      for (let j = 0; j < line.length; j++) {
        if (checkIncDec(removeAtIndex(line, j))) {
          total++;
          break;
        }
      }
    }
  }
  console.log(total);
}

function main() {
  readFile("input2.txt", (err, data) => {
    if (err) throw err;
    partOne(data);
    partTwo(data);
  });
}
main();
