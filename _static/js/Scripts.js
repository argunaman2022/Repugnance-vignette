// When the user clicks the button, open the modal.
function button_click(index, keepTrack = false) {
  var modal = document.getElementById("myModal" + index);
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function span_click(index){
  document.getElementById("myModal" + index).style.display = "none";
}

// moves the screen to the alert div and shakes it
function move_to_alert(targetDiv){
  targetDiv.style.display = "flex";
  // calculate its position and scroll to this alert
  var windowHeight = window.innerHeight;
  var divHeight = targetDiv.clientHeight;
  var divTopOffset = targetDiv.getBoundingClientRect().top;
  var scrollPosition = divTopOffset - (windowHeight - divHeight) / 2;

  window.scrollTo({
    top: scrollPosition,
    behavior: "smooth"
  });
  // Apply a shake animation class
  targetDiv.classList.add("shake");

  // Wait for a moment, then remove the shake class
  setTimeout(function () {
    targetDiv.classList.remove("shake");
  }, 500); // Adjust the time (in milliseconds) for the duration of the shake effect
}


function next_button(check_attention = false, SOB=false){
  // If this is an attention check
  if (check_attention){
    var slider1 = document.getElementById("exploit").value;
    var slider2 = document.getElementById("autonomy").value;
    var slider3 = document.getElementById("coercion").value;
    var slider4 = document.getElementById("fairA").value;
    var slider5 = document.getElementById("fairB").value;
    var slider6 = document.getElementById("dignity").value;

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
  // if this is the SOB question then check if the two fields are filled
  else if (SOB){
    let current_vignette = js_vars.current_vignette;
    field1 = 'id_' + current_vignette+'_equality' + '_SOB';
    field2 = 'id_' + current_vignette+'_inequality' + '_SOB';
    console.log(field2)
    var field1 = document.getElementById(field1).value;
    var field2 = document.getElementById(field2).value;
    console.log(field2)
    if (field1=='' || field2 ==''){
      var targetDiv = document.getElementById("alert-move-sliders");
      move_to_alert(targetDiv)
  }
    else{
      document.getElementById("submit_button").click();
    }
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
            // get the alert div and display it              
            var targetDiv = document.getElementById("alert-move-sliders");
            move_to_alert(targetDiv)
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

function sliderChange(dimension, attention_check=false){
  let vignette = js_vars.vignette;
  val = dimension.value;

  if (attention_check=false){
  var inputFieldId = "id_" + vignette + "_" + dimension.id;
  var inputField = document.getElementById(inputFieldId);
  inputField.value = val;
}
  const labels = dimension.parentElement.querySelector(".slider-range-labels").querySelectorAll(".label");

  // Determine the position of the slider value
  const sliderValue = parseFloat(val);
  const thresholds = [-8, -5, -2, 1, 4, 7, 10]; // Adjust these thresholds as needed

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

function percentsliderChange(dimension){
  let vignette = js_vars.current_vignette;
  val = dimension.value;
  // TODO: currently doesnt work because formfield isnt dynamic see init
  var inputFieldId = "id_" + vignette + "_" + dimension.id+'_SOB'; 
  var inputField = document.getElementById(inputFieldId);
  inputField.value = val;

  const labels = dimension.parentElement.querySelector(".slider-range-labels").querySelectorAll(".label");

  // Determine the position of the slider value
  const sliderValue = parseFloat(val);
  // const thresholds = [-7.15, -4.3, -0.95, 0.95, 3.43, 6.7, 10]; // Adjust these thresholds as needed
  // get the element whose id is "version1answer" and set its value to the val
  displayVal = 'Your answer: ' + val + "%";
  tag = dimension.id + "_answer"
  console.log(tag)
  document.getElementById(tag).textContent = displayVal;
}

function ban_button(answer){
  let vignette = js_vars.vignette;
  var formField = "id_" + vignette + "_ban";

  // if answer equals yes input one
  if (answer == 1){
    document.getElementById(formField).value = 1;
  }
  else if (answer == 0){
    document.getElementById(formField).value = 0;
  }

  var initiallyHidden = document.querySelectorAll('.hidden'); // Get all the elements that are hidden
  var banContainer = document.querySelector('.ban-container'); // Get the container that holds the ban button
  // Remove the hidden class from all the elements that are hidden and add the hidden class to the ban container
  initiallyHidden.forEach(function(element) {
    element.classList.remove('hidden');});
  banContainer.classList.add('hidden');
}