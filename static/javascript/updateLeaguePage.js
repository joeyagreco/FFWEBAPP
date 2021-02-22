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

function getChangeCount() {
    return parseInt(sessionStorage["changeCount"]);
}

function clearChanges() {
    // this sets/resets the change count to 0
    sessionStorage["changeCount"] = "0";
}

function changeMade() {
    // when this method is called, it increments the changeCount by 1
    // it also enables the save button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.remove("disabled");
    var changeCount = getChangeCount();
    changeCount++;
    sessionStorage["changeCount"] = changeCount.toString();
}

function addYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;
    window.location = "/add-year?league_id="+leagueId+"&selected_year="+currentYear;
}

function deleteYear() {
    var leagueId = document.getElementById("league_id").value;
    var currentYear = document.getElementById("original_year_number").value;
    window.location = "/delete-year?league_id="+leagueId+"&selected_year="+currentYear;
}

function yearRedirect(year) {
    var leagueId = document.getElementById("league_id").value;
    // GET request
     window.location = "/update-league?league_id="+leagueId+"&year="+year;
}