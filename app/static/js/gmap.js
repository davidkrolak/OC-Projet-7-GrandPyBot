$("#search_request").submit(function(event) {
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
    $("#display_name").text(data.name);
    $("#formated_address").text(data.formatted_address);
    $("#wiki_definition").text(data.wiki_summary);
}

function zero_results_response(data) {
    $("#search_input").val("");
    $("#display_name").text("");
    $("#wiki_definition").text("Je ne peux pas répondre a ta question, désolé");
    console.log(data.status);
}

function error_response(data) {
    coordinates = {lat: data.lat, lng: data.lng};
    $("#search_input").val("");
    $("#display_name").text(data.name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status);
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
    $("#display_name").text(data.name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status);
}