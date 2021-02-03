function homeRedirect() {
    window.location = "/";
}

function leagueHomepageRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/league-homepage?league_id=" + leagueId;
}

function statExplanationRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/stats-explained?league_id=" + leagueId;
}