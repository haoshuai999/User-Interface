var displayitems = function(id){
	if(id != 12){
		img = "<img src='" + data[id].Poster +"' class='mx-auto d-block img-fluid' alt='loading'>"
	}
	else{
		img = "<iframe width='1100' height='600' align='middle' src='" + data[id].Poster +"'></iframe>"
	}
	date = data[id].Year + '-' + data[id].Month + '-' + data[id].Day
	footer = '<br>' + 'Authors & editors: ' + data[id].PageAuthor + ' & ' + data[id].PageEditor
	$("#headline").append(data[id].Title)
	$("#image").append(img)
	$("#author").append("Credit: " + data[id].Copyright)
	$("#date").append(date)
	$("#explanation").append(data[id].Explanation)
	$("#footer").append(footer)
}
$(document).ready(function(){
	displayitems(id - 1);
})