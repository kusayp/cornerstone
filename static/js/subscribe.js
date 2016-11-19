$(document).on('submit', '#subscribe', function(e) {
    e.preventDefault();
    $.ajax({ 
        type: 'POST',
        url: '/',
        data: {
            email: $('#email').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert("Subscribe");
        }
    });
});