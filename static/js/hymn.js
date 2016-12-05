var hymn= function(){
	var stanza = $('#stanza'); 
	var request_context=$('#request_context');
	var hymns=$('#hymns');
	var api_token = $('#api_token');
	var numberPerPage=15;
	var ajaxCall=function(){
		$.ajax({
			url:request_context.val()+'/api/v1.0/hymns/', 
			method: 'get',
			headers: {'Authorization': 'Token '+ api_token.val()}
		}).done(function(data){
			console.log('return',data);
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
							url:request_context.val()+'/api/v1.0/hymns/?page='+page,
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
					var $stanzas='';
					for(ind in data.results[i].stanzas){
						$stanzas+='<h4 style="background-color:green; color: white">Verse '+(parseInt(ind)+1)+'</h4><p class"center">'+data.results[i].stanzas[ind].content.replace(/(?:\r\n|\r|\n)/g, '<br />')+'</p>';
						if(data.results[i].has_refrain){
							$stanzas+='<h4 style="background-color:red; color: white">Refrain</h4><p class"center">'+data.results[i].refrain.replace(/(?:\r\n|\r|\n)/g, '<br />')+'</p>';
						}
					}
					hymns.append($(document.createElement('div')).addClass('panel accordion-list').attr('style', 'border-radius:50%;')
						.append($(document.createElement('div')).addClass('panel-headingm')
							.append($(document.createElement('h4')).addClass('accordion__Heading')
								// .append($(document.createElement('a')).attr('href', '#media-audio_'+data.results[i].id).attr('aria-controls', 'media-audio').attr('role', 'tab').attr('data-toggle', 'tab'))
								.append($(document.createElement('a')).attr('data-toggle', 'collapse').attr('data-parent','#hymns').attr('href','#collapse_'+data.results[i].id).html(data.results[i].name)
								)
								)
							)
						.append($(document.createElement('div')).addClass('accordion__panel is-collapsed collapse').attr('id', 'collapse_'+data.results[i].id)
							.append($(document.createElement('div')).addClass('panel-body tab-content')	
								.html($stanzas)
								)
							// .append($(document.createElement('div')).attr('id', 'media-audio_'+data.results[i].id).attr('role', 'tabpanel').addClass('tab-pane')
							// 		.append($(document.createElement('div')).addClass('plyr')
							// 			.append($(document.createElement('audio')).attr('controls', '').attr('crossorigin', '')
							// 				.append($(document.createElement('source')).attr('src', '/static/media/'+data.results[i].name+'.mp3').attr('type', 'audio/mp3')))))
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