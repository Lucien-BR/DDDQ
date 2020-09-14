import json, requests

class RequestsApi(object):
    def __init__(self):
        self.base_uri = "https://www.alphavantage.co/"
        self.api_key = "FF6J2NVW0PWV8KA9"

    def getOverview(self, ticker):
        url = self.base_uri + "query?function=OVERVIEW&symbol=" + ticker + "&apikey=" + self.api_key

        response = requests.get(url)
        if response.status_code != 200:
            print("Didn't work: " + response.status_code)
            return 1

        return self.filterOverview(response.json())
        
    def filterOverview(self, rawData):
        light = {
            "ticker": rawData["Symbol"],
            "name": rawData["Name"],
            "exchange": rawData["Exchange"],
            "currency": rawData["Currency"],
            "country": rawData["Country"],
            "returnOn": {
                "assetsTTM": rawData["ReturnOnAssetsTTM"],
                "equityTTM": rawData["ReturnOnEquityTTM"],
            }
        }
        return light
