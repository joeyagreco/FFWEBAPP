function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    window.location = "/graphs?league_id="+leagueId+"&graph_selection="+graphName;
}

function htmlDecode(input){
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function testInject() {
//alert("in js");
    var injectDiv = document.getElementById("graphDiv").innerHTML;
    $('#generatedGraph').append(htmlDecode(injectDiv));
}
