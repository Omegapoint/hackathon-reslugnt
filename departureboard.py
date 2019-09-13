try:
    import urequests as requests
except ImportError:
    import requests

class DepartureBoard:
    
    def __init__(self, api_key, stop_id):
        self._base_url = "https://api.resrobot.se/v2/departureBoard?format=json&key={}&id={}&maxJourneys=1".format(api_key, stop_id)
        self._data = None
    
    def refresh(self):
        req = requests.get(self._base_url)
        self._data = req.json()
        req.close()
    
    def get_data(self):
        self.refresh()
        return self._data