$(document).ready(function(){
	$(".homepage").attr("disabled", true).css("color","white");
	$("nav").on("mouseover",".worldmap,.quiz",function(){
				$(this).addClass("hover")
	})
	$("nav").on("mouseout",".worldmap,.quiz",function(){
				$(this).removeClass("hover")
	})
	$("#worldmap,.worldmap").click(function(){
		window.location.href='intelligence'
	})
	$(".quiz").click(function(){
		window.location.href='expedition'
	})
});