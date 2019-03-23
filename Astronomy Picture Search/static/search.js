var display_result = function(search_result){
	var headline = $("<div class='row' p-1>")
	$("#search").append("<div class='row'><div class='col-md-12 py-3 sr'>Search Result")
	if(search_result.length == 0){
		$(headline).append("<div class='col-md-12 nore'><br/>No related results")
		$("#search").append(headline)
	}
	else{
		$(headline).append("<div class='col-md-4 hd'>Title")
		$(headline).append("<div class='col-md-2 hd'>Submit Date")
		$(headline).append("<div class='col-md-5 hd'>Copyright")
		$(headline).append("<div class='col-md-1 hd'>")
		$("#search").append(headline)
		$.each(search_result, function(index,value){
			var log = $("<div class='row' p-1>")
			var til = $("<div class='col-md-4 p-2 bold'></div>").append(search_result[index].Title)
			var dat = $("<div class='col-md-2 p-2'></div>").append(search_result[index].Day + '/' + search_result[index].Month + '/' + search_result[index].Year)
			var cop = $("<div class='col-md-5 p-2'></div>").append(search_result[index].Copyright)
			var det = $("<div class='col-md-1 p-2'>")
			var det_button = $("<button class='btn btn-dark'>Details</button>")
			$(det_button).click(function(){
			    window.location.href= 'http://127.0.0.1:5000/Item/' + search_result[index].Id
			})
			$(det).append(det_button)
			$(log).append(til, dat, cop, det)
			$("#search").append(log)
		})
	}
}

var submitsearch = function(){
	search_keyword = $.trim($("#searchspace").val())
	if(search_keyword.length == 0){
		alert("Please type in search keywords.")
		$("#searchspace").focus()
	}
	else{
		$.ajax({
		    type: "POST",
		    url: "search_item",                
		    dataType : "json",
		    contentType: "application/json; charset=utf-8",
		    data : JSON.stringify(search_keyword),
		    success: function(result){
		    	search_result = result["search_result"]
		    	display_result(search_result)
		    },
		    error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
		    }
		});
	}
}

$(document).ready(function(){
	$("#searchbtn").click(function(){
		$("#search").empty();
	    submitsearch();
	})
})