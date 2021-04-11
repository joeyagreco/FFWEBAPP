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

function getNumberOfRowsToShow() {
    // this returns the number of teams in the league OR 10 (default), whichever is more.
    var numberOfRows = 10;
    var numberOfTeamsInLeague = document.getElementById("number_of_teams").value;
    if(numberOfTeamsInLeague > numberOfRows) {
        numberOfRows = numberOfTeamsInLeague;
    }
    return numberOfRows;
}

function initializeTable() {
    $(document).ready( function () {
        $('#statsTable').DataTable(
            {
                "order": [[ getIndexOfColumnToSort(), "desc" ]],
                "searching": false,
                "iDisplayLength": getNumberOfRowsToShow(),
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
}