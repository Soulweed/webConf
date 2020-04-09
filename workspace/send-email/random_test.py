from random import randint
from flask import Flask, request
from flask_ngrok import run_with_ngrok
from flask import jsonify
import json

app = Flask(__name__)
run_with_ngrok(app)

ans = 6
@app.route('/guess', methods = ['POST'])
def guess():
    try :
        # ans = randint(1,12)
        data = json.loads(request.data)
        print(data)
        username = data.get('user')
        number = data.get('guess')
        print(number, ans)
        if number == ans:
            
            return jsonify({'result': 'You Win', 'username': username }), 200
        elif number > ans :
            return jsonify({'result' : 'Try Again', 'msg' : 'More'}) , 200
        else :
            return jsonify({'result' : 'Try Again', 'msg' : 'Less'}) , 200

    except Exception as err:
        print(err)
        return jsonify({'result' : 'Somthing wrong !'}), 200

@app.route('/setnum', methods = ['POST'])
def set_num():
    
    data = json.loads(request.data)
    user = data.get('user')
    passwd = data.get('pass')
    if user == '499755' and passwd == '1234':
        global ans
        ans = randint(1,12)
        print(str(ans)+ "----")
        return jsonify({'status' : 'New number set'})
    else:
        return jsonify({'status' : 'You are not Authorize'})

    
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/random')
# def rand_func():
#     r = randint(1,50)
#     return '<h1 style="font-size:300px; text-align:center">{}</h1>'.format(r)


if __name__ == '__main__':
    app.run()

