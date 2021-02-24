function addWeek() {
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("year_number").value;
    window.location = "/add-week?league_id="+leagueId+"&year_number="+year;
}

function updateWeekDropdown(weekNumber) {
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("year_number").value;
    window.location = "/add-update-weeks?league_id="+leagueId+"&week="+weekNumber+"&year="+year;
}

function deleteWeek() {
    var weekNumber = document.getElementById("week_number").value;
    var leagueId = document.getElementById("league_id").value;
    var yearNumber = document.getElementById("year_number").value;

    Swal.fire({
    title: 'Are you sure you want to delete week ' + weekNumber + '?',
    text: "This cannot be undone.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete week ' + weekNumber + '.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
             window.location = "/delete-week?league_id="+leagueId+"&week="+weekNumber+"&year="+yearNumber;
         }
    })
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

function makeActiveTeam(newTeam, matchupId) {
    // this makes the given team active
    var newTeamElement = document.getElementsByClassName("backgroundTeamId"+newTeam["teamId"])[0];
    var activeClassName = "activeOdd";
    var teamAorB = "teamA";
    if(newTeamElement.classList.contains("evenTeam")) {
        activeClassName = "activeEven";
        teamAorB = "teamB"
    }
    var activeElement = document.getElementsByClassName(activeClassName)[0];
    // make the selected element have the active class and take it from the old active element
    newTeamElement.classList.add("active");
    newTeamElement.classList.add("activeOdd");
    activeElement.classList.remove("active");
    activeElement.classList.remove("activeOdd");
    // now update the display button
    var displayButtonElement = document.getElementsByClassName("matchupButton"+matchupId)[0];
    displayButtonElement.innerHTML = newTeam["teamName"];
    displayButtonElement.value = newTeam["teamId"];
    // remove teamId styling class
    for(var i=displayButtonElement.classList.length-1; i>=0; i--) {
        var className = displayButtonElement.classList[i];
        if(className.startsWith("backgroundTeamId")) {
            displayButtonElement.classList.remove(className);
        }
    }
    displayButtonElement.classList.add("backgroundTeamId"+newTeam["teamId"]);
    // update the score input
    var scoreElement = document.getElementById(teamAorB+"Score_matchup_"+matchupId);
    // remove teamId styling class
    for(var i=scoreElement.classList.length-1; i>=0; i--) {
        var className = scoreElement.classList[i];
        if(className.startsWith("backgroundTeamId")) {
            scoreElement.classList.remove(className);
        }
    }
    scoreElement.classList.add("backgroundTeamId"+newTeam["teamId"]);
    // change id of score element
    scoreElement.id = teamAorB+"Score_matchup_"+matchupId;
    // mark this as a change
    changeMade();
}