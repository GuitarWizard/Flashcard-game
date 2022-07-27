"""1. Modify the data.py file (don't change the main.py)
2. Make a get() request to fetch 10 True or false questions.
3. Parse the JSON response and replace the value of question_data (don't change the variable name)
hint: Creat a python dictionary for the aount and type parameters"""

import requests, json
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}
# quiz_questions_response = requests.get(url="https://opentdb.com/api.php?amount=10&category=20&type=boolean")
quiz_questions_response = requests.get(url="https://opentdb.com/api.php", params = PARAMETERS)
quiz_questions_response.raise_for_status()
quiz_questions_response = quiz_questions_response.json()
# print(quiz_questions_response)

# questions = quiz_questions_response["results"][0]["question"]
# print(questions)


question_data = quiz_questions_response["results"]


