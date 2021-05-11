from flask import Flask
from auth import api_key_required
import json
import userList
import questionsList

app = Flask(__name__)

@app.route('/usersQuestions', methods = ['GET', 'POST'])
@api_key_required
def questionsHandler():
    question = questionsList.questions()
    return question

@app.route('/usersAnswer')
@api_key_required
def answersHandler():
    return json.dumps({})

@app.route('/lastQuestion')
@api_key_required
def lastQuestionHandler():
    return json.dumps({})

@app.route('/admin',methods = ['GET', 'POST'])
@api_key_required
def handler():
    user_list = userList.getList()
    return user_list

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

