$(".request_input_text").submit(function (event) {
    event.preventDefault();
    var user_input = {"user_input": $("#research_input").val()};

    $.post("/user_message", user_input, function (data) {
        $("#research_input").val("");
        $('.msg_history').append(data).scrollTop(1000000);
    });

    $.post("/grandpy_message", user_input, function (data) {
        $('.msg_history').append(data).scrollTop(1000000);
    })
});

