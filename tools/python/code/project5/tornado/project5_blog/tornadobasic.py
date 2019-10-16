import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self,*args,**kwarg):
        self.write("hello world")
    def post(self,*args,**kwargs):
        pass


app = Application(handlers=[('/',IndexHandler)])
server = HTTPServer(app)
server.listen(80)
IOLoop.current().start()