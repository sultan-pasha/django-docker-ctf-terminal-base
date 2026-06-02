import json
import threading
import docker
from channels.generic.websocket import WebsocketConsumer


class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.client = docker.from_env()
        self.container = self.client.containers.run(
            "alpine:latest",
            detach=True,
            tty=True,
            stdin_open=True,
            auto_remove=True,
            command="/bin/sh",
            user="1000:1000"
        )
        self.socket = self.container.attach_socket(params={
            'stdin': 1,
            'stdout': 1,
            'stderr': 1,
            'stream': 1
        })
        
        self.alive = True
        self.thread = threading.Thread(target=self.stream_container_output)
        self.thread.daemon = True
        self.thread.start()



    def disconnect(self, close_code):
        self.alive = False
        try:
            self.container.stop()
        except Exception:
            pass


    def receive(self, text_data):
        data = json.loads(text_data)
        command = data.get("data", "")
        if self.socket and self.alive:
            self.socket._sock.send(command.encode('utf-8'))


    def stream_container_output(self):
        while self.alive:
            try:
                data = self.socket._sock.recv(4096)
                if not data:
                    break
                self.send(text_data=json.dumps({
                    "data": data.decode('utf-8', errors='ignore')
                }))
            except Exception:
                break
        self.close()
