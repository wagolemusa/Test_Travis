from flask import Flask, jsonify, abort, make_response, request
NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)



#data stractures
users = [
    {
        'id': 1,
        'name': 'reachird',
        'username': 'mudambi',
        'email': 'mudambi@gmail.com'
    },

    {
        'id': 2,
        'name': 'musa',
        'username': 'refuge',
        'email': 'refuge@gmail.com'

    },

    {
        'id':3,
        'name': 'deno',
        'username':'denny',
        'email': 'denny12@gmail.com'
    },
    {
        'id':4,
        'name' : 'fazali',
        'username':'faizos',
        'email':'faizoo@gmail.com'
    }
]
@app.route('/')
def index():
    return "<h1>Welcome To Maintenance Tracker</h1>"

# This methods Fetch all the requests of a logged in user
@app.route('/api/v1/users/requests', methods=['GET'])
def user_requests():
    return jsonify({'users':  users})


# This methods Fetch a request that belongs to a logged in user
@app.route('/api/v1/users/requests/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#This method Create a request. 
@app.route('/api/v1/users/requests/', methods=['POST'])
def create_request():
    if not request.json or not 'username' in request.json:
        abort(400)
    usr = {
        'id' : users[-1]['id'] + 1,
        'name' : request.json['name'],
        'username' : request.json['username'],
        'email' : request.json['email']
    }
    users.append(usr)
    return jsonify({'users': users})


#this methods Modify a request. the request
@app.route('/api/v1/users/requests/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type (request.json['name']) != unicode:
        abort(400)
    if 'username' in request.json and type (request.json['username']) != unicode:
        abort(400)
    if 'email' in request.json and type (requset.json['email']) is not unicode:
        abort(400)
    user[0]['user'] = request.json.get('name',user[0]['name'])
    user[0]['user'] = request.json.get('username', user[0]['username'])
    user[0]['user'] = request.json.get('email' , user[0]['email'])
    return jsonify({'user': user[0]})


if __name__ == '__main__':
    app.run(debug=True)


