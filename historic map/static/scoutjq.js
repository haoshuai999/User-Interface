function showquestions(page){
	$("#cityname").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center headline' id='cityname'>" + qdata[page-1].City)
	$("#question").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center question' id='question'>Q:" + qdata[page-1].Question)
	$("#op1").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op1'>" + qdata[page-1].Option1 + "</button>")
	$("#op2").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op2'>" + qdata[page-1].Option2 + "</button>")
	$("#op3").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op3'>" + qdata[page-1].Option3 + "</button>")
	$("#op4").replaceWith("<button type='button' class='btn btn-primary btn-sm op' id='op4'>" + qdata[page-1].Option4 + "</button>")
}
function answerquestions(page){
	$("#options").on("click",".op", function(){
		if($(this).text()==qdata[page-1].Answer){
			$(".op").addClass("red")
			$(this).removeClass("red").addClass("green")
			score += 10
			$("#score").replaceWith("<div class='col-md-12 p-2' id='score'><b>Score: </b>" + score)
		}
		else{
			for (i = 1; i <= 4; i++) {
				if($("#op" + i).text()==qdata[page-1].Answer){
					$("#op" + i).addClass("green")
				}
				else{
					$("#op" + i).addClass("red")
				}
			}
		}
		$("#next").removeClass("disabled")
		$("#submit").removeClass("disabled")
	})
	$("#next").click(function(){
		page++
		if(page == 3){
			$("#next").replaceWith("<button type='button' class='btn btn-primary btn-lg btn-block' id='submit'>Submit Score</button>")
		}
		showquestions(page)
		$("#next").addClass("disabled")
		$("#submit").addClass("disabled")
	})
	$("#sub-btn").on("click","#submit", function(){
		if(score==30){
			$("#modal0").addClass("display")
		}
		else{
			$("#modal1").addClass("display")
		}
	});
}
$(document).ready(function(){
	console.log(qdata)
	page = 1
	$("#next").addClass("disabled");
	$(".homepage").click(function(){
		if(confirm("Are you sure you want to go back to homepage?")){
			window.location.href='index.html'
		}
	});
	showquestions(page);
	answerquestions(page);
});