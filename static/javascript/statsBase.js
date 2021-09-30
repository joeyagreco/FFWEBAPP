function submitStat(stat) {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    window.location = "/stats-explained/"+leagueId+"?selected_stat="+stat;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function injectGraphAsDiv() {
    // this injects the HTML code we have "waiting" in a div in our HTML into the proper div as HTML.
    var purposeDiv = document.getElementById("purposeDivHidden").innerHTML;
    var formulaDiv = document.getElementById("formulaDivHidden").innerHTML;
    var formulaExplainedDiv = document.getElementById("formulaExplainedDivHidden").innerHTML;
    purposeDiv = htmlDecode(purposeDiv);
    formulaDiv = htmlDecode(formulaDiv);
    formulaExplainedDiv = htmlDecode(formulaExplainedDiv);
    $('#purposeBody').append(purposeDiv);
    $('#formulaBody').append(formulaDiv);
    $('#formulaExplainedBody').append(formulaExplainedDiv);
}