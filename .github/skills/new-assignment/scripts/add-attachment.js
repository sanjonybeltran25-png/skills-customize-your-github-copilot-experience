
const fs = require("fs");
const path = require("path");

const [assignmentId, displayName, filename, type] = process.argv.slice(2);
console.log(`Added "${displayName}" (${filename}) to assignment "${assignmentId}"`);