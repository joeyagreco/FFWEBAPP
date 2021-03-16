function postForm() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var name = document.getElementById("name_form").value;
    var email = document.getElementById("email_form").value;
    var feedback = document.getElementById("feedback_form").value;
    console.log(`League ID: ${leagueId}\nName: ${name.length}\nEmail: ${email}\nFeedback: ${feedback}`);
    stopLoading();
}