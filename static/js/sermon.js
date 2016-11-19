var hymn= function(){
	var sermon = $('#sermon');
	var request_context=$('#request_context');
	var api_token = $('#api_token'); 
	var numberPerPage=3;

	var ajaxCall=function(){
		console.log('token',api_token.val());
		// $('.list__item').find('a').on('click', function(){
		// 	var $this=$(this);

			$.ajax({
				url:request_context.val()+'/api/v1.0/sermon/',
				method: 'get',
				headers: {'Authorization': 'Token '+api_token.val()}
				}).done(function(data){
					populateHymns(data);

					var numberOfPages=Math.ceil(data.count/numberPerPage)
						console.log(numberOfPages);
						if(numberOfPages>1){
							var pagination=$(document.createElement('ul'));
							pagination.twbsPagination({
								totalPages:numberOfPages,
								visiblePages:7,
								initiateStartPageClick:false,
								onPageClick: function(event, page){ 
									$.ajax({
										url:request_context.val()+'/api/v1.0/sermon/?page='+page,
										method: 'get',
										headers: {'Authorization': 'Token '+ api_token.val()}
									}).done(function(data1){
										populateHymns(data1);
										console.log(data1);

									}).fail(function(err){
										console.log(err);
									})			

								}
							});
							$('#sermon_pagination').append(pagination);
						}
					}).fail(function(err){
							console.log(err);
				});
					function populateHymns(data){
			sermon.html('');
			if (data){
				for (var i = 0; i < data.results.length; i++) {
					sermon.append($(document.createElement('div')).attr('data_id', 0).addClass('sermon__item js-sermon-item')
						.append($(document.createElement('a')).addClass('sermon__preview')
							.append($(document.createElement('img')).attr('src', "/static/media-demo/post/post-3.jpg").addClass('sermon__preview-img')
								)
							.append($(document.createElement('figure')).addClass('sermon__ministry')
								.append($(document.createElement('figcaption')).addClass('sermon__ministry-name')
									.append($(document.createElement('strong')).html(data.results[i].author))
									)
								)
							)
						.append($(document.createElement('div')).addClass('sermon__info')
							.append($(document.createElement('time')).attr('datetime', 2016).addClass('sermon__time').html(moment(data.results[i].date).format('MMM. DD, YYYY')))
							.append($(document.createElement('h3')).addClass('sermon__name').append($(document.createElement('a')).attr('href', '/resources/'+data.results[i].id+'/').html(data.results[i].title))
								)
							.append($(document.createElement('div')).addClass('sermon__intro')
								// .append($(document.createElement('p')).html(data.results[i].content))
								)
							.append($(document.createElement('div')).addClass('clearfix'))
							.append($(document.createElement('a')).attr('href', '/resources/'+data.results[i].id+'/').addClass('btn--link event__more').html('Read more'))
							)
						);
				}
			}
		}
		};

	$('#categorys').find('.category').on('click', function(e){
		e.preventDefault();
		var page = $(this);
		var category_num = page.attr('data-key');
		console.log(category_num);
		$.ajax({
			url:request_context.val()+'/api/v1.0/sermon_categories/',
			method:'get',
			headers: {'Authorization': 'Token '+api_token.val()}
		}).done(function(data){
			console.log(data);
			sermon.html('');
			if (data) {
				for (var i = 0; i < data.results.length; i++) {
					a = data.results[i].id
					console.log(a);
					if (a == parseInt(category_num)) {
						for(ind in data.results[i].sermons){
							console.log('working');
							sermon.append($(document.createElement('div')).attr('data_id', 0).addClass('sermon__item js-sermon-item')
						.append($(document.createElement('a')).addClass('sermon__preview')
							.append($(document.createElement('img')).attr('src', "/static/media-demo/post/post-3.jpg").addClass('sermon__preview-img')
								)
							.append($(document.createElement('figure')).addClass('sermon__ministry')
								.append($(document.createElement('figcaption')).addClass('sermon__ministry-name')
									.append($(document.createElement('strong')).html(data.results[i].sermons[ind].author))
									)
								)
							)
						.append($(document.createElement('div')).addClass('sermon__info')
							.append($(document.createElement('time')).attr('datetime', 2016).addClass('sermon__time').html(data.results[i].sermons[ind].date))
							.append($(document.createElement('h3')).addClass('sermon__name').append($(document.createElement('a')).attr('href', '/resources/'+data.results[i].sermons[ind].id+'/').html(data.results[i].sermons[ind].title))
								)
							.append($(document.createElement('div')).addClass('sermon__intro')
								// .append($(document.createElement('p')).html(data.results[i].content))
								)
							.append($(document.createElement('div')).addClass('clearfix'))
							.append($(document.createElement('a')).attr('href', '/resources/'+data.results[i].sermons[ind].id+'/').addClass('btn--link event__more').html('Read more'))
							)
						);
						}
					}
				}
			}
		});
	});
	return{
		init:function(){
			ajaxCall();
		}
	}
}();