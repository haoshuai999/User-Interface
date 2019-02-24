clients = [
      "Shake Shack",
      "Toast",
      "Computer Science Department",
      "Teacher's College",
      "Starbucks",
      "Subsconsious",
      "Flat Top",
      "Joe's Coffee",
      "Max Caffe",
      "Nussbaum & Wu",
      "Taco Bell",
];

var sales = [
      {
            "salesperson": "James D. Halpert",
            "client": "Shake Shack",
            "reams": 100
      },
      {
            "salesperson": "Stanley Hudson",
            "client": "Toast",
            "reams": 400
      },
      {
            "salesperson": "Michael G. Scott",
            "client": "Computer Science Department",
            "reams": 1000
      },
]

function deletelog(object, index){
      $(object).parentsUntil(".all_logs").remove()
      sales.splice( index , 1)
      console.log(sales)
}
function defaultlog(){
      $("#clients").attr("placeholder","client")
      $("#reams").attr("placeholder","# reams")
      $.each(sales, function( index, value ){
            var log = $("<div class='row' id='log'>")
            var sal = $("<div class='col-md-3 p-2'>").text(sales[index].salesperson)
            var cli = $("<div class='col-md-3 p-2'>").text(sales[index].client)
            var rea = $("<div class='col-md-3 p-2'>").text(sales[index].reams)
            var del = $("<div class='col-md-3 p-2'>").html("<button class='btn btn-danger'>delete")
            log.append(sal, cli, rea, del)
            $(".all_logs").append(log)
            $(del).click(function(){
                  deletelog(this, index)
            })
      })



}
function disabledenter(){
      $("#clients").keypress(function(event) {
          if (event.keyCode == 13) {
              event.preventDefault();
          }
      })
      $("#reams").keypress(function(event) {
          if (event.keyCode == 13) {
              event.preventDefault();
          }
      })
}
function autocompleteclient(){
      $("#clients").autocomplete({
            source: clients
      })
}
function submitlog(client_name, reams_number){
      if (clients.includes(client_name) == false){
            clients.push(client_name)
      }
      var log = $("<div class='row' id='log'>")
      var sal = $("<div class='col-md-3 p-2'>").text("Shuai Hao")
      var cli = $("<div class='col-md-3 p-2'>").text(client_name)
      var rea = $("<div class='col-md-3 p-2'>").text(reams_number)
      var del = $("<div class='col-md-3 p-2'>").html("<button class='btn btn-danger'>delete")
      log.append(sal, cli, rea, del)
      var index = sales.push({salesperson: "Shuai Hao",client: client_name, reams: parseInt(reams_number)}) - 1 
      $(".all_logs").prepend(log)
      $(del).click(function(){
            deletelog(this, index)
      })
}
function getinput(){
      $(document).keyup(function(event){
            if (event.which ==13){
                  var client_name = $("#clients").val()
                  var reams_number = $("#reams").val()
                  if (client_name.length == 0){
                        alert("The client field is empty!")
                        $("#clients").focus()
                  }
                  else if(reams_number.length == 0){
                        alert("The reams field is empty!")
                        $("#reams").focus()
                  }
                  else if($.isNumeric(reams_number)==false){
                        alert("You should input number in the reams field!")
                        $("#reams").focus()
                  }
                  else{
                        submitlog(client_name, reams_number)
                        $("#clients").val("")
                        $("#reams").val("")
                        $("#clients").focus()
                  }
            }      
      })
      $("#submitbutton").click(function(){
            var client_name = $("#clients").val()
            var reams_number = $("#reams").val()
            if (client_name.length == 0){
                  alert("The client field is empty!")
                  $("#clients").focus()
            }
            else if(reams_number.length == 0){
                  alert("The reams field is empty!")
                  $("#reams").focus()
            }
            else if($.isNumeric(reams_number)==false){
                  alert("You should input number in the reams field!")
                  $("#reams").focus()
            }
            else{
                  submitlog(client_name, reams_number)
                  $("#clients").val("")
                  $("#reams").val("")
                  $("#clients").focus()
            }
            
      })
}

$(document).ready(function(){
      defaultlog();
      disabledenter();
      autocompleteclient();
      getinput();
});
