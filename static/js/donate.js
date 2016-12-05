var request_context=$('#request_context');
var api_token = $('#api_token');
$('#contact').on('submit', function(e) {
    e.preventDefault();
    var current_event = $('#event');
    var data=$(this).serialize();
    var request_context=$('#request_context');
        $.ajax({
            url:request_context.val()+'/api/v1.0/register/',
            method: 'post',
            headers: {'Authorization': 'Token '+ api_token.val()},
            data:data
        }).done(function(data1){            
        }).fail(function(err){
            console.log(err);
        })          
    });