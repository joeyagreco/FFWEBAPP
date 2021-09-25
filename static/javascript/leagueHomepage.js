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
      iconColor: '#40916C',
      title: 'League URL Copied',
      text: 'Use it to get back here anytime!',
      confirmButtonColor: '#40916C',
      heightAuto: false
    })
}

function teamStatsRedirect() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    window.location = "/team-stats/" + leagueId + "/0";
}

function headToHeadStatsRedirect() {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    window.location = "/head-to-head-stats/" + leagueId + "/0";
}

function leagueStatsRedirect() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    window.location = "/league-stats/"+leagueId;
}

function updateLeagueRedirect() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    window.location = "/update-league/"+leagueId;
}

function graphsRedirect() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var screenWidth = window.innerWidth;
    window.location = "/graphs/" + leagueId + "/0?screen_width="+screenWidth;
}

function insertUrl() {
    var urlForm = document.getElementById("copyLeagueUrlForm");
    urlForm.value = window.location.href;
}

