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