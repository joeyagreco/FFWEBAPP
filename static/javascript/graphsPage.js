function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    window.location = "/graphs?league_id="+leagueId+"&graph_selection="+graphName;
}

function testInject() {
    var injectDiv = '<div> <div id="758c7e19-d0c8-4645-be3c-a71d675c0ed7" class="plotly-graph-div" style="height:100%; width:100%;">';
//    var injectDiv = document.getElementById("graphDiv");
    document.getElementById("generatedGraph").innerHTML += injectDiv;
}
