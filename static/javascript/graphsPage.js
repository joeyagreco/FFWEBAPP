function submitGraph() {
    var leagueId = document.getElementById("league_id").value;
    var graphName = document.getElementById("graph_name").value;
    var screenWidth = window.innerWidth;
    window.location = "/graphs?league_id="+leagueId+"&graph_selection="+graphName+"&screen_width="+screenWidth;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function getWidthFromDivString(divString) {
    // this retrieves the first "width" from the given string and returns the value of the width
    var i = divString.indexOf("width:");
    var valueIndex = i+6;
    var widthValueRaw = divString.substring(valueIndex, valueIndex+6);
    var indexOfPeriod = 0
    for (indexOfPeriod; indexOfPeriod < widthValueRaw.length; indexOfPeriod++) {
        if(widthValueRaw[indexOfPeriod] == ".") {
            break;
        }
    }
    return widthValueRaw.substring(0,indexOfPeriod);


}

function injectGraphAsDiv() {
    // TODO update calculation to not be hardcoded
    var injectDiv = document.getElementById("graphDiv").innerHTML;
    if(getWidthFromDivString(injectDiv) !=  parseInt(window.innerWidth/2, 10)) {
        // width of given div does not match the screen size
        submitGraph();
    }
    $('#generatedGraph').append(htmlDecode(injectDiv));
}
