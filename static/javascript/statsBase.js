function submitStat() {
    var leagueId = document.getElementById("league_id").value;
    var selectedStat = document.getElementById("stat_name").value;
    window.location = "/stats-explained?league_id="+leagueId+"&selected_stat="+selectedStat;
}

function reroute(statName) {
    var leagueId = document.getElementById("league_id").value;
    var selectedStat = statName;
    window.location = "/stats-explained?league_id="+leagueId+"&selected_stat="+selectedStat;
}

function htmlDecode(input) {
    // used to get rid of escape characters that have replaced needed HTML valid characters
    var e = document.createElement('div');
    e.innerHTML = input;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
}

function injectGraphAsDiv() {
    // this injects the HTML code we have "waiting" in a div in our HTML into the proper div as HTML.
    var injectDiv = document.getElementById("purposeDivHidden").innerHTML;
    injectDiv = htmlDecode(injectDiv);
    $('#purposeBody').append(injectDiv);
}