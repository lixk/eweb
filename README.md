# eweb
eweb is a fast and simple micro-framework for small web applications. Its goal is to enable you to develop
web applications in a simple and understandable way. 

With it, you don't need to know the HTTP protocol, or how Python communicates with JavaScript. 

## Usage

###Python
```python
from eweb import Server
import user

server = Server(port=5000)
server.services['user.login'] = user.login


def callback():
    print('server startup!!!')


server.run(callback=callback)

```

