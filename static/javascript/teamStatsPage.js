function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    // GET request
     window.location = "/team-stats?league_id="+leagueId+"&year="+year;
}