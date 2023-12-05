const fs = require('fs');
const input = fs.readFileSync("./input.txt", "utf8").split("\n");
const {checkLine, computeLocations} = require("./utils");

const MAX_STEPS = 7;
const seeds = input[0].replace("seeds: ", "").split(" ").map(value => parseInt(value)).filter(x => !isNaN(x));
const steps = [];
let stepsPart = [];
let a = 0;

input.forEach((line) => {
    const index = input.indexOf(line);
    if (index === 0) {
        return;
    }
    const array = checkLine(line);
    if (!array) {
        return;
    }
    if (array.length === 0) {
        if (!a) {
            a = 1;
            return;
        }
        steps.push([...stepsPart]);
        stepsPart = [];
    } else {
        stepsPart.push({dest: array[0], src: array[1], range: array[2]});
    }
});

if (steps.length !== MAX_STEPS) {
    steps.push([...stepsPart]);
}

const locations = computeLocations(seeds, steps);

console.log("nearest location", Math.min(...locations));
