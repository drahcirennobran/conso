			var gaugeChart = AmCharts.makeChart(
			"cumulusGaugeChartdiv", {
				"type": "gauge",
				"pathToImages": "http://cdn.amcharts.com/lib/3/images/",
			        "arrows": [
                                   {
                                     "id": "GaugeArrow-1",
                                     "value": 87
			           }
			        ],
				"axes": [{
					"bottomText": "watt heure",
					"bottomTextYOffset": -20,
					"endValue": 3000,
					"id": "GaugeAxis-1",
					"valueInterval": 1000,
					"bands": [{
							"color": "#00CC00",
							"endValue": 1000,
							"id": "GaugeBand-1",
							"startValue": 0
						},
						{
							"color": "#ffac29",
							"endValue": 2000,
							"id": "GaugeBand-2",
							"startValue": 1000
						},
						{
							"color": "#ea3838",
							"endValue": 3000,
							"id": "GaugeBand-3",
							"innerRadius": "95%",
							"startValue": 2000
						}
					]
				}],
				"allLabels": [],
				"balloon": {},
				"titles": [{
					"id": "Title-1",
					"size": 15,
					"text": "Cumulus "
				}]
			}
			);

function updateSimpleValueFromWeb() {
var url="http://78.221.47.212/appname/consoInstantanee.py";
//url="http://78.221.47.212/appname/random.py";

                                if (window.XMLHttpRequest) {
                                        var request = new XMLHttpRequest();
                                } else {
                                        var request = new ActiveXObject('Microsoft.XMLHTTP');
                                }
                                request.open('GET', url, false);
                                request.send();
                                var value = eval(request.responseText);
console.debug(value);
  if(gaugeChart){
    if(gaugeChart.arrows){
      if(gaugeChart.arrows[0]){
        if(gaugeChart.arrows[0].setValue){
          gaugeChart.arrows[0].setValue(value);
          gaugeChart.axes[0].setBottomText(value + " watt heure");
        }
      }
    }
  }
}
gaugeChart.addListener("rendered", updateSimpleValueFromWeb);
setInterval(updateSimpleValueFromWeb, 1000);
