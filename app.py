import cbpro
import time

limits = {
    "alarm_1": 1900.00
}

class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["ETH-USD"]
        self.channels = ["ticker"]

    def on_message(self, msg):
        print(msg)

    def on_close(self):
        print("-- Goodbye! --")


wsClient = myWebsocketClient()
wsClient.start()
