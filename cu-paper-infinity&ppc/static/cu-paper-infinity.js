// clients = [
//       "Shake Shack",
//       "Toast",
//       "Computer Science Department",
//       "Teacher's College",
//       "Starbucks",
//       "Subsconsious",
//       "Flat Top",
//       "Joe's Coffee",
//       "Max Caffe",
//       "Nussbaum & Wu",
//       "Taco Bell",
// ];

// var sales = [
//       {
//             "salesperson": "James D. Halpert",
//             "client": "Shake Shack",
//             "reams": 100
//       },
//       {
//             "salesperson": "Stanley Hudson",
//             "client": "Toast",
//             "reams": 400
//       },
//       {
//             "salesperson": "Michael G. Scott",
//             "client": "Computer Science Department",
//             "reams": 1000
//       },
// ]

var display_sales_list = function(sales){
      $("#all_logs").empty()

      if(sales.length == 0){
            var log = $("<div class='row'>")
            var no_log = $("<div class='col-md-4 p-2'>")
            $(no_log).append("No Sales")
            $(log).append(no_log)
            $("#all_logs").append(log)
      }
      else{
            $.each(sales, function( index, value ){
                  var log = $("<div class='row' p-1>")
                  var sal = $("<div class='col-md-3 p-2'></div>").append(sales[index].salesperson)
                  var cli = $("<div class='col-md-3 p-2'></div>").append(sales[index].client)
                  var rea = $("<div class='col-md-3 p-2'></div>").append(sales[index].reams)
                  var del = $("<div class='col-md-3 p-2'>")
                  var del_button = $("<button class='btn btn-danger'>delete</button>")
                  $(del_button).click(function(){
                        delete_sale(index)
                  })
                  $(del).append(del_button)
                  $(log).append(sal, cli, rea, del)
                  $("#all_logs").append(log)
      })
      }
}

var save_sale = function(new_sale){
      //sales.unshift(new_sale)

      //display_sales_list(sales)

      // client = new_sale["client"]
      // if ($.inArray(client, clients) < 0) {
      //       clients.push(client)
      // }
      $.ajax({
            type: "POST",
            url: "save_sale",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(new_sale),
            success: function(result){
                  var all_sale_logs = result["sales"]
                  var autocompleteclient = result["clients"]
                  sales = all_sale_logs
                  clients = autocompleteclient
                  display_sales_list(sales)
                  $("#clients").autocomplete({
                        source: clients
                  })
            },
            error: function(request, status, error){
                  console.log("Error");
                  console.log(request)
                  console.log(status)
                  console.log(error)
            }
      });


      $("#clients").val("")
      $("#reams").val("")
      $("#clients").focus()
}

var delete_sale = function(id){
      //sales.splice(id , 1)
      //display_sales_list(sales)
      $.ajax({
            type: "POST",
            url: "delete_sale",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(id),
            success: function(result){
                  var all_sale_logs = result["sales"]
                  sales = all_sale_logs
                  display_sales_list(sales)
            },
            error: function(request, status, error){
                  console.log("Error");
                  console.log(request)
                  console.log(status)
                  console.log(error)
            }
      });
}

var submitlog = function(){
      var sales_person = "Shuai Hao"
      var client_name = $("#clients").val()
      var reams_number = $.trim($("#reams").val())
      if ($.trim(client_name.length) == 0){
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
            new_sale =  {
                  "salesperson": sales_person,
                  "client": client_name,
                  "reams": reams_number
            }
            save_sale(new_sale)
      }
}

// function deletelog(object, index){
//       $(object).parentsUntil(".all_logs").remove()
//       sales.splice( index , 1)
//       console.log(sales)
// }
// function defaultlog(){
//       $("#clients").attr("placeholder","client")
//       $("#reams").attr("placeholder","# reams")
//       $.each(sales, function( index, value ){
//             var log = $("<div class='row' id='log'>")
//             var sal = $("<div class='col-md-3 p-2'>").text(sales[index].salesperson)
//             var cli = $("<div class='col-md-3 p-2'>").text(sales[index].client)
//             var rea = $("<div class='col-md-3 p-2'>").text(sales[index].reams)
//             var del = $("<div class='col-md-3 p-2'>").html("<button class='btn btn-danger'>delete")
//             log.append(sal, cli, rea, del)
//             $(".all_logs").append(log)
//             $(del).click(function(){
//                   deletelog(this, index)
//             })
//       })
// }
// function disabledenter(){
// }
// function autocompleteclient(){
//       $("#clients").autocomplete({
//             source: clients
//       })
// }
// function submitlog(client_name, reams_number){
//       if (clients.includes(client_name) == false){
//             clients.push(client_name)
//       }
//       var log = $("<div class='row' id='log'>")
//       var sal = $("<div class='col-md-3 p-2'>").text("Shuai Hao")
//       var cli = $("<div class='col-md-3 p-2'>").text(client_name)
//       var rea = $("<div class='col-md-3 p-2'>").text(reams_number)
//       var del = $("<div class='col-md-3 p-2'>").html("<button class='btn btn-danger'>delete")
//       log.append(sal, cli, rea, del)
//       var index = sales.push({salesperson: "Shuai Hao",client: client_name, reams: parseInt(reams_number)}) - 1 
//       $(".all_logs").prepend(log)
//       $(del).click(function(){
//             deletelog(this, index)
//       })
// }
// function getinput(){
//       $(document).keyup(function(event){
//             if (event.which ==13){
//                   var client_name = $("#clients").val()
//                   var reams_number = $("#reams").val()
//                   if (client_name.length == 0){
//                         alert("The client field is empty!")
//                         $("#clients").focus()
//                   }
//                   else if(reams_number.length == 0){
//                         alert("The reams field is empty!")
//                         $("#reams").focus()
//                   }
//                   else if($.isNumeric(reams_number)==false){
//                         alert("You should input number in the reams field!")
//                         $("#reams").focus()
//                   }
//                   else{
//                         submitlog(client_name, reams_number)
//                         $("#clients").val("")
//                         $("#reams").val("")
//                         $("#clients").focus()
//                   }
//             }      
//       })
//       $("#submitbutton").click(function(){
//             var client_name = $("#clients").val()
//             var reams_number = $("#reams").val()
//             if (client_name.length == 0){
//                   alert("The client field is empty!")
//                   $("#clients").focus()
//             }
//             else if(reams_number.length == 0){
//                   alert("The reams field is empty!")
//                   $("#reams").focus()
//             }
//             else if($.isNumeric(reams_number)==false){
//                   alert("You should input number in the reams field!")
//                   $("#reams").focus()
//             }
//             else{
//                   submitlog(client_name, reams_number)
//                   $("#clients").val("")
//                   $("#reams").val("")
//                   $("#clients").focus()
//             }
            
//       })
// }

$(document).ready(function(){
      display_sales_list(sales);
      $("#clients").attr("placeholder","client")
      $("#reams").attr("placeholder","# reams")
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
      $("#clients").autocomplete({
            source: clients
      })
      $("#submitbutton").click(function(){
            submitlog()
      })
      $("#reams").keyup(function(event){
            if (event.which ==13){
                  submitlog()
            }
      })
});
