function postForm() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var name = document.getElementById("name_form").value;
    var email = document.getElementById("email_form").value;
    var feedback = document.getElementById("feedback_form").value;
    console.log(`League ID: ${leagueId}\nName: ${name.length}\nEmail: ${email}\nFeedback: ${feedback}`);
    // validate data
    var error = validateForms(name, email, feedback);
    if(error) {
        // load page with error
        window.location = "/feedback?league_id="+leagueId+"&error_message="+error;
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