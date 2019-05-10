function displaytutorial(data){
	$("#city").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center' id='city'>" + data.City)
	$("#cityimg").replaceWith("<div class='col-md-12 p-2 text-center' id='cityimg'><img src='" + data.URL + "' alt='cityimage' class='img-fluid'>")
	$("#key1").replaceWith("<li id='key1'>" + data.Key1)
	$("#key2").replaceWith("<li id='key2'>" + data.Key2)
	$("#key1").html($("#key1").html().replace('Kingdom of Macedon','<b>Kingdom of Macedon</b>').replace('The first Asian city','<b>The first Asian city</b>').replace('Capital','<b>Capital</b>'))
	$("#key2").html($("#key2").html().replace('Lighthouse','<b>Lighthouse</b>').replace('Greek culture','<b>Greek culture</b>'))
}
function gettutorial(){
	$.ajax({
		type: "GET",
		url: "tutorial",                
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		success: function(result){
			data = result["city"]
			displaytutorial(data)
		},
		error: function(request, status, error){
			console.log("Error");
			console.log(request)
			console.log(status)
			console.log(error)
		}
	});
}
function refresh(){
	$.ajax({
		type: "POST",
		url: "refresh",                
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		success: function(result){
			console.log(result)
		},
		error: function(request, status, error){
			console.log("Error");
			console.log(request)
			console.log(status)
			console.log(error)
		}
	});
}
$(document).ready(function(){
	$(".worldmap").attr("disabled", true).css("color","white");
	$("nav").on("mouseover",".homepage,.quiz",function(){
				$(this).addClass("hover")
	})
	$("nav").on("mouseout",".homepage,.quiz",function(){
				$(this).removeClass("hover")
	})
	gettutorial()
	addcity(1)
	$("body").on("click",".homepage",function(){
		$("#dialog-confirm1").dialog({
			resizable: false,
			height: "auto",
			width: 400,
			modal: true,
			buttons: {
			  "Yes": function() {
				$(this).dialog("close")
				refresh()
				window.location.href='/'
			  },
			  Cancel: function() {
				$(this).dialog("close");
			  }
			}
		});
	})
	$("body").on("click",".quiz",function(){
		$("#dialog-confirm1 p").replaceWith("<p>Go to the quiz page</p>")
		$("#dialog-confirm1").dialog({
			resizable: false,
			height: "auto",
			width: 400,
			modal: true,
			buttons: {
			  "Yes": function() {
				$(this).dialog("close")
				refresh()
				window.location.href='/expedition'
			  },
			  Cancel: function() {
				$(this).dialog("close");
			  }
			}
		});
	})
	$(".nextpage").click(function(){
		$.ajax({
			type: "POST",
			url: "tutorial",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			success: function(result){
				addcity(result["tutorpage"])
				displaytutorial(result["city"])
				if(result["tutorpage"] == 5){
					$(".nextpage").replaceWith("<button type='button' class='btn btn-warning btn-lg btn-block' id='expedition'>Quiz</button>")
					$("#guide").replaceWith("<div class='col-md-12 pb-2 text-center' id='guide'><b>Hover on map to review</b></div>")
					addhover()
				}
			},
			error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
			}
		});
	})
	// $("#next").on("click","#explore",function(){
	// 	$("#modal0").hide()
	// 	$("#hismap").removeClass("moveleft")
	// 	$("#sidebar").removeClass("conseal")
	// 	addcity(1)
	// })
	$("#exp").on("click","#expedition",function(){
		$("#dialog-confirm2").dialog({
			resizable: false,
			height: "auto",
			width: 400,
			modal: true,
			buttons: {
			  "Yes": function() {
				$(this).dialog("close")
				refresh()
				window.location.href='/expedition'
			  },
			  Cancel: function() {
				$(this).dialog("close");
			  }
			}
		});
	})
});