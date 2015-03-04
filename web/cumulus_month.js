			var chartByMonth = AmCharts.makeChart(
				"cumulusMonthChartdiv",{
					"type": "serial",
					"theme": "none",
					"pathToImages": "http://www.amcharts.com/lib/3/images/",
					"dataDateFormat": "YYYY-MM-DD",
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
						"categoryBalloonDateFormat": "DD/MM/YYYY",
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

			chartByMonth.loadJSON = function(url) {
				if (window.XMLHttpRequest) {
					var request = new XMLHttpRequest();
				} else {
					var request = new ActiveXObject('Microsoft.XMLHTTP');
				}
				request.open('GET', url, false);
				request.send();
				return eval(request.responseText);
			};
			var dataByMonth = chartByMonth.loadJSON('appname/consoData.py?by=month');
			chartByMonth.dataProvider = dataByMonth;
                        chartByMonth.invalidateSize();
