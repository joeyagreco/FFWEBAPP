function deleteLeague() {
    // GET request
    leagueId = document.getElementById("league_id").value;
    if(confirm("Are you sure you want to delete your league?")){
        window.location = "/deleteleague?league_id="+leagueId;
    }
}

function successfulUpdatePopup() {
    alert("League Successfully Updated");
}