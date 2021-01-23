function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    window.location = "/graphs?league_id="+leagueId+"&graph_selection="+graphName;
}

/**
 * Convert a template string into HTML DOM nodes
 * @param  {String} str The template string
 * @return {Node}       The template HTML
 */
var stringToHTML = function (str) {
	var dom = document.createElement('div');
	dom.innerHTML = str;
	return dom;
};

function testInject() {
    var injectDiv = document.getElementById("graphDiv").innerHTML;
//    injectDiv = '<h1 style="color:purple">testing</h1>'
//    console.log(typeof injectDiv);
//    injectDiv = stringToHTML(injectDiv);
//    console.log(typeof injectDiv);
//    document.getElementById("generatedGraph").appendChild(injectDiv);

    document.getElementById("generatedGraph").innerHTML += injectDiv;

//    console.log(injectDiv);
//    parentDiv = document.getElementById("generatedGraph");
//    parentDiv.appendChild(injectDiv);
}
