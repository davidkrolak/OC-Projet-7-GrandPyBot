$(".request_input_text").submit(function (event) {
    event.preventDefault();
    var user_input = {"user_input": $("#user_input").val()};

    $.post("/user_message",user_input , function (data) {
        $("#user_input").val("");
        $('.msg_history').append(data).scrollTop(1000000);
    });

    // $.post("/search", search_query, function (data) {
    //     if (data.status === "zero_results") {
    //         zero_results_response(data);
    //     } else if (data.status === "error") {
    //         error_response(data);
    //     } else if (data.status === "no_info") {
    //         no_info_response(data);
    //     } else {
    //         valid_response(data);
    //     }
    // })
});

