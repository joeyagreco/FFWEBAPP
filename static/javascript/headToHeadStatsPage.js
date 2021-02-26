//function getHeadToHeadTable(team1, team2) {
//    var leagueId = document.getElementById("league_id").value;
//    var year = document.getElementById("selectYearButton").value;
//    window.location = "/head-to-head-stats?league_id="+leagueId+"&team1="+team1+"&team2="+team2+"&year="+year;
//}

function updateTeam1(team1) {
    var team2 = document.getElementById("team2button").value;
    getHeadToHeadTable(team1, team2);
}

function updateTeam2(team2) {
    var team1 = document.getElementById("team1button").value;
    getHeadToHeadTable(team1, team2);
}

function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    var team1 = document.getElementById("team1button").value;
    var team2 = document.getElementById("team2button").value;
    // GET request
     window.location = "/head-to-head-stats?league_id="+leagueId+"&team1="+team1+"&team2="+team2+"&year="+year;
}