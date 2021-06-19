$(document).ready(function(){
    
    $.ajax({
        data : {
            question : $("#question").val()
        },
        type: 'POST',
        url : "/wolframR"
        }
    )
    .done(function(data){
        if (!data.error) {
            const answer = document.createElement("div")
            answer.innerText = data.answer;
        }
    });
    event.preventDefault();
});