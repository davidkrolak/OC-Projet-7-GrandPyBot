$("#search_request").submit(function (event) {
    event.preventDefault();
    var search_input = $("#search_input").val();
    var search_query = {"search": search_input};
    $.post("/search", search_query, function (data) {

        if (data.status === "zero_results") {
            zero_results_response(data);
        } else if (data.status === "error") {
            error_response(data);
        } else if (data.status === "no_info") {
            no_info_response(data);
        } else {
            valid_response(data);
        }
    })
});


function valid_response(data) {
    coordinates = {lat: data.lat, lng: data.lng};
    gmap.panTo(coordinates);
    gmap.setZoom(15);
    marker.setOptions({
        position: coordinates,
        visible: true
    });
    $("#mapid").show();
    $("#mapid_placeholder").hide();
    $("#search_input").val("");
    $("#display_name").text("Tu m'as posé une question sur \"" + data.name + "\".");
    $("#grandpy_response").text(data.grandpy_response + ", voici son adresse:");
    $("#formated_address").text(data.formatted_address);
    $("#pre_definition").text("Voici ce que je peux te dire à son propos:");
    $("#wiki_definition").text(data.wiki_summary);
}

function zero_results_response(data) {
    coordinates = {lat: 0, lng: 0};
    gmap.panTo(coordinates);
    gmap.setZoom(1);
    marker.setOptions({
        position: coordinates,
        visible: false
    });
    $("#search_input").val("");
    $("#display_name").text("Tu m'as posé une question sur \"" + data.name + "\".");
    $("#grandpy_response").text(data.grandpy_response);
    $("#formated_address").text("");
    $("#pre_definition").text("");
    $("#wiki_definition").text("");
}

function error_response(data) {
    coordinates = {lat: data.lat, lng: data.lng};
    gmap.panTo(coordinates);
    gmap.setZoom(15);
    marker.setOptions({
        position: coordinates,
        visible: true
    });
    $("#search_input").val("");
    $("#display_name").text("Tu m'as posé une question sur \"" + data.name + "\".");
    $("#grandpy_response").text(data.grandpy_response);
    $("#formated_address").text("");
    $("#pre_definition").text("");
    $("#wiki_definition").text("");
}

function no_info_response(data) {
    coordinates = {lat: data.lat, lng: data.lng};
    gmap.panTo(coordinates);
    gmap.setZoom(15);
    marker.setOptions({
        position: coordinates,
        visible: true
    });
    $("#mapid").show();
    $("#mapid_placeholder").hide();
    $("#search_input").val("");
    $("#display_name").text("Tu m'as posé une question sur \"" + data.name + "\".");
    $("#grandpy_response").text(data.grandpy_response + ", voici son adresse:");
    $("#formated_address").text(data.formatted_address);
    $("#pre_definition").text("");
    $("#wiki_definition").text("");
}