function sendRequest() {
    // Sends a post request to the server with the query string
    const xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "IP:SOMEPORT", false);
    xmlHttp.send(window.location.search);
}

function homePage() {
    // Loads the home page
    window.location.href = "index.html";
}

function nextPage() {
    // Gets the next year from the query string
    var index = window.location.search.indexOf("year=");
    const year = parseInt(window.location.search.substring(index + "year=".length, index + "year=".length + 4)) + 10;
    
    // If the year isn't the last
    if (year <= 2010) {
        // The matching year and images
        pairs = {
            "1980" : "code.jpg",
            "1990" : "www.png",
            "2000" : "connections.jpg",
            "2010" : "net.jpg"
        };
        
        // Send to the next page
        const image = pairs[year];
        window.location.href = `history.html?year=${year}&img=${image}`;
    }
}

window.onload = () => {
    // Gets the next year from the query string
    var index = window.location.search.indexOf("year=");
    const year = parseInt(window.location.search.substring(index + "year=".length, index + "year=".length + 4));
    
    // If the year is last
    if (year == 2010) {
        // Remove the next button
        const btn = document.getElementById("next");
        btn.parentNode.removeChild(btn);    
    }
};