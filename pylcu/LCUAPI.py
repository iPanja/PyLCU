import requests, json
from requests.auth import HTTPBasicAuth
from requests.models import InvalidURL

from pylcu.URLs import *

import urllib3

urllib3.disable_warnings()

class LCUAPI:
    def __init__(self, port: int, password: str):
        self.url = URLs(port)
        self.auth = HTTPBasicAuth('riot', password)
    
    """Helper Methods"""
    #Requests response to json
    def __format_response(self, response: requests.models.Response) -> str:
        try:
            return response.json()
        except Exception:
            return response
    #GET request
    def __get_data(self, url, parameters=None):
        return self.__format_response(requests.get(url, auth=self.auth, verify=False, params=parameters))
    def __post_data(self, url, data=None):
        return self.__format_response(requests.post(url, auth=self.auth, verify=False, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'}))
    def __put_data(self, url, data=None):
        return self.__format_response(requests.put(url, auth=self.auth, verify=False, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'}))
    def __delete_data(self, url):
        return self.__format_response(requests.delete(url, auth=self.auth, verify=False))
    
    """PROPERTIES"""
    @property
    def isConnected(self) -> bool:
        #Find a generic endpoint with a consistent response to test connection
        try:
            return self.__get_data(self.url.summoner_url()) != None
        except InvalidURL:
            return False

    """WRAPPER CALLS"""
    #SUMMONER
    def get_summoner(self):
        return self.__get_data(self.url.summoner_url())
    #QUEUE
    def get_ready_check(self):
        return self.__get_data(self.url.ready_check_url())
    def accept_ready_check(self):
        return self.__post_data(self.url.accept_queue_url())
    def decline_ready_check(self):
        return self.__post_data(self.url.decline_queue_url())
    def matchmaking_search(self):
        return self.__post_data(self.url.matchmaking_search_url())
    def matchmaking_leave(self):
        return self.__delete_data(self.url.matchmaking_search_url())
    #LOBBY
    def set_position_preferences(self, primary: str, secondary: str):
        #valid_options = ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "SUPPORT"]
        payload = {
            "firstPreference": primary.upper(),
            "secondPreference": secondary.upper()
        }
        print(json.dumps(payload))
        return self.__put_data(self.url.set_position_preferences_url(), data=payload)
    def set_lobby_queue_id(self, id: int):
        return self.__put_data(self.url.set_lobby_queue_id(), data=id)
    def get_lobby_members(self):
        return self.__get_data(self.url.get_lobby_members())
    def kick_lobby_member(self, summonerId: int):
        return self.__post_data(self.url.kick_lobby_member().format(summonerId=str(summonerId)), data=summonerId)
    def promote_lobby_member(self, summonerId: int):
        return self.__post_data(self.url.promote_lobby_member().format(summonerId=str(summonerId)), data=summonerId)
    
    """WEBSOCKETS"""
    #TODO...

    """CUSTOM"""
    def get(self, endpoint):
        return self.__get_data(self.url.base_url + endpoint)