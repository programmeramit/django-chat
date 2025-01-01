from channels.generic.websocket import AsyncWebsocketConsumer,SyncConsumer
import json
import asyncio
from asgiref.sync import async_to_sync
import time

class ChatApp(SyncConsumer):

    def websocket_connect(self, event):
        self.group_name = self.scope["url_route"]["kwargs"]["group"]

        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
    
   
        data = json.loads(event["text"])
        print(data["users"])
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            "type":"chat.message",
            "message":{
                "message":data["content"],
                "user":data["users"]
            },
        })
        
    def websocket_disconnect(self,event):
        print("websocket disconnected")
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        
        
    def chat_message(self,event):
        data = event["message"]
        print(data)
        message = data.get('message', '')
        username = data.get('user', '')

            # Send multiple data back to the WebSocket
        response_data = {
                "message": message,
                "username": username,
                "status": "Message received",
                "timestamp":time.ctime()
            }

        self.send({
                "type": "websocket.send",
                "text": json.dumps(response_data),
            })

