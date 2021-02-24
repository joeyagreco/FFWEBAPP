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
    console.log(data);
    alert(data);
    // send POST request
    var fetchPromise = post("/update-league", data);
    // redirect
//    fetchPromise.then(response => {
//      window.location.href = response.url;
//    });
}

// method for sending POST requests
window.post = function(url, data) {
    return fetch(url, {method: "POST", body: JSON.stringify(data)});
}