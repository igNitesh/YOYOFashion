var form = document.getElementById("priceFilterForm");
// Get all the input fields within the form
var inputFields = form.querySelectorAll("input");
// form.action = window.location.href;
inputFields[0].checked = false

inputFields.forEach(function (input) {
  // checked_value += input.value
  if (input.type === "checkbox") {
    // Add event listener for "change" event
    input.addEventListener("change", function () {
      if (input.checked) {
        // input.value = checked_value
        form.submit(); // Submit the form
        console.log("submited..");
        console.log(input.value);
        form.reset();
      }
    });
  }
});



var colour_form = document.getElementById("colorFilterForm");
// Get all the input fields within the form
var colour_inputFields = colour_form.querySelectorAll("input");
console.log(colour_inputFields)
colour_inputFields[0].checked = false


colour_inputFields.forEach(function (input) {
  // checked_value += input.value
  if (input.type === "checkbox") {
    // Add event listener for "change" event
    input.addEventListener("change", function () {
      if (input.checked) {
        // input.value = checked_value
        colour_form.submit(); // Submit the form
        console.log("submited..");
        console.log(input.value);
        colour_form.reset();
      }
    });
  }
});


var sizeFilterForm = document.getElementById("sizeFilterForm");
// Get all the input fields within the form
var size_inputFields = sizeFilterForm.querySelectorAll("input");
console.log(colour_inputFields)
size_inputFields[0].checked = false


size_inputFields.forEach(function (input) {
  // checked_value += input.value
  if (input.type === "checkbox") {
    // Add event listener for "change" event
    input.addEventListener("change", function () {
      if (input.checked) {
        // input.value = checked_value
        sizeFilterForm.submit(); // Submit the form
        sizeFilterForm.reset();
      }
    });
  }
});
