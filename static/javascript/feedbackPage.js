function postForm() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var name = document.getElementById("name_form").value;
    var email = document.getElementById("email_form").value;
    var feedback = document.getElementById("feedback_form").value;
    console.log(`League ID: ${leagueId}\nName: ${name}\nEmail: ${email}\nFeedback: ${feedback}`);
    // validate data
    var error = validateForms(name, email, feedback);
    var errorMessageElement = document.getElementById("errorMessageFill");
    if(error) {
        // set error in page
//        window.location = "/feedback?league_id="+leagueId+"&error_message="+error;
        errorMessageElement.innerHTML = "- "+error+" -";
    }
    else {
        errorMessageElement.innerHTML = "";
    }
    stopLoading();
}

function validateForms(name, email, feedback) {
    // check name
    if(name.length == 0) {
        return "Name is required.";
    }
    // check email
    // nothing right now
    // check feedback
    if(feedback.length == 0) {
        return "Feedback is required."
    }
    return null;
}

function activateSubmitButton() {
    // this activates the submit button when forms are filled correctly
    // get all values
    var name = document.getElementById("name_form").value;
    var email = document.getElementById("email_form").value;
    var feedback = document.getElementById("feedback_form").value;

    // set booleans of whether or not these fields are valid
    var validName = isValidName(name);
    var validEmail = isValidEmail(email);
    var validFeedback = isValidFeedback(feedback);

    var submitButtonElement = document.getElementById("send_feedback_button");
    // check if all fields are valid
    if(validName && validEmail && validFeedback) {
        // activate submit button
        submitButtonElement.classList.remove("disabled");
    }
    else {
        // disable submit button
        submitButtonElement.classList.add("disabled");
    }
}

function isValidName(name) {
    //returns a boolean of whether or not the given name (string) is valid
    if(name.length == 0) {
        return false;
    }
    return true;
}

function isValidEmail(email) {
    //returns a boolean of whether or not the given email (string) is valid
    if(email.length == 0) {
        // email is not a required field, so it is valid if none is given
        return true;
    }
    if(email.substring(email.length-4, email.length+1) != ".com") {
        return false;
    }
    if(!email.includes("@")) {
        return false;
    }
    return true;
}

function isValidFeedback(feedback) {
    //returns a boolean of whether or not the given feedback (string) is valid
    if(feedback.length == 0) {
        return false;
    }
    return true;
}
