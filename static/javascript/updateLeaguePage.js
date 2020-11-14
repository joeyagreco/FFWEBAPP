function deleteLeague() {
    // GET request
    leagueId = document.getElementById("league_id").value;
    if(confirm("Are you sure you want to delete your league?")){
        window.location = "/delete-league?league_id="+leagueId;
    }
}

function successfulUpdatePopup() {
    alert("League Successfully Updated");
}

function sendToUpdateWeeks() {
    // GET request
    leagueId = document.getElementById("league_id").value;
    window.location = "/add-update-weeks?league_id="+leagueId;

}