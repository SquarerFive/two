from aiohttp import web
import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    print("Receive Join")
    #return web.Response(text="Hello")
    #with open('index.html') as f:
    #data = await request.json()
    #print(data)
    return web.Response(text="Hello", content_type='text/html')
    #    return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
async def join_server(sid, data):
    print(data)
    await sio.emit("test" , data, broadcast=True)
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host="localhost", port= 2175)
