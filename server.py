import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Dipendra\n")
        print(self.request)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        ])

if _name_ ++ "_main_":
   app = make_app()
   app.listen(8888)
   tornado.ioloop.IOLoop.current().start()
