
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
            console.log(data);
            render_line_graph(data, svg);
    }
);


svg = d3.select("#map")
    .append("svg")
    .attr("viewBox", [0, 0, 975, 610]);

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
var svg = d3.select("map")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

const render_map = state_data => {
    
    function format_state_data(data)  {
        var dataArray = [];
        for (var d = 0; d < data.length; d++) {
            dataArray.push(parseFloat(data[d].Value))
            
        }
        
        var minVal = d3.min(dataArray)
        var maxVal = d3.max(dataArray)
        var ramp = d3.scaleLinear().domain([minVal,maxVal]).range([lowColor,highColor])
        return(dataArray)
    }

    function comb_states_json(data){
        state_json = d3.json("../static/dataset/us.json")
        // Loop through each state data value in the .csv file
        for (var i = 0; i < data.length; i++) {

            // Grab State Name
            var dataState = data[i].State;

            // Grab data value 
            var dataValue = data[i].Value;

            // Find the corresponding state inside the GeoJSON
            for (var j = 0; j < state_json.features.length; j++) {
                var jsonState = state_json.features[j].properties.name;
                if (dataState == jsonState) {
                    // Copy the data value into the JSON
                    json.features[j].properties.value = dataValue;
                    // Stop looking through the JSON
                    break;
                }
            }       
        }

        return json;
    }

    formatted_state_depression = format_state_data(state_data)
    updated_json = comb_states_json( formatted_state_depression)
    console.log("Here")
    console.log(updated_json);
    // Bind the data to the SVG and create one path per GeoJSON feature
    svg.append("g")
      .selectAll("path")
      .data(updated_json.features)
      .enter()
      .append("path")
      .attr("d", path)
      .style("stroke", "#fff")
      .style("stroke-width", "1")
      .style("fill", function(d) { return ramp(d.properties.value) });

    // add a legend
    var w = 140, h = 300;

    var key = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h)
        .attr("class", "legend");

    var legend = key.append("defs")
        .append("svg:linearGradient")
        .attr("id", "gradient")
        .attr("x1", "100%")
        .attr("y1", "0%")
        .attr("x2", "100%")
        .attr("y2", "100%")
        .attr("spreadMethod", "pad");

    legend.append("stop")
        .attr("offset", "0%")
        .attr("stop-color", highColor)
        .attr("stop-opacity", 1);
        
    legend.append("stop")
        .attr("offset", "100%")
        .attr("stop-color", lowColor)
        .attr("stop-opacity", 1);

    key.append("rect")
        .attr("width", w - 100)
        .attr("height", h)
        .style("fill", "url(#gradient)")
        .attr("transform", "translate(0,10)");

    var y = d3.scaleLinear()
        .range([h, 0])
        .domain([minVal, maxVal]);

    var yAxis = d3.axisRight(y);

    key.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(41,10)")
        .call(yAxis)
};

console.log("Wut")
national_depression = d3.csv("../static/dataset/national_depression_by_state_1.csv").then(render_map)
