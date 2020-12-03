function homeRedirect() {
    window.location = "/";
}

function leagueHomepageRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/league-homepage?league_id=" + leagueId;
}