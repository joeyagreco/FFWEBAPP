function homeRedirect() {
    Swal.fire({
      title: 'Leave your league?',
      html: "You should <a onclick='leagueHomepageRedirect()' href='#' style='color: black;'> save your league URL</a> first.",
      icon: 'warning',
      iconColor: '#bf1d43',
      showCancelButton: true,
      confirmButtonColor: '#40916C',
      cancelButtonColor: '#bf1d43',
      confirmButtonText: 'Yes, leave!',
      heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
         window.location = "/";
         }
    })
}

function leagueHomepageRedirect() {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    window.location = "/league-homepage?league_id=" + leagueId;
}

function statExplanationRedirect() {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    window.location = "/stats-explained?league_id=" + leagueId;
}

function aboutRedirect() {
    var leagueId = document.getElementById("league_id").value;
    startLoading();
    window.location = "/about?league_id=" + leagueId;
}

function startLoading() {
    document.querySelector("#loader-wrapper").style.display = "flex";
    document.querySelector("#loader-wrapper").style.visibility = "visible";
}

function stopLoading() {
    document.querySelector("#loader-wrapper").style.display = "none";
    document.querySelector("#loader-wrapper").style.visibility = "hidden";
    document.querySelector("body").style.visibility = "visible";
}

document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        startLoading();
    } else {
        stopLoading();
    }
}