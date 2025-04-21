from flask import Flask # type: ignore
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'

from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}
]

from flask import request # type: ignore

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

todos = [
    {
        "label": "Sample Todo",
        "done": False
    }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Step 2: Convert the request body to a Python dictionary
    request_body = request.json  # This converts the JSON body to a Python dictionary
    print("Incoming request with the following body", request_body)

    todos.append(request_body)

    return jsonify(todos)  

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True) 
    
@app.route('DELETE/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return jsonify(todos)