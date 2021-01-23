function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    window.location = "/graphs?league_id="+leagueId+"&graph_selection="+graphName;
}

function testInject() {
    var injectDiv = document.getElementById("graphDiv");
//    document.getElementById("generatedGraph").appendChild(injectDiv);
//    document.getElementById("generatedGraph").innerHTML += injectDiv;


    parentDiv = document.querySelector(".generatedGraph");
    parentDiv.appendChild(injectDiv);
}
