			var chartByDay = AmCharts.makeChart(
				"cumulusDayChartdiv",{
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
						"categoryBalloonDateFormat": "EEEE DD/MM/YYYY",
					},
					"categoryField": "date",
					"categoryAxis": {
						"parseDates": true,
						"dashLength": 1,
						"minorGridEnabled": true,
						"position": "top",
						"minPeriod": "DD"
					}
				}
			);

			chartByDay.loadJSON = function(url) {
				if (window.XMLHttpRequest) {
					var request = new XMLHttpRequest();
				} else {
					var request = new ActiveXObject('Microsoft.XMLHTTP');
				}
				request.open('GET', url, false);
				request.send();
				return eval(request.responseText);
			};
			var chartDataByDay = chartByDay.loadJSON('appname/consoData.py?by=day');
			chartByDay.dataProvider = chartDataByDay;
			chartByDay.invalidateSize();
