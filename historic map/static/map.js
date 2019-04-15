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

var city_url = "https://gist.githubusercontent.com/haoshuai999/8cf154c19be32079e8834aac7253bd65/raw/bb898762192e12f17b9d13ade901085b1a1e8dc0/city.geo.json";

Promise.all([d3.json(url), d3.json(city_url)]).then(function(data) {
  var country = data[0];
  var city = data[1]

  console.log(data)

  svg.append("path")
	.attr("d", path(country))
	.attr("fill", "lightgray")
	.attr("stroke", "white");
  
  svg.selectAll("circle")
	.data(city.features)
	.enter()
	.append("circle")
	.attr("r", 3.5)
	.attr("cx", function(d) {
		return projection(d.geometry.coordinates)[0]
	})
	.attr("cy", function(d) {
		return projection(d.geometry.coordinates)[1]
	})
	.attr("fill", "darkgreen")
	.attr("stroke", "white")
	.attr("stroke-width",15)
	.attr("stroke-opacity",0)
	.attr("opacity", 0.5)
	.on("mouseover",function(d,i){
		d3.select(this).style("fill","red")
		showdata(d)
	})
	.on("mouseout",function(d,i){
		d3.select(this).style("fill","darkgreen")
	})
  
  svg.selectAll("text")
	.data(city.features)
	.enter()
	.append("text")
	.attr("x", function(d) { 
		return projection(d.geometry.coordinates)[0]; 
	})
	.attr("y", function(d) { 
		return projection(d.geometry.coordinates)[1]; 
	})
	.text( function (d) { 
		return d.properties.name; 
	})
});

function showdata(data){
	$("#cityname").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center headline' id='cityname'>" + data.properties.name)
	$("#country").replaceWith("<div class='col-md-12 p-1' id='country'><b>Country: </b>" + data.properties.country)
	$("#population").replaceWith("<div class='col-md-12 p-1' id='population'><b>Population: </b>" + data.properties.population)
	$("#description").replaceWith("<div class='col-md-12 p-1' id='description'>" + data.properties.description)
	$("#builtdate").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center date' id='builtdate'>Built in: <b>" + data.properties.builtdate)
	$("#newname").replaceWith("<div class='col-md-12 p-2 border-bottom border-dark text-center headline' id='newname'>" + data.properties.newname)
	$("#newcountry").replaceWith("<div class='col-md-12 p-1' id='newcountry'><b>Country: </b>" + data.properties.newcountry)
	$("#newpopulation").replaceWith("<div class='col-md-12 p-1' id='newpopulation'><b>Population: </b>" + data.properties.newpopulation)
	$("#newdescription").replaceWith("<div class='col-md-12 p-1' id='newdescription'>" + data.properties.newdescription)
	$("#listeddate").replaceWith("<div class='col-md-12 px-2 border-bottom border-dark text-center date' id='listeddate'>Listed as Heritage: <b>" + data.properties.listeddate)
}