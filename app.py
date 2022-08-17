from flask import *
from datetime import datetime
from f2a import get_2fa
from id_fb import get_idfb, cookie_to_uid
from mail import get_mail, get_pass

import os
import platform
import psutil

app = Flask(__name__)

# =======================Home Page=================================
@app.route('/', methods=['GET'])
def homepage():
	the_time = datetime.now().strftime("%m-%d-%Y %T:%M%p")
	return render_template("home.html",the_time=the_time)



#===========================download file================================
@app.route('/return-files', methods=['GET'])
def return_files_tut():
	try:
		file = str(request.args.get('file'))
		return send_file(file, attachment_filename=file)
	except Exception as e:
		return str(e)
	

	
#========================upload file=====================================
@app.route('/upload')  
def upload():
	return render_template("file_upload_form.html")
 
@app.route('/success', methods = ['POST'])  
def success():
	if request.method == 'POST':  
		f = request.files['file']  
		f.save(f.filename)  
		return render_template("success.html", name = f.filename)  



#=================================get totp===============================
@app.route('/2fa', methods=['GET','POST'] )
def _2fa():
	if request.method == 'POST':
		code = request.form['text']
		try:
			code_f2a = get_2fa(code)
			txt1 = f"Code F2A: {code_f2a}"
			txt2 = str(code)
			return render_template("f2a.html", code=txt1,f2a=txt2)  
		except:
			return render_template("f2a.html", code="Code Error")

	elif request.method == 'GET':
		return render_template("f2a.html",code="",f2a="N7NZYJTBXUQ6VHGQN3SDZ3INHQUQPUZX")


@app.route('/id_fb', methods=['GET','POST'] )
def _idfb():
	if request.method == 'POST':
		link = request.form['text']
		try:
			id = get_idfb(link)['id']
			txt1 = f"ID Facebook: {id}"
			return render_template("idfb.html", link1=txt1,link2=link)  
		except:
			return render_template("idfb.html", link1="Link Error", link2="https://www.facebook.com/thinhmaz90/")

	elif request.method == 'GET':
		return render_template("idfb.html", link2="https://www.facebook.com/thinhmaz90/")


# ==============================================================
@app.route('/client')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> Your IP address is:' + ip_addr


@app.route('/client')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Your IP address is:' + ip_addr


@app.route('/getinfo')
def getinfo():
	s = ""
	arr = os.listdir(os.path.normpath(os.getcwd()))
	for i in arr :
		s +=f"<h1>{str(i)}</h1>\n"
	return s

@app.route('/getinfopc')
def getinfopc():
	_os,_bit = platform.architecture()
	_memory = psutil.virtual_memory().total
	txt = f"""
	<h1><a href="/" class="home">Home Page</a></h1>
	<h3>Machine: {platform.architecture()}</h3>
	<h3>Ram: ({int(psutil.virtual_memory().total /1000000)})</h3>
"""
	return txt
# =============================Get Messenger Temp Mail===========================
@app.route('/mail10p', methods=['GET','POST'])
def mail10p():
	if request.method == 'POST':
		pass
	elif request.method == 'GET':
		pass
	return ""
#================================================================================
@app.route('/miningmail', methods=['GET'])
def mining_mail():
	if request.method == 'GET':
		return f"""
		<h1><a href="/" class="home">Home Page</a></h1>
		<form action = "/miningmail" method = "get">
			<input type = "submit" value="Reset"> 
		</form>
		<p>{get_mail()}|{get_pass()}</p>
		"""
	elif request.method == 'POST':
		return f"{get_mail()}|{get_pass()}"

@app.route('/cookie2uid', methods=['GET'])
def cookie2uid():
	if request.method == 'GET':
		try:
			cookies_string = str(request.args.get('cookies'))
			uid = cookie_to_uid(cookies_string)
			txt = f"ID Facebook: {uid}"
			return render_template("cookie2uid.html",link1=txt,link2 = cookies_string)
		except:
			return render_template("cookie2uid.html",link2="c_user=123;xs=xxx;sb=xxx;datr=xxx")

	elif request.method == 'POST':
		cookies_string = request.form.get('cookies')
		uid = cookie_to_uid(cookies_string)
		return uid

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

