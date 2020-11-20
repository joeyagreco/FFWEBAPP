function addWeek() {
    console.log("in js function");
    leagueId = document.getElementById("league_id").value;
    window.location = "/add-week?league_id="+leagueId;
}