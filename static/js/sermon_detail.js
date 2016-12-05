var comments= function(){
    var request_context=$('#request_context');
    var api_token = $('#api_token');
    var comments = $('#comments');
    var current_event = $('#sermon'); 
    var comments_comments = $('#comments_comments');

    var ajaxCall=function(){
        $.ajax({ 
        url: request_context.val()+'/api/v1.0/sermon/',
        method: 'get',
        headers:{'Authorization':'Token '+api_token.val()}
        }).done(function(data1){
            if (data1){
                for (var i = 0; i < data1.results.length; i++) {
                    a = data1.results[i].id;
                    if (a == parseInt(current_event.val())) {
                        comments.html('');
                        for(ind in data1.results[i].comments){
                        comments.append($(document.createElement('div')).addClass('comment__item')
                        .append($(document.createElement('div')).addClass('comment__avatar')
                            .append($(document.createElement('img')).attr('src', '/static/media-demo/default.jpg')))
                        .append($(document.createElement('div')).addClass('comment__info')
                            .append($(document.createElement('div')).addClass('comment__info-left')
                                .append($(document.createElement('h3')).addClass('comment__author').html(data1.results[i].comments[ind].author))
                                .append($(document.createElement('time')).addClass('comment__time').html(moment(data1.results[i].comments[ind].date_posted).fromNow()))
                                )
                                )
                            
                        .append($(document.createElement('p')).addClass('comment__body').html(data1.results[i].comments[ind].content))
                            )
                    }
                    }
                }
            }
        }).fail(function(err){
            console.log(err);
        });
    };

    var send = function(){
        $('#sermon_detail').on('submit', function(e) {
        e.preventDefault();
        var data=$(this).serialize(); 

        $.ajax({
            url:request_context.val()+'/api/v1.0/comment/',
            method: 'post',
            headers: {'Authorization': 'Token '+api_token.val()},
            data:data
        }).done(function(data){
        }).fail(function(err){
            console.log(err);
        })          

        ajaxCall();
    });
    }
    
    return{
        init:function(){
            ajaxCall();
            send();
        }
    } 
}();