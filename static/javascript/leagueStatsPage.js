function submitLeagueStat() {
    var leagueId = document.getElementById("league_id").value;
    var leagueStat = document.getElementById("league_stat").value;
    var pageNumber = 2;
    window.location = "/league-stats?league_id="+leagueId+"&stat_selection="+leagueStat+"&page_number="+pageNumber;
}
