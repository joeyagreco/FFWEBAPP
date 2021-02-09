function homeRedirect() {
    Swal.fire({
      title: 'Leave your league?',
      html: "You should <a onclick='leagueHomepageRedirect()' href='#'> save your league URL</a> first.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
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
    window.location = "/league-homepage?league_id=" + leagueId;
}

function statExplanationRedirect() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/stats-explained?league_id=" + leagueId;
}