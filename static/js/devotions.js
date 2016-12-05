
var request_context=$('#request_context');
var api_token = $('#api_token'); 
$('#list').find('.devotion').on('click', function (e) {
	e.preventDefault();
	var page = $(this);
	var devotion_num = page.attr('data-id');
	$.ajax({
		url: request_context.val()+'/api/v1.0/devotion/', 
		method: 'GET',
		headers: {'Authorization': 'Token '+api_token.val()}
	}).done(function(data){
		if (data) {
				for (var i = 0; i < data.results.length; i++) {
					a = data.results[i].id
					if (a == parseInt(devotion_num)) {
						$('#title').text(data.results[i].title);
						$('#content').html(data.results[i].content);
						$('#principle').html(data.results[i].principle);
					}
				}
			}
	}).fail(function(err){
		console.log(err);
	})
})