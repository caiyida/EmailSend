#Import libraries
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

#log in page
@app.route('/')
def form():
    return render_template('form_submit.html')

#Authentication function
@app.route('/login', methods=['POST'])
def login():
    sdr = request.form['username']
    pw = request.form['password']
    host = request.form['host']
    port = request.form['port']
    print (type(port))
    svr = smtplib.SMTP(host,int(port))
    svr.starttls()
    try:
        svr.login(sdr,pw)
        #return svr
        #return json.dumps({'login':'true'})
        return render_template('form_action.html')
    except smtplib.SMTPAuthenticationError:
        #return None
        #return json.dumps({'login':'false'})
        return render_template('login_fail.html')
        

#message editing and send email 
#@app.route('/sendmail', methods=['POST'])
#def emailsend(sdr,recr,sub,body,svr):
#    msg = MIMEMultipart()
#    msg['From'] = sdrd
#    msg['To'] = recr
#    msg['Subject'] = sub
#    msg.attach(MIMEText(body))
#    try:
#        svr.sendmail(sdr,recr,msg.as_string())
#        return json.dumps({'sendmail':'true'})
#    except Exceptions:
#        return json.dumps({'sendmail':'false'})

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
      #app.run(host='0.0.0.0', port=1024)
