function checkCharacterLimit() {
    // this function simply prevents the user from entering a league id that has more than 6 digits
    var leagueIdForm = document.getElementById("league_id");
    if(leagueIdForm.value.length > 6) {
        leagueIdForm.value = leagueIdForm.value.slice(0,6);
    }
}

function activateSubmitButton() {
    // this activates the submit button if the league name field isn't empty
    var leagueIdInputElement = document.getElementById("league_id");
    var loadLeagueButtonElement = document.getElementById("load_league_button");
    console.log(leagueIdInputElement.value.replaceAll(/\s/g,'').length);
    if(leagueIdInputElement.value.replaceAll(/\s/g,'').length == 5) {
        // valid league name given, enable submit button
        loadLeagueButtonElement.classList.remove("disabled");
    }
    else {
        console.log("disabled");
        // check if submit button is disabled, if not, disable it again
        if(!loadLeagueButtonElement.classList.contains("disabled")) {
            loadLeagueButtonElement.classList.add("disabled");
        }
    }
}