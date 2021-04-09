# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import random

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
		self.wfile.write(bytes("<p>this is my server:</p>", "utf-8"))
		self.wfile.write(bytes("<body>", "utf-8"))
		self.wfile.write(bytes("<p>it serves cats.</p>", "utf-8"))
		cats = ['https://cdn.britannica.com/91/181391-050-1DA18304/cat-toes-paw-number-paws-tiger-tabby.jpg', 'https://icatcare.org/app/uploads/2018/09/Scottish-fold.png', 'https://www.sciencenewsforstudents.org/wp-content/uploads/2020/05/1030_LL_domestic_cats.jpg', 'https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2020-07/kitten-510651.jpg?h=f54c7448&itok=ZhplzyJ9', 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg', 'https://i.natgeofe.com/n/3861de2a-04e6-45fd-aec8-02e7809f9d4e/02-cat-training-NationalGeographic_1484324.jpg?w=636&h=424', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlNyI5Bbsl1vq1BQjH9XA-Z4j0Kkk0cEpAnA&usqp=CAU', 'https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg', 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-girl-cat-names-1606245046.jpg', 'https://scx2.b-cdn.net/gfx/news/hires/2020/careforcatss.jpg', 'https://i.pinimg.com/originals/50/57/0c/50570c2f273b4c17471e174d756a721a.jpg', 'https://i.pinimg.com/originals/d1/ef/1e/d1ef1e9749e56edd43b8e05a8837a652.png', 'https://iheartcats.com/wp-content/uploads/2020/08/chachamaru_21_83209884_222080682159076_3592060361305647220_n.jpg', 'https://cdn.zmescience.com/wp-content/uploads/2016/01/Km0Icil.jpg']
		my_cat = random.choice(cats)
		self.wfile.write(bytes("<img src=%s width='400'>" % my_cat, "utf-8"))
		self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
	webServer = HTTPServer((hostName, serverPort), MyServer)
	print("Server started http://%s:%s" % (hostName, serverPort))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	print("Server stopped.")
