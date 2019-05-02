function showquestions(qdata,score){
	$("#cityname").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center headline' id='cityname'>" + qdata.City)
	$("#question").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center question' id='question'>Q:" + qdata.Question)
	$("#op1").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op1'>" + qdata.Option1 + "</button>")
	$("#op2").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op2'>" + qdata.Option2 + "</button>")
	$("#op3").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op3'>" + qdata.Option3 + "</button>")
	$("#op4").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op4'>" + qdata.Option4 + "</button>")
	$("#score").replaceWith("<div class='col-md-12 p-2' id='score'><b>Score: </b>" + score)
}
function answerquestions(){
	$("#options").on("click",".op", function(){
		user_answer = $(this).text()
		$.ajax({
			type: "POST",
			url: "answer_quiz",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			data : JSON.stringify(user_answer),
			success: function(result){
				$("#score").replaceWith("<div class='col-md-12 p-2' id='score'><b>Score: </b>" + result["score"])
				correct_index = result["correct_index"]
				$(".op").attr("disabled", true).addClass("red")
				$("#op" + correct_index).attr("disabled", true).removeClass("red").addClass("green")
				$("#next").attr("disabled", false).removeClass("disabled")
				$("#submit").attr("disabled", false).removeClass("disabled")
				$(".homepage,.worldmap").attr("disabled", true).addClass("disabled")
			},
			error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
			}
		});
	})
	$("#next").click(function(){
		getquestions(1)
	})
	$("#sub-btn").on("click","#submit", function(){
		$.ajax({
			type: "GET",
			url: "refresh",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			success: function(result){
				score = result["score"]
				$(".homepage,.worldmap").attr("disabled", false).removeClass("disabled")
				if(score==50){
					$("#modal0").addClass("display")
				}
				else{
					$("#modal1").addClass("display")
				}
			},
			error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
			}
		});
	});
}
function getquestions(new_page){
	$.ajax({
		type: "POST",
		url: "display_questions",                
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(new_page),
		success: function(result){
			addcity(result["page"])
			showquestions(result["question"],result["score"])
			if(result["page"] == 5){
				$("#next").replaceWith("<button type='button' class='btn btn-primary btn-lg btn-block' id='submit'>Submit Score</button>")
			}
			$(".op").attr("disabled", false)
			$("#next").attr("disabled", true).addClass("disabled")
			$("#submit").attr("disabled", true).addClass("disabled")
			$(".homepage,.worldmap").attr("disabled", false).removeClass("disabled")
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
function exittip(page,flag){
	if(page >= 6){
		$("#dialog-confirm").dialog({
			resizable: false,
			height: "auto",
			width: 400,
			modal: true,
			buttons: {
			  "Yes": function() {
				$(this).dialog("close")
				refresh()
				if(flag==0){
					window.location.href='/'
				}
				else{
					window.location.href='/intelligence'
				}
			  },
			  Cancel: function() {
				$(this).dialog("close");
			  }
			}
		});
	}
	else{
		$("#dialog-confirm p").replaceWith("<p>Do you want to save the progress?</p>")
		$("#dialog-confirm").dialog({
			resizable: false,
			height: "auto",
			width: 400,
			modal: true,
			buttons: {
			  "Yes": function() {
				$(this).dialog("close")
				if(flag==0){
					window.location.href='/'
				}
				else{
					window.location.href='/intelligence'
				}
			  },
			  "No": function() {
				$(this).dialog("close")
				refresh()
				if(flag==0){
					window.location.href='/'
				}
				else{
					$("#dialog-confirm1 p").replaceWith("<p>Go to the world map page</p>")
					window.location.href='/intelligence'
				}
			  },
			  Cancel: function() {
				$(this).dialog("close");
			  }
			}
		});
	}
}
$(document).ready(function(){
	//console.log(page)
	//console.log(score)
	$(".quiz").attr("disabled", true).css("color","white");
	$("nav").on("mouseover",".worldmap,.homepage",function(){
				$(this).addClass("hover")
	})
	$("nav").on("mouseout",".worldmap,.homepage",function(){
				$(this).removeClass("hover")
	})
	$("#next").attr("disabled", true).addClass("disabled");
	$(".homepage").click(function(){
		$.ajax({
			type: "GET",
			url: "refresh",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			success: function(result){
				exittip(result["page"],0)
			},
			error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
			}
		});
	});
	$("body").on("click",".worldmap",function(){
		$.ajax({
			type: "GET",
			url: "refresh",                
			dataType : "json",
			contentType: "application/json; charset=utf-8",
			success: function(result){
				exittip(result["page"],1)
			},
			error: function(request, status, error){
				console.log("Error");
				console.log(request)
				console.log(status)
				console.log(error)
			}
		});
	})
	$("#retake").click(function(){
		refresh();
		location.reload();
	});
	$("#review").click(function(){
		refresh();
		window.location.href='intelligence'
	});
	getquestions(0);
	answerquestions();
});