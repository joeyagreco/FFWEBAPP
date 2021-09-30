function submitYearAndGraph(year, graphName) {
    var leagueId = document.getElementById("league_id").value;
    var screenWidth = window.innerWidth;
    if(!graphName) {
        // default to whatever the selected graph is
        graphName = document.getElementById("selected_graph_button").value;
    }
    if(year == null) {
        // default to whatever the selected year is
        year = document.getElementById("selectYearButton").value;
    }
    startLoading();
    window.location = "/graphs/" + leagueId + "/" + year + "?graph_selection="+graphName+"&screen_width="+screenWidth;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function isDiv(input) {
    return input.trim().substring(0, 5) == "<div>";
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
    // this injects the HTML code we have "waiting" in a div in our HTML into the proper div as HTML.
    // it first checks if the graph within the div should be resized, and generates a new one if so.
    var injectDiv = document.getElementById("graphDiv").innerHTML;
    injectDiv = htmlDecode(injectDiv);
    // TODO update calculation to not be hardcoded
    if(getWidthFromDivString(injectDiv) !=  parseInt(window.innerWidth/2, 10) && isDiv(injectDiv) && window.innerWidth > 414) {
        // width of given div does not match the screen size
        year = document.getElementById("selectYearButton").value;
        submitYearAndGraph(year, 0);
    }
    $('#generatedGraph').append(injectDiv);
}
