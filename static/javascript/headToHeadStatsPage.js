function yearRedirect(year, team1, team2) {
    var leagueId = document.getElementById("league_id").value;
    if(!team1) {
        var team1 = document.getElementById("team1button").value;
    }
    if(!team2) {
        var team2 = document.getElementById("team2button").value;
    }
    // GET request
     window.location = "/head-to-head-stats?league_id="+leagueId+"&team1="+team1+"&team2="+team2+"&year="+year;
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

function setTeamDropdownWidths(teams) {
    // get all team dropdown button elements
    width = getMaxTeamNameLength(teams);
    // add room for dropdown arrow
    width += 5;
    console.log(typeof width);
    teamDropdownButtons = document.getElementsByClassName("teamDropdownButton");
    for(i=0; i<teamDropdownButtons.length; i++) {
        teamDropdownButtons[i].setAttribute('style', 'width:'+width+'ch');
    }
}