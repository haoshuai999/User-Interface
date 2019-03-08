// var non_ppc_people = [
// 		"Phyllis",
// 		"Angela",
// 		"Dwight",
// 		"Oscar",
// 		"Creed",
// 		"Pam",
// 		"Jim",
// 		"Stanley",
// 		"Michael",
// 		"Kevin",
// 		"Kelly"
// ]
// var ppc_people = []

var display_lists = function(non_ppc_people, ppc_people){
	var z = 1
	$("#non-ppc").empty()
	$("#ppc").empty()
	$.each(non_ppc_people, function( index, value ){
		var $element = $("<div class='name'>").text((index + 1) + ":" + value);
		$("#non-ppc").append($element);
	})
	$.each(ppc_people, function( index, value ){
		var $element = $("<div class='name'>").text((index + 1) + ":" + value);
		$("#ppc").append($element);
	})
	$("#non-ppc .name").draggable({
		drag: function( event, ui ){
			$(this).addClass("Hover")
			$(this).css("z-index", z++)
		},
		revert: "invalid"
	});
	$("#ppc .name").draggable({
		drag: function( event, ui ){
			$(this).addClass("Hover")
			$(this).css("z-index", z++)
		},
		revert: "invalid"
	});
	hover();
}

var move_to_ppc = function(name){
	$.ajax({
		type: "POST",
		url: "move_to_ppc",                
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(name),
		success: function(result){
		      var temp_non_ppc = result["non_ppc_people"]
		      var temp_ppc = result["ppc_people"]
		      non_ppc_people = temp_non_ppc
		      ppc_people = temp_ppc
		      display_lists(non_ppc_people, ppc_people)
		},
		error: function(request, status, error){
		      console.log("Error");
		      console.log(request)
		      console.log(status)
		      console.log(error)
		}
	});
}

var move_to_non_ppc = function(name){
	$.ajax({
		type: "POST",
		url: "move_to_non_ppc",                
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(name),
		success: function(result){
		      var temp_non_ppc = result["non_ppc_people"]
		      var temp_ppc = result["ppc_people"]
		      non_ppc_people = temp_non_ppc
		      ppc_people = temp_ppc
		      display_lists(non_ppc_people, ppc_people)
		},
		error: function(request, status, error){
		      console.log("Error");
		      console.log(request)
		      console.log(status)
		      console.log(error)
		}
	});
}
function hover(){
	$(".name").hover(
		function() {
		    $(this).addClass("Hover");
		}, 
		function() {
		    $(this).removeClass("Hover");
		}
	)
}
// function dragnonppc(){
// 	var z = 1;
// 	$("#non-ppc .name").draggable({
// 		drag: function( event, ui ){
// 			$(this).addClass("Hover")
// 			$(this).css("z-index", z++)
// 		},
// 		revert: "invalid"
// 	});
// }
function dropnonppc(){
	$("#P").droppable({
		accept: "#non-ppc .name",
		classes: {
			"ui-droppable-active": "orange",
			"ui-droppable-hover": "darkorange"
		},
		drop: function( event, ui ){
			var name = ui.draggable.text().substring(2)
			// ppc_people.push(ui.draggable.text().substring(2))
			// non_ppc_people.splice($.inArray(ui.draggable.text().substring(2), non_ppc_people), 1 )
			move_to_ppc(name)
			
		}
	});
}
// function dragppc(){
// 	var z = 1;
// 	$("#ppc .name").draggable({
// 		drag: function( event, ui ){
// 			$(this).addClass("Hover")
// 			$(this).css("z-index", z++)
// 		},
// 		revert: "invalid"
// 	});
// }
function dropppc(){
	$("#NP").droppable({
		accept: "#ppc .name",
		classes: {
			"ui-droppable-active": "orange",
			"ui-droppable-hover": "darkorange"
		},
		drop: function( event, ui ){
			var name = ui.draggable.text().substring(2)
			// non_ppc_people.push(ui.draggable.text().substring(2))
			// ppc_people.splice($.inArray(ui.draggable.text().substring(2), ppc_people), 1 )
			
			move_to_non_ppc(name)
		}
	});
}

$(document).ready(function(){
	display_lists(non_ppc_people,ppc_people);
	hover();
	

	dropnonppc();
	dropppc();
});