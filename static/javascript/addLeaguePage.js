function setNumberOfTeams(numOfTeams) {
    var newTeamElement = document.getElementById(numOfTeams+"teams");
    var activeElement = document.getElementsByClassName("active")[0];
    // make the selected element have the active class and take it from the old active element
    newTeamElement.classList.add("active");
    activeElement.classList.remove("active");
    // make the button that holds the display value show the value of our given number of Teams
    var displayButtonElement = document.getElementById("number_of_teams");
    displayButtonElement.innerHTML = numOfTeams + " Teams";
    displayButtonElement.value = numOfTeams;
}

function postNewLeague() {
    // get all the values we need for this new league and put into a dictionary
    var leagueName = document.getElementById("league_name").value;
    // check if league name is valid before submitting
    error = isInvalidLeagueName(leagueName);
    if(error) {
        // send back with error message
        window.location = "/new-league?error_message="+error;
        return;
    }
    var numOfTeams = document.getElementById("number_of_teams").value;
    var data = {"league_name": leagueName, "number_of_teams": numOfTeams};
    // send POST request
    var fetchPromise = post("/add-league", data);
    // redirect
    fetchPromise.then(response => {
      window.location.href = response.url;
    });
}

function isInvalidLeagueName(leagueName) {
    // check if it is blank
    if (leagueName.replaceAll(/\s/g,'').length == 0) {
        return "League name must have at least 1 valid character.";
    }
    // check if it is over 30 characters
    if (leagueName.length > 30) {
        return "League name must be less than 30 characters.";
    }
    return false;
}

// method for sending POST requests
window.post = function(url, data) {
    return fetch(url, {method: "POST", body: JSON.stringify(data)});
}

function activateSubmitButton() {
    // this activates the submit button if the league name field isn't empty
    var leagueNameInputElement = document.getElementById("league_name");
    var submitLeagueButton = document.getElementById("createLeagueButton");
    if(leagueNameInputElement.value.replaceAll(/\s/g,'').length != 0) {
        // valid league name given, enable submit button
        submitLeagueButton.classList.remove("disabled");
    }
    else {
        // check if submit button is disabled, if not, disable it again
        if(!submitLeagueButton.classList.contains("disabled")) {
            submitLeagueButton.classList.add("disabled");
        }
    }

}