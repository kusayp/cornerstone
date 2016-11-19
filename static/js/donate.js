$('#contact').on('submit', function(e) {
    e.preventDefault();
    var current_event = $('#event');
    console.log(current_event.val());
    console.log($('input[name=csrfmiddlewaretoken]').val());
    console.log('heeeeeeeeeeee');
    var data=$(this).serialize();
    var request_context=$('#request_context');
    console.log(data);

        $.ajax({
            url:request_context.val()+'/api/v1.0/register/',
            method: 'post',
            headers: {'Authorization': 'Token aa3ab205f24441e0b161568c69e99d9f19155fbf'},
            data:data
        }).done(function(data1){
            console.log(data1);
            
        }).fail(function(err){
            console.log(err);
        })          

    // $.ajax({ 
    //     type: 'POST',
    //     url: 'api/v1.0/register/',
    //     data: data,
    //     headers:{'Authorization':'Token aa3ab205f24441e0b161568c69e99d9f19155fbf'}
    //     success:function(data){
    //         console('return',data);
    //         alert("Thank You");
    //     }
    // });
});







// {
//             name: $('#name').val(),
//             email: $('#email').val(),
//             phone: $('#phone').val(),
//             current_event: current_event.val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         }