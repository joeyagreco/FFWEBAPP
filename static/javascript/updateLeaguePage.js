function deleteLeague() {
    Swal.fire({
    title: 'Are you sure you want to delete your league?',
    text: "This cannot be undone.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete my league forever.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
            var leagueId = document.getElementById("league_id").value;
             window.location = "/delete-league?league_id="+leagueId;
         }
    })
}

function addUpdateWeeksRedirect() {
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("original_year_number").value;
    // GET request
     window.location = "/add-update-weeks?league_id="+leagueId+"&year="+year;
}

function getChangeCount() {
    return parseInt(sessionStorage["changeCount"]);
}

function clearChanges() {
    // this sets/resets the change count to 0
    sessionStorage["changeCount"] = "0";
}

function changeMade() {
    // when this method is called, it increments the changeCount by 1
    // it also enables the save button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.remove("disabled");
    var changeCount = getChangeCount();
    changeCount++;
    sessionStorage["changeCount"] = changeCount.toString();
}

function addYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;
    window.location = "/add-year?league_id="+leagueId+"&selected_year="+currentYear;
}

function deleteYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;

        Swal.fire({
    title: 'Are you sure you want to delete the ' + currentYear + ' year?',
    text: "This cannot be undone.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete the ' + currentYear + ' year.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
             window.location = "/delete-year?league_id="+leagueId+"&selected_year="+currentYear;
         }
    })
}

function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    // GET request
     window.location = "/update-league?league_id="+leagueId+"&year="+year;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function enableDeleteYearButton() {
    // this will enable the delete year button if there is more than 1 year in the given league (2 including year 0)
    document.getElementById("deleteYearButton").disabled = false;
}

function toggleYearEdit() {
    // this will toggle the year edit "bar" which includes an input form and the league delete button
    var yearEditBar = document.getElementById("yearEdit");
    if(window.getComputedStyle(yearEditBar).display === "none") {
        // year edit bar is currently hidden
        yearEditBar.style.display = "flex";
    }
    else {
        yearEditBar.style.display = "none";
    }
}

function preparePageForYearZero() {
    // this disables the add/update week button and the edit button.
    // it is used when the update league page is on the "all time" year [year 0]
    // first make the add/update week button not visible
    document.getElementById("addOrUpdateWeekButton").style.display = "none";
    // then disable the edit button
    document.getElementById("editYearButton").disabled = true;
}

function postLeagueChanges() {
    // get all the values we need and put them in a dictionary
    var leagueId = document.getElementById("league_id").value;
    var leagueName = document.getElementById("league_name").value;
    var originalYear = document.getElementById("selectYearButton").value;
    var newYear = document.getElementById("year_form").value;
    var numberOfTeams = document.getElementById("number_of_teams").value;
    // put all data into a dict
    data = {"league_id": leagueId,
            "league_name": leagueName,
            "year_number": newYear,
            "original_year_number": originalYear,
            "number_of_teams": numberOfTeams}
    // grab all team names and put them into the data dict
    for (i=1; i<=numberOfTeams; i++) {
        var teamName = document.getElementById("team_"+i).value;
        data["team_"+i] = teamName;
    }
    // validate data here
    var error = getErrorInData(data);
    if (error) {
        window.location = "/update-league?league_id="+leagueId+"&error_message="+error;
        return;
    }
    // send POST request
    var fetchPromise = fetch("/update-league", {method: "POST",
                                                headers: {"Content-Type": "application/json"},
                                                body: JSON.stringify(data)});
    // redirect
    fetchPromise.then(response => {
      window.location.href = response.url;
    });
}

function getErrorInData(data) {
    // this validates the dict about to be posted
    var numberOfTeams = document.getElementById("number_of_teams").value;
    if(data["league_name"].replaceAll(/\s/g,'').length == 0) {
        // check if the league name is empty
        return "League name cannot be empty.";
    }
    if(data["year_number"] != parseInt(data["year_number"], 10)) {
        // check if the year is an int
        return "Year must be an integer.";
    }
    if((data["year_number"] < 1920 && data["year_number"] != 0) || data["year_number"] >= 3000) {
        // check if the year is in a valid range
        return "Year must be in a valid range.";
    }
    // check team names
    for(i=1; i<=numberOfTeams; i++) {
        if(data["team_"+i].replaceAll(/\s/g,'').length == 0) {
            return "Team names cannot be empty."
        }
    }
    return "";
}

function getMaxTeamNameLength(teams) {
    var maxLength = 0;
    for(i=0; i<teams.length; i++) {
        var newLength = teams[i]["teamName"].length;
        if(newLength > maxLength) {
            maxLength = newLength;
        }
    }
    return maxLength;
}

function setTeamNameInputWidths(teams) {
    // get all team dropdown button elements
    width = getMaxTeamNameLength(teams);
    // add room for dropdown arrow
    width += 5;
    teamInputForms = document.getElementsByClassName("teamForm");
    console.logg
    for(i=0; i<teamInputForms.length; i++) {
        teamInputForms[i].setAttribute('style', 'width:'+width/2+'ch');
    }
}