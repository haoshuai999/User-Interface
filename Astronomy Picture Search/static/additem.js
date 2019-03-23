var saveitem = function(newitem){
	$.ajax({
	    type: "POST",
	    url: "save_item",                
	    dataType : "text",
	    contentType: "application/json; charset=utf-8",
	    data : JSON.stringify(newitem),
	    success: function(newid){
	          var returnid = newid
	          $("#success").append("Successfully add one picture to Astronomy Picture Database!")
	          $("#url").append("Please click <a href='http://127.0.0.1:5000/Item/" + returnid + "'>this link</a> to see the new page.")
	    },
	    error: function(request, status, error){
	          console.log("Error");
	          console.log(request)
	          console.log(status)
	          console.log(error)
	    }
	});


	$("#imgtitle").val("")
	$("#imglink").val("")
	$("#imgdate").val("")
	$("#imgexp").val("")
	$("#imgcopyright").val("")
	$("#imgauthor").val("")
	$("#imgeditor").val("")
	$("html, body").animate({
	    scrollTop: $('#success').offset().top
	},500);
}

var submititem = function(){
	date = $("#imgdate").val().split("-")
	var title = $.trim($("#imgtitle").val())
	var link = $.trim($("#imglink").val())
	var year = date[2]
	var month = date[1]
	var day = date[0]
	var explanation = $.trim($("#imgexp").val())
	var copyright = $.trim($("#imgcopyright").val())
	var author = $.trim($("#imgauthor").val())
	var editor = $.trim($("#imgeditor").val())
	if(title.length == 0){
		alert("Unable to submit! The Image Title field is empty.")
		$("#imgtitle").focus()
	}
	else if(link.length == 0){
		alert("Unable to submit! The Image Link field is empty.")
		$("#imglink").focus()
	}
	else if(explanation.length == 0){
		alert("Unable to submit! The Explanation field is empty.")
		$("#imgexp").focus()
	}
	else if(copyright.length == 0){
		alert("Unable to submit! The Image Author field is empty.")
		$("#imgcopyright").focus()
	}
	else if(author.length == 0){
		alert("Unable to submit! The Page Author field is empty.")
		$("#imgauthor").focus()
	}
	else if(editor.length == 0){
		alert("Unable to submit! The Page Editor field is empty.")
		$("#imgeditor").focus()
	}
	else if($.isNumeric(year)==false || $.isNumeric(month)==false || $.isNumeric(day)==false){
		alert("Unable to submit! Please input number in the Image Submit Time field.")
		$("#imgdate").focus()
	}
	else if(date.length == 0 || year.length == 0 || month.length == 0 || day.length == 0){
		alert("Unable to submit! Please input a valid Image Submit Time.")
		$("#imgdate").focus()
	}
	else{
		newitem = {
			"Title": title,
			"Poster": link,
			"Year": year,
			"Month": month,
			"Day": day,
			"Explanation": explanation,
			"Copyright": copyright,
			"PageAuthor": author,
			"PageEditor": editor
		}
		saveitem(newitem)
	}
}

$(document).ready(function(){
	$("#submit").click(function(){
		$("#success, #url").empty();
	    submititem();
	})
})