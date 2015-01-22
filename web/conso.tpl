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

chart = AmCharts.makeChart("chartdiv",{
	   "type": "serial",
	   "theme": "none",
           "pathToImages": "http://www.amcharts.com/lib/3/images/",
           "dataDateFormat": "YYYY-MM-DD JJ:NN:SS",
          "valueAxes": [{
            "id":"v1",
            "axisAlpha": 0,
            "position": "left"
        }],
        "graphs": [{
	   "id": "g1",
            "lineThickness": 2,
	   "fillAlphas": 0.4,
            "title": "red line",
            "valueField": "mwh"
        }],
        "chartScrollbar": {
	   "graph": "g1",
	   "scrollbarHeight": 50
	   },
        "chartCursor": {
            "cursorPosition": "mouse",
            "pan": true,
	   "categoryBalloonDateFormat": "JJ:NN:SS",
        },
        "categoryField": "date",
        "categoryAxis": {
            "parseDates": true,
            "dashLength": 1,
            "minorGridEnabled": true,
            "position": "top",
	   "minPeriod": "mm"
        },

	   "dataProvider": [
           ${data}
	   ]
});
chart.addListener("rendered", zoomChart);
chart.invalidateSize();
zoomChart();
function zoomChart(){
    chart.zoomToIndexes(chart.dataProvider.length - 40, chart.dataProvider.length - 1);
}

</script>
</head>

<body>
    <div id="chartdiv" style="width: 1024px; height: 768px;"></div>
</body>
</html>
