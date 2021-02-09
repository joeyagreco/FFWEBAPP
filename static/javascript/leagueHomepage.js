function copyUrl() {
  /* Get the text field */
  var copyText = document.getElementById("copyLeagueUrlForm");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert success */
    Swal.fire({
      icon: 'success',
      title: 'League URL Copied',
      text: 'Use it to get back here anytime!',
      heightAuto: false
    })
}

function testStats() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/test-stats?league_id="+leagueId;
}

function teamStatsRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/team-stats?league_id="+leagueId;
}

function headToHeadStatsRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/head-to-head-stats?league_id="+leagueId;
}

function leagueStatsRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/league-stats?league_id="+leagueId;
}

function updateLeagueRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/update-league?league_id="+leagueId;
}

function graphsRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/graphs?league_id="+leagueId;
}

