function successUpdatePopup() {
    window.alert("League Successfully updated");
}

function deleteLeague() {
    // GET request
    leagueId = document.getElementById("league_id").value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/deleteleague?league_id="+leagueId, false);
    xhttp.send();
}