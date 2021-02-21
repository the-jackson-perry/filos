/*
var margin = {top: 20, right: 20, bottom: 20, left:20},
    width = 400 - margin.left - margin.right,
    height = 400 - margin.top -margin.bottom;

var svg = d3.select("#linechart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + ";" + margin.top + ")");

const render_line_graph = (data, svg2) => {
        // Add X axis --> it is a date format
        var x = d3.scaleLinear()
          .domain([0,12])
          .range([ 0, width ]);
        svg2.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x));
    
        // Add Y axis
        var y = d3.scaleLinear()
          .domain([0, 50])
          .range([ height, 0 ]);
        svg2.append("g")
          .call(d3.axisLeft(y));
    
        // Show confidence interval
        svg2.append("path")
          .datum(data)
          .attr("fill", "#cce5df")
          .attr("stroke", "none")
          .attr("d", d3.area()
            .x(function(d) { 
                return x(d.Time_Period); })
            .y0(function(d) { return y(d.Low_CI) })
            .y1(function(d) { return y(d.High_CI) })
            )
    
        // Add the line
        svg2
          .append("path")
          .datum(data)
          .attr("fill", "none")
          .attr("stroke", "steelblue")
          .attr("stroke-width", 1.5)
          .attr("d", d3.line()
            .x(function(d) { return x(d.Time_Period) })
            .y(function(d) { return y(d.Value) })
            )
    
}

national_depression = d3.csv("../static/dataset/national_depression.csv")

national_depression.then( 
    data => {
            render_line_graph(data, svg);
    }
);
*/

const render_map = filename => {
    //Width and height of map
    var width = 960;
    var height = 500;

    var lowColor = '#f9f9f9'
    var highColor = '#bc2a66'

    // D3 Projection
    var projection = d3.geoAlbersUsa()
    .translate([width / 2, height / 2]) // translate to center of screen
    .scale([1000]); // scale things down so see entire US


    // Define path generator
    var path = d3.geoPath() // path generator that will convert GeoJSON to SVG paths
    .projection(projection); // tell path generator to use albersUsa projection

    //Create SVG element and append map to the SVG
    var svg = d3.select("#map")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    var dataArray = [];
    var dataArray2 = [];
    // Load in my states data!
    d3.csv(filename, function(data) {
        dataArray.push( {"Value":parseFloat(data.Value), "State": data.State })
        dataArray2.push( parseFloat(data.Value) );
    });

    console.log(dataArray2)
    var minVal = 17
    var maxVal = 38
    
    var ramp = d3.scaleLinear().domain([minVal,maxVal]).range([lowColor,highColor])

    // Load GeoJSON data and merge with states data
    d3.json("../static/dataset/us.json").then( f = json => {
        
        // Loop through each state data value in the .csv file
        for (var i = 0; i < dataArray.length; i++) {
            // Grab State Name
            var dataState = dataArray[i].State;
            // Grab data value 
            var dataValue = dataArray[i].Value;

            // Find the corresponding state inside the GeoJSON
            for (var j = 0; j < json.features.length; j++) {
                var jsonState = json.features[j].properties.name;
                if (dataState == jsonState) {
                    // Copy the data value into the JSON
                    json.features[j].properties.Value = dataValue;

                    // Stop looking through the JSON
                    break;
                }
            }
        }
        return json;
    }).then( f = json => {

            console.log(json.features);
                // Bind the data to the SVG and create one path per GeoJSON feature
            svg.selectAll("path")
                .data(json.features)
                .enter()
                .append("path")
                .attr("d", path)
                .style("stroke", "#fff")
                .style("stroke-width", "1")
                .style("fill", function(d) { 
                    return ramp(d.properties.Value) 
                });
    });
}

render_map("../static/dataset/national_depression_by_state_1.csv")
render_map("../static/dataset/national_depression_by_state_12.csv")