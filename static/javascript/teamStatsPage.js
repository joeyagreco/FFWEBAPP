function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    // GET request
     window.location = "/team-stats?league_id="+leagueId+"&year="+year;
}