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
    // var slider5 = document.getElementById("fairB").value;
    var slider6 = document.getElementById("dignity").value;
    var attention_check_yes = document.getElementById("id_Attention_2-0");
    var attention_check_no = document.getElementById("id_Attention_2-1");
    // IF ALL OF THE SLIDER VALUES ARE GREATER THAN 0.9 THEN THE USER IS NOT PAYING ATTENTION
    if (slider1 > 0.9 && slider2 > 0.9 && slider3 > 0.9 && slider4 > 0.9  && slider6 > 0.9 && slider7 > 0.9){
      attention_check_yes.click();
    } 
    else {
      attention_check_no.click();
    }
    document.getElementById("submit_button").click();
  }
  // if this is the SOB question then check if the two fields are filled
  else if (SOB){
    let vignette = js_vars.vignette;
    inputField  = "id_" + vignette + "_beliefs";
    var inputFieldVal = document.getElementById(inputField).value

    // check if the input field is empty
    if (inputFieldVal == "") {
      var targetDiv = document.getElementById("alert-move-sliders");
      move_to_alert(targetDiv)
    }
    else{
      document.getElementById("submit_button").click();
    }
    

    if (inputFieldVal == ""){
      var targetDiv = document.getElementById("alert-move-sliders");
      move_to_alert(targetDiv)
    }
    else{
      // hide the ban div
      ban_div.style.display = "none";
          
      // Remove the hidden class from all the elements that are hidden and add the hidden class to the ban container
      var initiallyHidden = document.querySelectorAll('.hidden'); // Get all the elements that are hidden
      initiallyHidden.forEach(function(element) {
        element.classList.remove('hidden');});
        }



  }
  // if this is a standard round, check if the sliders have been moved.
  else{
    let vignette = js_vars.vignette;
    var slider1 = document.getElementById("id_" + vignette + "_exploit").value;
    var slider2 = document.getElementById("id_" + vignette + "_autonomy").value;
    var slider3 = document.getElementById("id_" + vignette + "_coercion").value;
    var slider4 = document.getElementById("id_" + vignette + "_fairA").value;
    var slider5 = document.getElementById("id_" + vignette + "_dignity").value;
    var slider6 = document.getElementById("id_" + vignette + "_harm").value;
    if (slider1 == "" || slider2 == "" || slider3 == "" || slider4 == "" ||
        slider5 == "" || slider6 == ""){
            // get the alert div and display it              
            var targetDiv = document.getElementById("alert-move-sliders");
            move_to_alert(targetDiv)
    }
    else{
      document.getElementById("true_next_button").click();
      console.log('submit')
    }
  }
}

function next_button_2(){
    let vignette = js_vars.vignette;
    var slider1 = document.getElementById("id_" + vignette + "_imagined_health").value;
    var slider2 = document.getElementById("id_" + vignette + "_imagined_price").value;
    var targetDiv = document.getElementById("alert-move-sliders");
    var targetDiv_2 = document.getElementById("alert-move-sliders_2");
    if (slider1 == "" || slider2 == ""){
            // get the alert div and display it              
            move_to_alert(targetDiv)
    } else if (isNaN(slider2)) {
      move_to_alert(targetDiv_2)
      console.log("slider2 contains non-numeric characters");
    }
    else {
      document.getElementById("true_next_button").click();
      console.log('submit');
    }
    }



function next_button_3(){
    let vignette = js_vars.vignette;
    var slider1 = document.querySelector('input[name="scenario_directionality_1_ban"]:checked');
    var slider2 = document.querySelector('input[name="scenario_directionality_2_ban"]:checked');
    var slider3 = document.getElementById("id_scenario_directionality_1_realism").value;
    var slider4 = document.getElementById("id_scenario_directionality_2_realism").value;
    
    var slider5 = document.getElementById("id_scenario_directionality_1_realism_free_text").value;
    var slider6 = document.getElementById("id_scenario_directionality_2_realism_free_text").value;
    
    

    if (slider1 == "" || slider2 == "", slider3 == "" || slider4 == "", slider5 == "" || slider6 == ""){
            // get the alert div and display it              
            var targetDiv = document.getElementById("alert-move-sliders");
            move_to_alert(targetDiv)
    }
    else{
      document.getElementById("true_next_button").click();
      console.log('submit')
    }
}
function next_button_4(){
    let vignette = js_vars.vignette;
    var slider1 = document.querySelector('input[name="scenario_donation_1_ban"]:checked');
    var slider2 = document.querySelector('input[name="scenario_donation_2_ban"]:checked');
    var slider3 = document.getElementById("id_scenario_donation_1_realism").value;
    var slider4 = document.getElementById("id_scenario_donation_2_realism").value;

    

    if (slider1 == "" || slider2 == "", slider3 == "" || slider4 == "" ){
            // get the alert div and display it              
            var targetDiv = document.getElementById("alert-move-sliders");
            move_to_alert(targetDiv)
    }
    else{
      document.getElementById("true_next_button").click();
      console.log('submit')
    }
}

