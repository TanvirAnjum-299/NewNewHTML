// Function with parameters
function calculateParameter(length, width) {
  return length * width;
}

// Function that asks user for input
function askDimensions() {
  // Prompt user for length and width
  let length = prompt("What is the length?");
  let width = prompt("What is the width?");

  // Convert to numbers
  length = parseFloat(length);
  width = parseFloat(width);

  // Call function with parameters
  let area = calculateParameter(length, width);

  // Show result on page
  document.getElementById("output").innerText =
    "The area of the rectangle is: " + parameter;
}
