function deleteLeague() {
    // GET request
    var leagueId = document.getElementById("league_id").value;
    if(confirm("Are you sure you want to delete your league?")){
        window.location = "/delete-league?league_id="+leagueId;
    }
}

function addUpdateWeeksRedirect() {
    // GET request
    var leagueId = document.getElementById("league_id").value;
    window.location = "/add-update-weeks?league_id="+leagueId;

}