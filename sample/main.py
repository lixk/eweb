from eweb import Server


def hello(name):
    return 'hello %s' % name


def callback():
    print('Server startup completed!')
    import webbrowser
    webbrowser.open('http://localhost:%s/index.html' % server.port)


if __name__ == '__main__':
    server = Server(port=5000)
    server.services['hello'] = hello
    import user
    server.services['user.login'] = user.login
    server.services['user.upload'] = user.upload

    server.run(callback=callback)
