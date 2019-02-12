$("#request_input_form").submit(function (event) {
    event.preventDefault();
    var user_input = {"user_input": $("#research_input").val()};

    $.post("/user_message", user_input, function (data) {
        $("#research_input").val("");
        h = $('#msg_history').height();
        console.log(h);
        $('#msg_history').append(data);
        $('#chat_box').scrollTop(h);
    });

    $.post("/grandpy_message", user_input, function (response) {
        h = $('#msg_history').height();
        console.log(h);
        $('#msg_history').append(response.msg_1);
        $('#chat_box').scrollTop(h);
    })
});
