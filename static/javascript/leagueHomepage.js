function Copy() {
  var url = document.getElementById("league_id");
  url.value = window.location.href;
  url.focus();
  url.select();
  document.execCommand("Copy");
}

