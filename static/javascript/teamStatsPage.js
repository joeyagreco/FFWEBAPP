function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    // GET request
     window.location = "/team-stats?league_id="+leagueId+"&year="+year;
}

function getIndexOfColumnToSort() {
    // this returns the index for the column for Win Percentage
    var index = 4;
    var year = document.getElementById("selectYearButton").value;
    if(year == 0) {
        // win percentage is in the 5th index
        index = 5;
    }
    return index;
}

function initializeTable() {
    $(document).ready( function () {
        $('#statsTable').DataTable(
            {
                "order": [[ getIndexOfColumnToSort(), "desc" ]],
                "searching": false
            }
        );
    } );
}