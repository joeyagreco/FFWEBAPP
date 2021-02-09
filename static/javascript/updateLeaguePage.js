function deleteLeague() {
    Swal.fire({
    title: 'Are you sure you want to delete your league?',
    text: "This cannot be undone.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete my league forever.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
            var leagueId = document.getElementById("league_id").value;
             window.location = "/delete-league?league_id="+leagueId;
         }
    })
}

function addUpdateWeeksRedirect() {
    var leagueId = document.getElementById("league_id").value;
    // GET request
     window.location = "/add-update-weeks?league_id="+leagueId;
}