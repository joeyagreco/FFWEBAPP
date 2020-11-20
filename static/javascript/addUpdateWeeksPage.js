function addWeek() {
    leagueId = document.getElementById("league_id").value;
    window.location = "/add-week?league_id="+leagueId;
}

function updateWeekDropdown() {
    leagueId = document.getElementById("league_id").value;
    newWeek = document.getElementById("select_week_dropdown").value;
    window.location = "/add-update-weeks?league_id="+leagueId+"&week="+newWeek;
}

function deleteWeek() {
    alert("week deleted")
}