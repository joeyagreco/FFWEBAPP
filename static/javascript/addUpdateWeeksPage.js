function addWeek() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/add-week?league_id="+leagueId;
}

function updateWeekDropdown() {
    var leagueId = document.getElementById("league_id").value;
    var newWeek = document.getElementById("select_week_dropdown").value;
    window.location = "/add-update-weeks?league_id="+leagueId+"&week="+newWeek;
}

function deleteWeek() {
    var leagueId = document.getElementById("league_id").value;
    var week = document.getElementById("select_week_dropdown").value;
    window.location = "/delete-week?league_id="+leagueId+"&week="+week;
}