// For redirecting to the completion page
function Completion_button(href) {
  window.open(href, "_blank");
}

function sliderChange(dimension, attention_check=false){
  let vignette = js_vars.vignette;
  val = dimension.value;
  if (attention_check==false){
      var inputFieldId = "id_" + vignette + "_" + dimension.id;

    var inputField = document.getElementById(inputFieldId);
    inputField.value = val;
  }
  else{
    var slider1 = document.getElementById("exploit").value;
    var slider2 = document.getElementById("autonomy").value;
    var slider3 = document.getElementById("coercion").value;
    var slider4 = document.getElementById("fairA").value;
    var slider6 = document.getElementById("dignity").value;
    var attention_check_yes = document.getElementById("id_Attention_2-0");
    var attention_check_no = document.getElementById("id_Attention_2-1");
    // IF ALL OF THE SLIDER VALUES ARE GREATER THAN 0.9 THEN THE USER IS NOT PAYING ATTENTION
    if (slider1 > 0.9 && slider2 > 0.9 && slider3 > 0.9 && slider4 > 0.9  && slider6 > 0.9 ){
      attention_check_yes.click();
    } 
    else {
      attention_check_no.click();
    }


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
            labels[i].classList.add("bold-label");
            break;
        }
    }
}

function sliderChange_2(dimension){
  val = dimension.value;

  var inputFieldId = "id_" + dimension.id.replace(/_slider$/, '');;

  var inputField = document.getElementById(inputFieldId);
  inputField.value = val;

  const labels = dimension.parentElement.querySelector(".slider-range-labels").querySelectorAll(".label");

  // Determine the position of the slider value
  const sliderValue = parseFloat(val);
  const thresholds = [-7, -2, 2, 4, 10]; // Adjust these thresholds as needed

    // Remove the "bold-label" class from all labels
    labels.forEach((label) => label.classList.remove("bold-label"));

    // Check which label's threshold the slider value falls under and add the "bold-label" class accordingly
    for (let i = 0; i < thresholds.length; i++) {
        if (sliderValue <= thresholds[i]) {
            labels[i].classList.add("bold-label");
            break;
        }
    }
}

function percentsliderChange(ban=false, dimension, attention_check=false){
  let vignette = js_vars.vignette;
  let current_vignette = js_vars.current_vignette;

  if (ban==true){
    var inputFieldId = "id_" + vignette + "_beliefs";
  }
  else {
    val = dimension.value;
    var inputFieldId = "id_" + vignette + "_" + dimension.id
}
  val=dimension.value;
  var inputField = document.getElementById(inputFieldId);
  inputField.value = val;

  // Determine the position of the slider value
  const sliderValue = parseFloat(val);
  // const thresholds = [-7.15, -4.3, -0.95, 0.95, 3.43, 6.7, 10]; // Adjust these thresholds as needed
  // get the element whose id is "version1answer" and set its value to the val
  displayVal = 'Your answer: ' + val + "% of participants will choose 'Yes'";
  
  if (attention_check==true){
    displayVal = 'Your answer: ' + val + "%";
  }

  tag = dimension.id + "_answer"
  document.getElementById(tag).textContent = displayVal;
}

// function ban_button(answer, SOB=false, next=true){
//   let vignette = js_vars.vignette;
  
//   if (SOB==true){
//     var formField = "id_SOB_" + vignette + "_ban";
//   }
//   else{
//     var formField = "id_" + vignette + "_ban";
//   }

//   // if answer equals yes input one
//   if (answer == 1){
//     document.getElementById(formField).value = 1;
//   }
//   else if (answer == 0){
//     document.getElementById(formField).value = 0;
//   }

//   if (next==true){
//     document.getElementById("NextButton").click();
//   }
//   else{

//   var initiallyHidden = document.querySelectorAll('.hidden'); // Get all the elements that are hidden
//   var banContainer = document.querySelector('.ban-container'); // Get the container that holds the ban button
//   // Remove the hidden class from all the elements that are hidden and add the hidden class to the ban container
//   initiallyHidden.forEach(function(element) {
//     element.classList.remove('hidden');});
//   banContainer.classList.add('hidden');
// }
// }