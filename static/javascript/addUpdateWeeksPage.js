window.onload = function disableButtonsIfNecessary() {

    document.getElementById("delete_week_button").disabled = true;
}

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
    leagueId = document.getElementById("league_id").value;
    week = document.getElementById("select_week_dropdown").value;
    window.location = "/delete-week?league_id="+leagueId+"&week="+week;
}