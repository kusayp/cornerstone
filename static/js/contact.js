$(document).on('submit', '#contact', function(e) {
    e.preventDefault();
    $.ajax({ 
        type: 'POST',
        url: '/cont/contact/',
        data: {
            name: $('#name').val(),
            email: $('#email').val(),
            phone: $('#phone').val(),
            content: $('#content').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert("Thank You");
        }
    });
});