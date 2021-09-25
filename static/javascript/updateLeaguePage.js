function deleteLeague() {
    Swal.fire({
    title: 'Are you sure you want to delete your league?',
    text: "This cannot be undone.",
    icon: 'warning',
    iconColor: '#bf1d43',
    showCancelButton: true,
    confirmButtonColor: '#bf1d43',
    cancelButtonColor: '#40916C',
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
    startLoading();
    // GET request
     window.location = "/add-update-weeks?league_id="+leagueId+"&year="+year;
}

function setOriginalValues() {
    // this saves the original values of everything on the page to sessionStorage
    sessionStorage["originalLeagueName"] = document.getElementById("league_name").value;
    sessionStorage["originalYearNumber"] = document.getElementById("year_form").value;
    sessionStorage["numberOfTeams"] = document.getElementById("number_of_teams").value;
    for(i=1; i<=sessionStorage["numberOfTeams"]; i++) {
        sessionStorage["originalTeamName"+i] = document.getElementById("team_"+i).value;
    }
}

function checkAndHandleIfChangeMade() {
    // this checks if a change was made and handles it accordingly
    if(sessionStorage["originalLeagueName"] != document.getElementById("league_name").value) {
        handleChangeMade();
        return;
    }
    if(sessionStorage["originalYearNumber"] != document.getElementById("year_form").value) {
        handleChangeMade();
        return;
    }
    for(i=1; i<=sessionStorage["numberOfTeams"]; i++) {
        if(sessionStorage["originalTeamName"+i] != document.getElementById("team_"+i).value) {
            handleChangeMade();
            return;
        }
    }
    undoChangeMade();
}

function getChangeCount() {
    return parseInt(sessionStorage["changeCount"]);
}

function clearChanges() {
    // this sets/resets the change count to 0
    sessionStorage["changeCount"] = "0";
}

function handleChangeMade() {
    // when this method is called, it increments the changeCount by 1
    // it also enables the save button
    // it also disables the edit year button
    // it also disables the year select dropdown button
    // it also disables the add year button
    // it also disables the add/update week button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.remove("disabled");
    saveButton.disabled = false;
    var changeCount = getChangeCount();
    changeCount++;
    sessionStorage["changeCount"] = changeCount.toString();
    var editYearButtonElement = document.getElementById("editYearButton");
    editYearButtonElement.classList.add("disabled");
    editYearButtonElement.disabled = true;
    var yearDropdownButtonElement = document.getElementById("selectYearButton");
    yearDropdownButtonElement.classList.add("disabled");
    yearDropdownButtonElement.disabled = true;
    var yearAddButtonElement = document.getElementById("addYearButton");
    yearAddButtonElement.classList.add("disabled");
    yearAddButtonElement.disabled = true;
    var addUpdateWeekButtonElement = document.getElementById("addOrUpdateWeekButton");
    addUpdateWeekButtonElement.classList.add("disabled");
    addUpdateWeekButtonElement.disabled = true;
}

function undoChangeMade() {
    // when this method is called, it sets the changeCount to 0
    // it also disables the save button
    // it also enables the edit year button
    // it also enables the year select dropdown button
    // it also enables the add year button
    // it also enables the add/update week button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.add("disabled");
    saveButton.disabled = true;
    clearChanges();
    var editYearButtonElement = document.getElementById("editYearButton");
    editYearButtonElement.classList.remove("disabled");
    editYearButtonElement.disabled = false;
    var yearDropdownButtonElement = document.getElementById("selectYearButton");
    yearDropdownButtonElement.classList.remove("disabled");
    yearDropdownButtonElement.disabled = false;
    var yearAddButtonElement = document.getElementById("addYearButton");
    yearAddButtonElement.classList.remove("disabled");
    yearAddButtonElement.disabled = false;
    var addUpdateWeekButtonElement = document.getElementById("addOrUpdateWeekButton");
    addUpdateWeekButtonElement.classList.remove("disabled");
    addUpdateWeekButtonElement.disabled = false;
}

function addYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;
    startLoading();
    window.location = "/add-year?league_id="+leagueId+"&selected_year="+currentYear;
}

function deleteYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;

        Swal.fire({
    title: 'Are you sure you want to delete the ' + currentYear + ' year?',
    text: "This cannot be undone.",
    icon: 'warning',
    iconColor: '#bf1d43',
    showCancelButton: true,
    confirmButtonColor: '#bf1d43',
    cancelButtonColor: '#40916C',
    confirmButtonText: 'Yes, delete the ' + currentYear + ' year.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
            startLoading();
            window.location = "/delete-year?league_id="+leagueId+"&selected_year="+currentYear;
         }
    })
}

function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    // GET request
     window.location = "/update-league/"+leagueId+"/"+year;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function enableDeleteYearButton() {
    // this will enable the delete year button if there is more than 1 year in the given league (2 including year 0)
    var deleteYearButtonElement = document.getElementById("deleteYearButton")
    deleteYearButtonElement.disabled = false;
    deleteYearButtonElement.classList.remove("disabled");
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
    startLoading();
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
    var width = getMaxTeamNameLength(teams);
    // add room for dropdown arrow
    var teamInputForms = document.getElementsByClassName("teamForm");
    for(i=0; i<teamInputForms.length; i++) {
        teamInputForms[i].setAttribute('style', 'width:'+width+'ch');
    }
}

function setLeagueNameInputWidth() {
    // get league name input element
    var leagueNameInputElement = document.getElementById("league_name");
    var leagueNameLength = leagueNameInputElement.value.length;
    var width = leagueNameLength;
    leagueNameInputElement.setAttribute('style', 'width:'+width+'ch')
}