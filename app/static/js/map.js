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
    var display_name = data.display_name;
    var wiki_summary = data.wiki_summary;

    $("#display_name").text(display_name);
    $("#wiki_definition").text(wiki_summary);
}

function place_not_found_response(data) {
    console.log(data.status_code);
}

function error_response(data) {
    var lat = data.lat;
    var lon = data.lon;
    var display_name = data.display_name;

    $("#display_name").text(display_name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status_code);
}

function no_info_response(data) {
    var lat = data.lat;
    var lon = data.lon;
    var display_name = data.display_name;

    $("#display_name").text(display_name);
    $("#wiki_definition").text("Je sais ou c'est mais je ne connais rien a propos de cette endroit");

    console.log(data.status_code);
}