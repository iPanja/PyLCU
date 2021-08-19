# PyLCU
A Python wrapper for the League of Legends Client (LCU). This will not contain every endpoint available but the ones I need to use for other projects.

This was created to better understand the LCU and its API as well as to create a tool to automate champion selection.

# Usage
``` python
port, password = Credentials.fetch()
lcu = LCUAPI(port, password)

if lcu.isConnected:
    lcu.set_position_preferences("MIDDLE", "JUNGLE")
    lcu.enter_matchmaking()
```

# Acknowledgements
This wouldn't have been possible if not for the documentation provided by [hextechdocs.dev](https://hextechdocs.dev/).