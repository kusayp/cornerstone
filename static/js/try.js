var wwb= function(){
	var request_context=$('#request_context');
	var hymns=$('#wwb_list');
	var api_token = $('#api_token');
	var numberPerPage=10;
	var ajaxCall=function(){ 
		$.ajax({
			url:request_context.val()+'/api/v1.0/wwb/',
			method: 'get',
			headers: {'Authorization': 'Token '+ api_token.val()}
		}).done(function(data){
			populateHymns(data);

			var numberOfPages=Math.ceil(data.count/numberPerPage)
			if(numberOfPages>1){
				var pagination=$(document.createElement('ul'));
				pagination.twbsPagination({
					totalPages:numberOfPages, 
					visiblePages:7,
					initiateStartPageClick:false,
					onPageClick: function(event, page){
						$.ajax({
							url:request_context.val()+'/api/v1.0/wwb/?page='+page,
							method: 'get',
							headers: {'Authorization': 'Token '+ api_token.val()}
						}).done(function(data1){
							populateHymns(data1);
						}).fail(function(err){
							console.log(err);
						})			

					}
				});
				$('#hymn_pagination').append(pagination); 
			}
			

			

		}).fail(function(err){
				console.log(err);
		});

		};
function populateHymns(data){
			hymns.html('');
			if (data){
				for (var i = 0; i < data.results.length; i++) {
					hymns.append($(document.createElement('div')).addClass('panel panel-default')
						.append($(document.createElement('div')).addClass('panel-heading')
							.append($(document.createElement('h4')).addClass('panel-title')
								.append($(document.createElement('a')).attr('data-toggle', 'collapse').attr('data-parent','#wwb_list').attr('href','#collapse_'+data.results[i].id).html(data.results[i].title)

								)
								)
							)
						.append($(document.createElement('div')).addClass('panel-collapse collapse').attr('id', 'collapse_'+data.results[i].id)
							.append($(document.createElement('div')).addClass('panel-body')
								.html($.trim(data.results[i].content))

								)
							)
						)
				}
			}
		}


	return{
		init:function(){
			ajaxCall();
		}
	}
}();

// .substring(0, 100).split(" ").slice(0, -1).join(" ")+"..."