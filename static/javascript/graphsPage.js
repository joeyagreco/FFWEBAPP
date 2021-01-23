function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    window.location = "/graph?league_id="+leagueId+"&graph_selection="+graphName;