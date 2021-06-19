$("#submitBtn").click(function(){
    $.ajax({
        data : {
            question : $("#question").val()
        },
        type: 'POST',
        url : "/test"
    })
})
