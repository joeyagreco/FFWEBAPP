function makeLeagueAveragesSquareCss() {
    // makes the height = width on all .averageBlock divs
    var allAverageBlocks = document.getElementsByClassName("averageBlock");
    var stylingInfo = allAverageBlocks[0].getBoundingClientRect();
    for(i=0; i<allAverageBlocks.length; i++) {
        allAverageBlocks[i].style.height = stylingInfo.width + "px";
        console.log(allAverageBlocks[i].style.height);
    }
}