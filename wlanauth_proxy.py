from flask import Flask,request,abort
import requests


def authenticate_to_wlc():

#Change the url with the one used by your WLC and the username and password in the post_data. Of course the redirect_url of your choosing.
  
        url = "https://wlanauth.domain.com/login.html"



        post_data = {   "buttonClicked":"4",
                        "redirect_url":"www.msftconnecttest.com/redirect",
                        "err_flag":"0",
                        "info_flag":"0",
                        "info_msg":"0",
                        "username":"user",
                        "password":"pass"
                    }


        req_post = requests.post(url, data = post_data)





app = Flask(__name__)

@app.route('/', methods=['GET'])

def webhook():
    if request.method == 'GET':

        print("Got a GET request")
        authenticate_to_wlc()

        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)







