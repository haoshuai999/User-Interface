var employees = [
		"Phyllis",
		"Angela",
		"Dwight",
		"Oscar",
		"Creed",
		"Pam",
		"Jim",
		"Stanley",
		"Michael",
		"Kevin",
		"Kelly"
]
var ppclist = []

function makeNames(employees, ppclist){
	$("#non-ppc").empty()
	$("#ppc").empty()
	$.each(employees, function( index, value ){
		var $element = $("<div class='name'>").text((index + 1) + ":" + value);
		$("#non-ppc").append($element);
	})
	$.each(ppclist, function( index, value ){
		var $element = $("<div class='name'>").text((index + 1) + ":" + value);
		$("#ppc").append($element);
	})
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
function dragnonppc(){
	var z = 1;
	$("#non-ppc .name").draggable({
		drag: function( event, ui ){
			$(this).addClass("Hover")
			$(this).css("z-index", z++)
		},
		revert: "invalid"
	});
}
function dropnonppc(){
	$("#P").droppable({
		accept: "#non-ppc .name",
		classes: {
			"ui-droppable-active": "orange",
			"ui-droppable-hover": "darkorange"
		},
		drop: function( event, ui ){
			ppclist.push(ui.draggable.text().substring(2))
			employees.splice($.inArray(ui.draggable.text().substring(2), employees), 1 )
			makeNames(employees, ppclist)
			hover()
			dragnonppc()
			dragppc()
		}
	});
}
function dragppc(){
	var z = 1;
	$("#ppc .name").draggable({
		drag: function( event, ui ){
			$(this).addClass("Hover")
			$(this).css("z-index", z++)
		},
		revert: "invalid"
	});
}
function dropppc(){
	$("#NP").droppable({
		accept: "#ppc .name",
		classes: {
			"ui-droppable-active": "orange",
			"ui-droppable-hover": "darkorange"
		},
		drop: function( event, ui ){
			employees.push(ui.draggable.text().substring(2))
			ppclist.splice($.inArray(ui.draggable.text().substring(2), ppclist), 1 )
			makeNames(employees, ppclist)
			hover()
			dragnonppc()
			dragppc()
		}
	});
}

$(document).ready(function(){
	makeNames(employees, ppclist);
	hover();
	
	dragnonppc();
	dropnonppc();

	dragppc();
	dropppc();
});