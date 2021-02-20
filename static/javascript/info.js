var margin = {top: 20, right: 20, bottom: 20, left:20},
    width = 230 - margin.left - margin.right,
    height = 400 - margin.top -margin.bottom;

var svg = d3.select("#linechart")
    .append("svg")
    .attr("width", width_margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + ";" + margin.top + ")");

d3.csv()

d3.csv("../dataset/national_depression.csv", function(data) {

    // Add X axis --> it is a date format
    var x = d3.scaleLinear()
      .domain([1,100])
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, 13])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Show confidence interval
    svg.append("path")
      .datum(data)
      .attr("fill", "#cce5df")
      .attr("stroke", "none")
      .attr("d", d3.area()
        .x(function(d) { return x(d.x) })
        .y0(function(d) { return y(d.CI_right) })
        .y1(function(d) { return y(d.CI_left) })
        )

    // Add the line
    svg
      .append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.x) })
        .y(function(d) { return y(d.y) })
        )

})


const render = data => {

}