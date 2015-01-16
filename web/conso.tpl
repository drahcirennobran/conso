<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Consommation du cumulus</title>
<script src="../amcharts/amcharts.js" type="text/javascript"></script>
<script src="../amcharts/serial.js" type="text/javascript"></script>
<script type="text/javascript">
           var chart;
            var graph;

	var chartData = [{
		"country": "USA",
		"visits": 4252
	}, {
		"country": "China",
		"visits": 1882
	}, {
		"country": "Japan",
		"visits": 1809
	}, {
		"country": "Germany",
		"visits": 1322
	}, {
		"country": "UK",
		"visits": 1122
	}, {
		"country": "France",
		"visits": 1114
	}, {
		"country": "India",
		"visits": 984
	}, {
		"country": "Spain",
		"visits": 711
	}, {
		"country": "Netherlands",
		"visits": 665
	}, {
		"country": "Russia",
		"visits": 580
	}, {
		"country": "South Korea",
		"visits": 443
	}, {
		"country": "Canada",
		"visits": 441
	}, {
		"country": "Brazil",
		"visits": 395
	}, {
		"country": "Italy",
		"visits": 386
	}, {
		"country": "Australia",
		"visits": 384
	}, {
		"country": "Taiwan",
		"visits": 338
	}, {
		"country": "Poland",
		"visits": 328
	}];
AmCharts.ready(function() {
chart = new AmCharts.AmSerialChart();
chart.dataProvider = chartData;
chart.categoryField = "country";

var categoryAxis = chart.categoryAxis;
categoryAxis.autoGridCount  = false;
categoryAxis.gridCount = chartData.length;
categoryAxis.gridPosition = "start";
categoryAxis.labelRotation = 90;

graph = new AmCharts.AmGraph();
graph.valueField = "visits";
graph.type = "column";
graph.fillAlphas = 0.8;
chart.addGraph(graph);
chart.write('chartdiv');
});
</script>
</head>

<body>
    <div id="chartdiv" style="width: 640px; height: 400px;"></div>
</body>
</html>
