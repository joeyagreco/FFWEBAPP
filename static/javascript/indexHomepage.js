function checkCharacterLimit() {
    // this function simply prevents the user from entering a league id that has more than 6 digits
    var leagueIdForm = document.getElementById("league_id");
    if(leagueIdForm.value.length > 6) {
        leagueIdForm.value = leagueIdForm.value.slice(0,6);
    }
}