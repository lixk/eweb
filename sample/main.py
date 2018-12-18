from eweb import Server
import user

server = Server(port=5000)
server.services['user.login'] = user.login


def callback():
    print('server startup!!!')


server.run(callback=callback)
