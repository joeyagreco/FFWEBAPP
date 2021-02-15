function submitLeagueStat(pageNumber) {
    var leagueId = document.getElementById("league_id").value;
    var leagueStat = document.getElementById("league_stat").value;
    window.location = "/league-stats?league_id="+leagueId+"&stat_selection="+leagueStat;
}

function initializeTables() {
    $(document).ready( function () {
        $('#all_scores_table').DataTable();
    } );
    $(document).ready( function () {
        $('#margins_of_victory_table').DataTable();
    } );
}
