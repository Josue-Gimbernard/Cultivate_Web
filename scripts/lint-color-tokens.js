const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..", "static", "css");
const allowed = new Set([
  "#2A7D6F",
  "#1C5048",
  "#C4622D",
  "#E8F5F2",
  "#FDF6F0",
  "#E8F5E9",
  "#243A34",
  "#5F716B",
  "#D8E5DE",
  "#FFFFFF"
]);

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const target = path.join(dir, entry.name);
    return entry.isDirectory() ? walk(target) : [target];
  });
}

const violations = [];
for (const file of walk(root)) {
  const text = fs.readFileSync(file, "utf8");
  const matches = text.match(/#[0-9A-Fa-f]{6}/g) || [];
  for (const match of matches) {
    const upper = match.toUpperCase();
    if (!allowed.has(upper)) {
      violations.push(`${path.relative(process.cwd(), file)} uses ${match}`);
    }
  }
}

if (violations.length) {
  console.error(violations.join("\n"));
  process.exit(1);
}

console.log("Color token lint passed.");

