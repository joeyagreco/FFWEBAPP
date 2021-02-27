function submitLeagueStat(year, leagueStat) {
    var leagueId = document.getElementById("league_id").value;
    if(!year) {
        year = document.getElementById("select_year_button").value;
    }
    if(!leagueStat) {
        leagueStat = document.getElementById("stat_selection").value;
    }
    alert(year);
    window.location = "/league-stats?league_id="+leagueId+"&stat_selection="+leagueStat+"&year="+year;
}

function initializeTables() {
    $(document).ready( function () {
        $('#all_scores_table').DataTable();
    } );
    $(document).ready( function () {
        $('#margins_of_victory_table').DataTable();
    } );
}
