			var chartByQuart = AmCharts.makeChart(
				"cumulusQuarterchartdiv",{
					"type": "serial",
					"theme": "none",
					"pathToImages": "http://www.amcharts.com/lib/3/images/",
					"dataDateFormat": "YYYY-MM-DD JJ:NN:SS",
					"columnWidth": 0.1,
					"valueAxes": [{
						"id":"v1",
						"axisAlpha": 0,
						"position": "left"
					}],
					"graphs": [{
						"id": "g1",
						"type": "step",
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
						"minPeriod": "15mm"
					}
				}
			);

		        chartByQuart.loadJSON = function(url) {
				if (window.XMLHttpRequest) {
					var request = new XMLHttpRequest();
				} else {
					var request = new ActiveXObject('Microsoft.XMLHTTP');
				}
				request.open('GET', url, false);
				request.send();
				return eval(request.responseText);
			};
			var quartData = chartByQuart.loadJSON('appname/consoData.py?by=quart');
			chartByQuart.dataProvider = quartData;
			chartByQuart.invalidateSize();
