function getHeadToHeadTable() {
    var leagueId = document.getElementById("league_id").value;
    var team1 = document.getElementById("team1Id").value;
    var team2 = document.getElementById("team2Id").value;
    window.location = "/head-to-head-stats?league_id="+leagueId+"&team1="+team1+"&team2="+team2;
}