import subprocess, shlex, re, platform, click
from typing import Tuple

class ConnectionTool:
    #Get string containing app_port and password from League process output
    @staticmethod
    def __getProccessInfo() -> str:
        if platform.system() == "Windows":
            cmd = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline"
        else: #Linux/Mac OS
            cmd = "ps -A grep LeagueClientUx"

        proc = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.DEVNULL)
        
        output = proc.stdout
        return output
    #Parse the app_port and password from __getProcessInfo() - {app_port, password}
    @staticmethod
    def getLockfileInfo() -> Tuple[int, str]:
        try:
            info = ConnectionTool.__getProccessInfo()
            app_port = re.search('--app-port=([0-9]*)', info).group()
            remoting_auth_token = re.search('--remoting-auth-token=([-\w_]*)', info).group()
            if app_port == None or remoting_auth_token == None:
                print("App Port/Remoting Auth Token not found in lockfile")
                return False
            app_port = app_port.split('=')[1]
            password = remoting_auth_token.split('=')[1]

            return (int(app_port), password)
        except AttributeError:
            return False
    @staticmethod
    def fetch_credentials() -> Tuple[int, str]:
        while True:
            try:
                app_port, password = ConnectionTool.getLockfileInfo()
                return (app_port, password)
            except TypeError:
                return False