$("#search_request").on('click', function () {

    var search_input = $("#search_input").val();
    var search_query = {"search":search_input};

    $.post("/search", search_query, function (data) {
        var lat = data.lat;
        var lon = data.lon;
        var mapbox_token = data.mapbox_token;
        var wiki_definition = data.wiki_definition;
        $("#wiki_definition").text(wiki_definition);

        marker = L.marker([lat, lon]).addTo(mymap);
        mymap.setView([lat, lon], 13);
        L.marker([lat, lon]).addTo(mymap);
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.streets',
            accessToken: mapbox_token
        }).addTo(mymap);
    })
});



