$("#search_request").on('click', function () {
    var search_input = $("#search_input").val();
    var search_query = {"search": search_input};
    $.post("/search", search_query, function (data) {

        if (data.status_code === "place_not_found") {
            place_not_found_response(data);
        } else if (data.status_code === "error") {
            error_response(data);
        } else if (data.status_code === "no_info") {
            no_info_response(data);
        } else {
            valid_response(data);
        }
    })
});


function valid_response(data) {
    var lat = data.lat;
    var lon = data.lon;
    var mapbox_token = data.mapbox_token;
    var display_name = data.display_name;
    var wiki_summary = data.wiki_summary;

    marker.setLatLng([lat, lon]);
    marker.setOpacity(1);
    mymap.setView([lat, lon], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: mapbox_token
    }).addTo(mymap);
    $("#display_name").text(display_name);
    $("#wiki_definition").text(wiki_summary);
}

function place_not_found_response(data) {
    var mapbox_token = data.mapbox_token;
    mymap.setView([0, 0], 1);
    marker.setOpacity(0);
    $("#wiki_definition").text('Je ne connais pas cette endroit');
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: mapbox_token
    }).addTo(mymap);
    console.log(data.status_code);
}

function error_response(data) {
    var lat = data.lat;
    var lon = data.lon;
    var mapbox_token = data.mapbox_token;
    var display_name = data.display_name;

    marker.setLatLng([lat, lon]);
    marker.setOpacity(1);
    mymap.setView([lat, lon], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: mapbox_token
    }).addTo(mymap);
    $("#display_name").text(display_name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status_code);
}

function no_info_response(data) {
    var lat = data.lat;
    var lon = data.lon;
    var mapbox_token = data.mapbox_token;
    var display_name = data.display_name;

    marker.setLatLng([lat, lon]);
    marker.setOpacity(1);
    mymap.setView([lat, lon], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: mapbox_token
    }).addTo(mymap);
    $("#display_name").text(display_name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status_code);
}