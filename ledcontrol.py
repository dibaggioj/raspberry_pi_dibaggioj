import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

class LedHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print "Connection opened"
		self.write_message("Client: connection opened")

	def on_close(self):
		print "Connection closed"

	def on_message(self, message):
		print "Message received: {}".format(message)
		self.write_message("Message received.")

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", LedHandler)])
	server = tornado.httpserver.HTTPServer(app)
	server.listen(9000)
	tornado.ioloop.IOLoop.instance().start()
