function postForm() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var name = document.getElementById("name_form").value;
    var email = document.getElementById("email_form").value || null;
    var feedback = document.getElementById("feedback_form").value;
    var postObject = {
    "appId": 1,
    "requestorName": name,
    "requestorEmail": email,
    "requestBody": feedback
    };
    var feedbackApiUrl = "http://feedback-service.live:3000/v1/feedback";
    postData(feedbackApiUrl, postObject)
      .then(response => {
        // see if we got a 200 status or not
        if(response.status != 200) {
            // unsuccessful POST, load feedback page with error message
            window.location = "/feedback?league_id="+leagueId+"&error_message="+"Can not submit feedback at this time.";
            return;
        }
        else {
            // successful post
              /* Alert success */
                Swal.fire({
                  icon: 'success',
                  iconColor: '#40916C',
                  title: 'Feedback Received',
                  text: 'Thank you!',
                  confirmButtonColor: '#40916C',
                  heightAuto: false
                }).then(function() {
                    window.location = "/feedback?league_id="+leagueId;
                });
        }
      });
}

// POST method
async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response; // parses JSON response into native JavaScript objects
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
