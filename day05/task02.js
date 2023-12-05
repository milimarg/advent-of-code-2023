const fs = require('fs');
const input = fs.readFileSync("./input.txt", "utf8").split("\n");
const {checkLine} = require("./utils");

const MAX_STEPS = 7;
let a = 0;
const seeds = input[0].replace("seeds: ", "").split(" ").map(value => parseInt(value)).filter(x => !isNaN(x));
const steps = [];
let stepsPart = [];
const samples = [];

for (let i = 0; i < seeds.length; i += 2) {
    samples.push({"start": seeds[i], "rangeProp": seeds[i + 1]});
}

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

const reprocessSeed = (seedRange, step) => {
    const convertedRanges = []
    step.forEach((stepLine) => {
        const stepLineEnd = stepLine.src + stepLine.range;
        if (seedRange.start < stepLineEnd && seedRange.start + seedRange.rangeProp > stepLine.src) {
            const rangeStart = Math.max(seedRange.start, stepLine.src);
            const rangeEnd = Math.min(seedRange.start + seedRange.rangeProp, stepLineEnd);
            const convertedStart = stepLine.dest + (rangeStart - stepLine.src);
            convertedRanges.push({start: convertedStart, rangeProp: rangeEnd - rangeStart});
        }
    });
    return convertedRanges.length > 0 ? convertedRanges : [{start: seedRange.start, rangeProp: seedRange.rangeProp}];
}

const getLocationsOfSeed = (sample, steps) => {
    let currentRanges = [sample];

    steps.forEach(step => {
        let processedRanges = [];
        currentRanges.forEach((seedRange) => {
            processedRanges = processedRanges.concat(reprocessSeed(seedRange, step));
        });
        currentRanges = processedRanges;
    });
    return currentRanges;
}

let lowestLocationOfAllTimeYesIBecameCrazyBecauseOfThatExercise = Number.MAX_SAFE_INTEGER;

samples.forEach(sample => {
    const locations = getLocationsOfSeed(sample, steps);

    const minimumLocation = Math.min(...locations.map(x => x.start));

    if (minimumLocation < lowestLocationOfAllTimeYesIBecameCrazyBecauseOfThatExercise) {
        lowestLocationOfAllTimeYesIBecameCrazyBecauseOfThatExercise = minimumLocation;
    }
});

console.log("nearest location", lowestLocationOfAllTimeYesIBecameCrazyBecauseOfThatExercise);
