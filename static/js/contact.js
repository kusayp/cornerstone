$(document).on('submit', '#contact', function(e) {
    e.preventDefault();
    console.log($('#name').val());
    console.log($('input[name=csrfmiddlewaretoken]').val());
    console.log('heeeeeeeeeeee');
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