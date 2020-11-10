function successUpdatePopup() {
    window.alert("League Successfully updated");
}

function deleteLeague() {
    // GET request
    leagueId = document.getElementById("league_id").value;
    //fetch("/deleteleague?league_id="+leagueId);
    window.location = "/deleteleague?league_id="+leagueId;
}