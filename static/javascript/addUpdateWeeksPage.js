function addWeek() {
    var leagueId = document.getElementById("league_id").value;
    window.location = "/add-week?league_id="+leagueId;
}

function updateWeekDropdown() {
    var leagueId = document.getElementById("league_id").value;
    var newWeek = document.getElementById("select_week_dropdown").value;
    window.location = "/add-update-weeks?league_id="+leagueId+"&week="+newWeek;
}

function deleteWeek() {
    var weekNumber = document.getElementById("select_week_dropdown").value;
    var leagueId = document.getElementById("league_id").value;

    Swal.fire({
    title: 'Are you sure you want to delete week ' + weekNumber + '?',
    text: "This cannot be undone.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete week ' + weekNumber + '.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
             window.location = "/delete-week?league_id="+leagueId+"&week="+weekNumber;
         }
    })
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