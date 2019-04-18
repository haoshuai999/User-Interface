$(document).ready(function(){
	$("#worldmap").click(function(){
		window.location.href='map.html'
	})
	$("#scout").click(function(){
		window.location.href='scout.html'
	})
	$("#exit").click(function(){
		if(confirm("Do you really want to exit?")){
			window.close();
		}
	})
});