var width = 1000, 
	height = 600;
var svg = d3.select("svg")
			.attr("width",width)
			.attr("height",height);
var projection = d3.geoMercator()
				.center([44,33])
				.scale(800)
				.translate([width/2.5, height/2.5]);
var path = d3.geoPath().projection(projection);

var url = "https://gist.githubusercontent.com/haoshuai999/c2ef0b5f71808bbb2cfd7166704db4af/raw/f2b4a24518785fbcb6248befc4dbb753cb8b1602/alexander.geo.json";

var city_url = "https://gist.githubusercontent.com/haoshuai999/8cf154c19be32079e8834aac7253bd65/raw/b32e602ae56a59c2546ba88b21f5c9be3e0b1a08/city.geo.json";

d3.json(url).then(function(data) {
  var country = data;

  svg.append("g")
	.attr("id","d3map")
	.append("path")
	.attr("d", path(country))
	.attr("fill", "#fed766")
	.attr("stroke", "white")
});

function addcity(page){
	d3.json(city_url).then(function(data) {
		city = []
		for (var i = 0; i < page; i++) {
			city.push(data.features[i])
		}
		setTimeout(function(){
			svg.select("#d3map").selectAll("circle")
				.data(city)
				.enter()
				.append("circle")
				.transition()
				.duration(500)
				.attr("r", 7.5)
				.attr("cx", function(d) {
					console.log(city)
					return projection(d.geometry.coordinates)[0]
				})
				.attr("cy", function(d) {
					return projection(d.geometry.coordinates)[1]
				})
				.attr("fill", "black")
				.attr("opacity", 0.75)
				.attr("stroke", "white")
				.attr("stroke-width",25)
				.attr("stroke-opacity",0)

			svg.select("#d3map").selectAll("text")
				.data(city)
				.enter()
				.append("text")
				.transition()
				.duration(500)
				.attr("fill", "black")
				.style("font-weight","bold")
				.attr("x", function(d) { 
					return (projection(d.geometry.coordinates)[0] + 5); 
				})
				.attr("y", function(d) { 
					return projection(d.geometry.coordinates)[1]; 
				})
				.text( function (d) { 
					return d.properties.name; 
				})
				});
		}, 1000);
}
function addhover(){
	setTimeout(function(){
		svg.selectAll("circle")
			.on("mouseover",function(d,i){
				d3.select(this).style("stroke-opacity",1)
				showdata(d)
			})
			.on("mouseout",function(d,i){
				d3.select(this).style("stroke-opacity",0)
			})
	}, 500);
}
function showdata(data){
	$("#city").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center' id='city'>" + data.properties.name)
	$("#cityimg").replaceWith("<div class='col-md-12 p-2' id='cityimg'><img src='" + data.properties.image + "' alt='cityimage' class='img-fluid'>")
	$("#key1").replaceWith("<li id='key1'>" + data.properties.key1)
	$("#key2").replaceWith("<li id='key2'>" + data.properties.key2)
	//$("#builtdate").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center date' id='builtdate'>Built in: <b>" + data.properties.builtdate)
	// $("#newname").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center headline' id='newname'>" + data.properties.newname)
	// $("#newcountry").replaceWith("<div class='col-md-12 p-1' id='newcountry'><b>Country: </b>" + data.properties.newcountry)
	// $("#newpopulation").replaceWith("<div class='col-md-12 p-1' id='newpopulation'><b>Population: </b>" + data.properties.newpopulation)
	// $("#newdescription").replaceWith("<div class='col-md-12 p-1' id='newdescription'>" + data.properties.newdescription)
	// $("#listeddate").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center date' id='listeddate'>Listed as Heritage: <b>" + data.properties.listeddate)
}