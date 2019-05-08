var width = 950, 
	height = 550;
var svg = d3.select("svg")
			.attr("width",width)
			.attr("height",height);
var projection = d3.geoMercator()
				.center([44,35])
				.scale(800)
				.translate([width/2.5, height/2.5]);
var path = d3.geoPath().projection(projection);

var url = "https://gist.githubusercontent.com/haoshuai999/c2ef0b5f71808bbb2cfd7166704db4af/raw/f2b4a24518785fbcb6248befc4dbb753cb8b1602/alexander.geo.json";

var city_url = "https://gist.githubusercontent.com/haoshuai999/8cf154c19be32079e8834aac7253bd65/raw/1bf0b82aff16461c8602563d9f59c697d83bb36b/city.geo.json";

d3.json(url).then(function(data) {
  var country = data;

  svg.append("g")
	.attr("id","d3map")
	.append("path")
	.attr("d", path(country))
	.attr("fill", "lightgrey")
	.attr("stroke", "white");
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
				.attr("r", 5.5)
				.attr("cx", function(d) {
					return projection(d.geometry.coordinates)[0]
				})
				.attr("cy", function(d) {
					return projection(d.geometry.coordinates)[1]
				})
				.style("fill", "red")
				.attr("opacity", 0.6)

			svg.select("#d3map").selectAll("text")
				.data(city)
				.enter()
				.append("text")
				.transition()
				.duration(500)
				.style("fill","red")
				.style("font-weight","bold")
				.attr("x", function(d) { 
					return (projection(d.geometry.coordinates)[0] + 5);; 
				})
				.attr("y", function(d) { 
					return projection(d.geometry.coordinates)[1]; 
				})
				.text( function (d) { 
					return d.properties.name; 
				})
			
			svg.selectAll("circle:not(:last-child)")
				.style("fill","black")

			svg.selectAll("text:not(:last-child)")
				.style("fill","black")
		}, 500);
	});
}