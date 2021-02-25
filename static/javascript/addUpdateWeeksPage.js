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
    // it also disables the add week button
    // it also disabled the week select dropdown
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.remove("disabled");
    saveButton.disabled = false;
    var addWeekButton = document.getElementById("addWeekButton");
    addWeekButton.classList.add("disabled");
    addWeekButton.disabled = true;
    var weekSelectButton = document.getElementById("dropdownMenuButton");
    weekSelectButton.classList.add("disabled");
    weekSelectButton.disabled = true;
    var changeCount = getChangeCount();
    changeCount++;
    sessionStorage["changeCount"] = changeCount.toString();
}

function makeActiveTeam(newTeamElement, newTeam, matchupId) {
    // this makes the given team active
    var activeClassName = "activeOdd";
    var teamAorB = "teamA";
    if(newTeamElement.classList.contains("evenTeam")) {
        activeClassName = "activeEven";
        teamAorB = "teamB"
    }
    var activeElement = document.getElementsByClassName(activeClassName)[0];
    // make the selected element have the active class and take it from the old active element
    newTeamElement.classList.add("active");
    newTeamElement.classList.add(activeClassName);
    activeElement.classList.remove("active");
    activeElement.classList.remove(activeClassName);
    // now update the display button
    var displayButtonElement = document.getElementsByClassName(teamAorB+"MatchupButton"+matchupId)[0];
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

function postWeek() {
    // this posts all needed info for the week
    var leagueId = document.getElementById("league_id").value;
    var weekNumber = document.getElementById("week_number").value;
    var yearNumber = document.getElementById("year_number").value;
    var numberOfTeams = document.getElementById("number_of_teams").value;

    data = {"league_id": leagueId,
            "week_number": weekNumber,
            "year_number": yearNumber};
    // add all the teams and scores
    for(i=1; i<=numberOfTeams/2; i++) {
        // add team
        data["teamAId_matchup_"+i] = document.getElementById("teamAId_matchup_"+i).value;
        data["teamBId_matchup_"+i] = document.getElementById("teamBId_matchup_"+i).value;
        // add scores
        data["teamAScore_matchup_"+i] = document.getElementById("teamAScore_matchup_"+i).value;
        data["teamBScore_matchup_"+i] = document.getElementById("teamBScore_matchup_"+i).value;
    }
    // validate data here
    var error = getErrorInData(data);
    if (error) {
        window.location = "/add-update-weeks?league_id="+leagueId+"&year="+yearNumber+"&error_message="+error;
        return;
    }
    // send POST request
    var fetchPromise = fetch("/update-week", {method: "POST",
                                                headers: {"Content-Type": "application/json"},
                                                body: JSON.stringify(data)});
    fetchPromise.then(response => {
        window.location.href = response.url;
    });
}

function getErrorInData(data) {
    // this validates the dict about to be posted
    var numberOfTeams = document.getElementById("number_of_teams").value;
    // check teams first
    var allTeamIds = [];
    var allTeamScores = [];
    for(i=1; i<=numberOfTeams/2; i++) {
        allTeamIds.push(data["teamAId_matchup_"+i]);
        allTeamIds.push(data["teamBId_matchup_"+i]);
        allTeamScores.push(data["teamAScore_matchup_"+i]);
        allTeamScores.push(data["teamBScore_matchup_"+i]);
    }
    var allTeamIdsSet = [...new Set(allTeamIds)]
    if(allTeamIds.length != allTeamIdsSet.length) {
        return "A teams must play once per week.";
    }
    for(i=0; i<allTeamScores.length; i++) {
        if(allTeamScores[i] == "") {
            return "All teams need a score.";
        }
    }
    return "";
}