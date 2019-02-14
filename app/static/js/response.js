const wikimedia_ok_status = [
    "wikimedia_page_id_ok",
    "wikimedia_page_summary_ok",
    "wikimedia_page_url_ok"
];
const error_status = [
    "wikimedia_error_500",
    "wikimedia_error_504",
    "wikimedia_error_400",
    "wikimedia_error_404",
    "wikimedia_api_error",
    "google_over_query_limit",
    "google_request_denied",
    "google_invalid_request",
    "google_unknown_error",
];
const zero_results_status = [
    "google_zero_results"
];
const no_info_status = [
    "wikimedia_zero_results",
    "wikimedia_no_page_url",
];
$(document).ready(function () {

    $("#request_input_form").submit(function (event) {
        event.preventDefault();
        const user_input = {"user_input": $("#research_input").val()};

        $.post("/user_message", user_input, function (data) {
            $("#research_input").val("");
            $('#msg_history').append(data);
            let h = $('#msg_history').height();
            $('#chat_box').scrollTop(h);
        });

        // Bot response
        $.post("/grandpy_message", user_input, function (response) {
            //Status gestion
            if (wikimedia_ok_status.indexOf(response.status) !== -1) {

                // Gmap mod
                gmap.panTo({lat: response.lat, lng: response.lng});
                gmap.setZoom(15);
                marker.setVisible(true);
                marker.setPosition({lat: response.lat, lng: response.lng});

                // First message
                $('#msg_history').append(response.msg_1);
                let h = $('#msg_history').height();
                $('#chat_box').scrollTop(h);

                // Second message
                setTimeout(function () {
                    $('#msg_history').append(response.msg_2);
                    let h = $('#msg_history').height();
                    $('#chat_box').scrollTop(h);
                }, 1500);

                // Third message
                setTimeout(function () {
                    $('#msg_history').append(response.msg_3);
                    let h = $('#msg_history').height();
                    $('#chat_box').scrollTop(h);
                }, 3000);

            } else if (no_info_status.indexOf(response.status) !== -1) {

                // Gmap mod
                gmap.panTo({lat: response.lat, lng: response.lng});
                gmap.setZoom(15);
                marker.setVisible(true);
                marker.setPosition({lat: response.lat, lng: response.lng});

                // First message
                $('#msg_history').append(response.msg_1);
                // noinspection JSUndeclaredVariable
                let h = $('#msg_history').height();
                $('#chat_box').scrollTop(h);

                // Second message
                setTimeout(function () {
                    $('#msg_history').append(response.msg_2);
                    let h = $('#msg_history').height();
                    $('#chat_box').scrollTop(h);
                }, 1500);

            } else if (zero_results_status.indexOf(response.status) !== -1) {

                // Gmap mod
                gmap.panTo({lat: 0, lng: 0});
                gmap.setZoom(1);
                marker.setVisible(false);

                // First message
                $('#msg_history').append(response.msg_1);
                let h = $('#msg_history').height();
                $('#chat_box').scrollTop(h);

            } else if (error_status.indexOf(response.status) !== -1) {

                // Gmap mod
                gmap.panTo({lat: 0, lng: 0});
                gmap.setZoom(1);
                marker.setVisible(false);

                // First message
                $('#msg_history').append(response.msg_1);
                let h = $('#msg_history').height();
                $('#chat_box').scrollTop(h);
            }
        });
    });
});


