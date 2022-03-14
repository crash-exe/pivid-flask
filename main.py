from flask import Flask, request
from os import listdir, path


app = Flask(__name__, static_folder='usb')

@app.route('/')
def index():
	print(request.__dict__)
	return f'''
Hello!<br>
This is the index page<br>
Click <a href="usb">this url</a> to start browsing:)
'''

########################################################
def normal_links(p):
	l = listdir(p)
	html = ''
	for i in l:
		html += f'''<a href='/{p}/{i}'>{i}</a>\n<br>\n'''
	return html

@app.errorhandler(404)
def page(e):
	p = request.__dict__['path'][1:]
	html = 'Containing these folders:<br>\n'
	if path.isdir(p): html += normal_links(p)

	return html

app.run(host='0.0.0.0',port=80, debug=1)
