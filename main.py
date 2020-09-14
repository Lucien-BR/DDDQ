from app import MyApp
from requestsApi import RequestsApi

if __name__ == "__main__":
   #  MyApp.initApp()
    api = RequestsApi()
    print(api.getOverview("IBM"))

    
     