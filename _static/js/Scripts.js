// When the user clicks the button, open the modal.
function button_click(index, keepTrack = false) {
  var modal = document.getElementById("myModal" + index);
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function span_click(index){
  document.getElementById("myModal" + index).style.display = "none";
}

function next_button(check_attention = false){
  // If this is an attention check
  if (check_attention){
    var slider1 = document.getElementById("exploit").value;
    var slider2 = document.getElementById("autonomy").value;
    var slider3 = document.getElementById("coercion").value;
    var slider4 = document.getElementById("fairA").value;
    var slider5 = document.getElementById("fairB").value;
    var slider6 = document.getElementById("dignity").value;
    var slider7 = document.getElementById("ban").value;

    var attention_check_yes = document.getElementById("id_Attention_2-0");
    var attention_check_no = document.getElementById("id_Attention_2-1");
    // IF ALL OF THE SLIDER VALUES ARE GREATER THAN 0.9 THEN THE USER IS NOT PAYING ATTENTION
    if (slider1 > 0.9 && slider2 > 0.9 && slider3 > 0.9 && slider4 > 0.9 && slider5 > 0.9 && slider6 > 0.9 && slider7 > 0.9){
      attention_check_yes.click();
    } 
    else {
      attention_check_no.click();
    }
    document.getElementById("submit_button").click();
  }
  // if this is a standard round, check if the sliders have been moved.
  else{
    let vignette = js_vars.vignette;
    // TODO: add code to save the result of the ban choice to the formfield.
    var slider1 = document.getElementById("id_" + vignette + "_exploit").value;
    var slider2 = document.getElementById("id_" + vignette + "_autonomy").value;
    var slider3 = document.getElementById("id_" + vignette + "_coercion").value;
    var slider4 = document.getElementById("id_" + vignette + "_fairA").value;
    var slider5 = document.getElementById("id_" + vignette + "_fairB").value;
    var slider6 = document.getElementById("id_" + vignette + "_dignity").value;
    var slider7 = document.getElementById("id_" + vignette + "_ban").value;
    if (slider1 == "" || slider2 == "" || slider3 == "" || slider4 == "" ||
     slider5 == "" || slider6 == "" || slider7 == ""){
        alert("Please answer all questions to continue. All the sliders need to be moved slightly to register a response.");
    }
    else{
      document.getElementById("submit_button").click();
    }
  }
}

// For redirecting to the completion page
function Completion_button(href) {
  window.open(href, "_blank");
}

function sliderChange(dimension){
  let vignette = js_vars.vignette;
  val = dimension.value;
  var inputFieldId = "id_" + vignette + "_" + dimension.id;
  var inputField = document.getElementById(inputFieldId);
  inputField.value = val;

  const labels = dimension.parentElement.querySelector(".slider-range-labels").querySelectorAll(".label");

  // Determine the position of the slider value
  const sliderValue = parseFloat(val);
  const thresholds = [-7.15, -4.3, -0.95, 0.95, 3.43, 6.7, 10]; // Adjust these thresholds as needed

    // Remove the "bold-label" class from all labels
    labels.forEach((label) => label.classList.remove("bold-label"));

    // Check which label's threshold the slider value falls under and add the "bold-label" class accordingly
    for (let i = 0; i < thresholds.length; i++) {
        if (sliderValue <= thresholds[i]) {
            console.log(sliderValue,thresholds[i]);
            labels[i].classList.add("bold-label");
            break;
        }
    }
}