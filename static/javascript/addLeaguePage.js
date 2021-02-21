function setNumberOfTeams(numOfTeams) {
    var newTeamElement = document.getElementById(numOfTeams+"teams");
    var activeElement = document.getElementsByClassName("active")[0];
    // make the selected element have the active class and take it from the old active element
    newTeamElement.classList.add("active");
    activeElement.classList.remove("active");
    // make the button that holds the display value show the value of our given number of Teams
    var displayButtonElement = document.getElementById("number_of_teams");
    displayButtonElement.innerHTML = numOfTeams + " Teams";
    displayButtonElement.value = numOfTeams;
}

function postNewLeague() {
    // get all the values we need for this new league and put into a dictionary
    var leagueName = document.getElementById("league_name").value;
    var numOfTeams = document.getElementById("number_of_teams").value;
    var data = {"league_name": leagueName, "number_of_teams": numOfTeams};
//    var data = "league_name="+leagueName"&number_of_teams="+numOfTeams;
    // send POST request
    post("/add-league", data);
}

// method for sending POST requests
window.post = function(url, data) {
    return fetch(url, {method: "POST", body: JSON.stringify(data)});
//    return fetch(url, {method: "POST", body: data});
}