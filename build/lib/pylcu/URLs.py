class URLs:
    def __init__(self, port: int):
        self.base_url = "127.0.0.1" + str(port)

        #Summoner
        self.summoner = '/lol-summoner/v1/current-summoner'

        #Queue
        self.ready_check = '/lol-matchmaking/v1/ready-check'
        self.accept_queue = '/lol-matchmaking/v1/ready-check/accept' #POST
        self.decline_queue = '/lol-matchmaking/v1/ready-check/decline' #POST
        self.matchmaking_search = '/lol-matchmaking/v1/search' #GET, POST, PUT, DELETE
        
        #Lobby
        self.position_preferences = '/lol-lobby/v2/lobby/members/localMember/position-preferences'
        self.lobby_queue_id = '/lol-lobby/v1/parties/queue'
        self.lobby_members = '/lol-lobby/v2/lobby/members'
        self.kick_member = '/lol-lobby/v2/lobby/members/{summonerId}/kick'.format(id="{summonerId}")
        self.promote_member = '/lol-lobby-team-builder/v1/lobby/members/{summonerId}/promote'.format(id="{summonerId}")

    def base_url(self):
        return self.base_url
    
    """SUMMONER"""
    def summoner_url(self):
        return self.base_url + self.summoner
    
    """MATCHMAKING"""
    def ready_check_url(self):
        return self.base_url + self.ready_check

    def accept_queue_url(self):
        return self.base_url + self.accept_queue
    
    def decline_queue_url(self):
        return self.base_url + self.decline_queue
    
    def matchmaking_search_url(self):
        return self.base_url + self.matchmaking_search
    
    "LOBBY"
    def set_position_preferences_url(self):
        return self.base_url + self.position_preferences
    
    def set_lobby_queue_id(self):
        return self.base_url + self.lobby_queue_id
    
    def get_lobby_members(self):
        return self.base_url + self.lobby_members
    
    def kick_lobby_member(self):
        return self.base_url + self.kick_member
    
    def promote_lobby_member(self):
        return self.base_url + self.promote_member