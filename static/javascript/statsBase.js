function submitStat() {
    var leagueId = document.getElementById("league_id").value;
    var selectedStat = document.getElementById("stat_name").value;
    window.location = "/stats-explained?league_id="+leagueId+"&selected_stat="+selectedStat;
}