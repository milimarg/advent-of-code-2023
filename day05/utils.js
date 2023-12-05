function checkLine(line) {
    if (line.length === 0) {
        return;
    }
    if (line.includes("seeds:")) {
        line = line.split(":")[1];
    }
    return line.split(" ").map(x => parseInt(x)).filter(x => !isNaN(x));
}

function computeLocations(seeds, steps) {
    const locations = [];

    seeds.forEach((seed) => {
        let currentLocation = seed;
        steps.forEach(step => {
            for (let i = 0; i < step.length; i++) {
                if (currentLocation >= step[i].src && currentLocation <= step[i].src + step[i].range - 1) {
                    currentLocation = step[i].dest + (currentLocation - step[i].src);
                    break;
                }
            }
        })
        locations.push(currentLocation);
    });
    return locations;
}

module.exports = {checkLine, computeLocations};
