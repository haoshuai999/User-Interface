$(document).ready(function(){
	$("#homepage").click(function(){
		if(confirm("Are you sure you want to go back to homepage?")){
			window.location.href='/#worldmap'
		}
	})
});