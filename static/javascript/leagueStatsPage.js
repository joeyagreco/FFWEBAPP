function submitLeagueStat(pageNumber) {
    var leagueId = document.getElementById("league_id").value;
    var leagueStat = document.getElementById("league_stat").value;
    var pageNumber = getPageNumber(pageNumber);
    window.location = "/league-stats?league_id="+leagueId+"&stat_selection="+leagueStat+"&page_number="+pageNumber;
}

function getPageNumber(pageNumber) {
    // this returns the page number wanted by the user
    if(typeof pageNumber == 'number') {
        return pageNumber;
    }
    else if (pageNumber == "Next") {
        var nextPageNumber = parseInt(document.getElementById("current_page_number").innerHTML)+1;
        var maxAmountOfPages = parseInt(document.getElementById("number_of_pages_hidden").innerHTML);
        if(nextPageNumber > maxAmountOfPages) {
            return nextPageNumber-1;
        }
        return nextPageNumber;
    }
    else if (pageNumber == "Previous") {
        var previousPageNumber = parseInt(document.getElementById("current_page_number").innerHTML)-1;
        if(previousPageNumber < 1) {
            return previousPageNumber+1
        }
        return previousPageNumber;
    }
    else {
        console.log("error");
        return 1;
    }
}

// the below functions are unused and will be templates for applying/removing sorting in the future
function test() {
    var myClassSorted = document.getElementsByClassName("sorttable_sorted").length;
    var myClassSortedReverse = document.getElementsByClassName("sorttable_sorted_reverse").length;
    if(myClassSorted) {
        console.log("sorted");
    }
    else if(myClassSortedReverse) {
        console.log("sorted reverse")
    }
    else {
        console.log("not sorted");
    }
}

function reApplySorting() {
    var myClassSorted = document.getElementsByClassName("sorttable_sorted");
    if(myClassSorted.length) {
        console.log(myClassSorted);
        myClassSorted.item(0).classList.add("test");
    }
}
