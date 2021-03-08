function submitLeagueStat(year, leagueStat) {
    var leagueId = document.getElementById("league_id").value;
    if(!year) {
        year = document.getElementById("select_year_button").value;
    }
    if(!leagueStat) {
        leagueStat = document.getElementById("stat_selection").value;
    }
    // check if the selected stat is an "ALWAYS ALL TIME" stat
    // TODO find a better way to do this
    if(leagueStat == "Owner Comparison") {
        year = 0;
    }
    window.location = "/league-stats?league_id="+leagueId+"&stat_selection="+leagueStat+"&year="+year;
}

function lockYearDropdownToAllTime() {
    var yearDropdownElement = document.getElementById("select_year_button");
    yearDropdownElement.disabled = true;
    yearDropdownElement.classList.add("disabled");
}

function initializeTables() {
    $(document).ready( function () {
        $('#all_scores_table').DataTable(
            {
                "order": [[ 0, "desc" ]]
            }
        );
    } );
    $(document).ready( function () {
        $('#margins_of_victory_table').DataTable(
            {
                "order": [[ 0, "desc" ]]
            }
        );
    } );
    $(document).ready( function () {
        $('#streaks_table').DataTable(
            {
                "order": [[ 0, "desc" ]]
            }
        );
    } );
        $(document).ready( function () {
        $('#owner_comparison_table').DataTable(
            {
                "order": [[ 4, "desc" ]]
            }
        );
    } );
}
