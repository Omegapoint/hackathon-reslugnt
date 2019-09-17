try:
    import urequests as requests
except ImportError:
    import requests
import micropython

class DepartureBoard:
    
    def __init__(self, api_key, stop_id, direction_id, maxJourneys=2):
        self._base_url = "https://api.resrobot.se/v2/departureBoard?format=json&key={}&id={}&direction={}&maxJourneys={}".format(api_key, stop_id, direction_id, maxJourneys)
        self._data = None
    
    def refresh(self):
        micropython.mem_info(1)
        req = requests.get(self._base_url)
        print(self._base_url)
        self._data = req.json()
        req.close()
           
    
    def get_data(self):
        self.refresh()
        return self._data