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