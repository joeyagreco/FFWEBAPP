function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    // GET request
     window.location = "/team-stats?league_id="+leagueId+"&year="+year;
}

function initializeTable() {
    $(document).ready( function () {
        $('#statsTable').DataTable(
            {
                "order": [[ 4, "desc" ]]
            }
        );
    } );
}