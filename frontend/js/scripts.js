$("#form").on("submit", function(){
	$.ajax({
		url: 'http://backend:8888',
		method: 'post',
		dataType: 'json',
		data: $(this).serialize(),
		success: function(data){
			alert("asd");
		}
	});
});