import os
import json
44  # import requests


# response = requests.get("https://opentdb.com/api.php", params=parameters)
# response.raise_for_status()

# filename = "generalQuestions.txt"
# filename = "week3content.txt"
# filename = "week4content.json"

# TODO#1: DO ALL QUIZZES TO PREP FOR FINAL EXAM:  

# filename = "PMCquizez/pmcWk1ch1IntroToPmc"
# filename = "PMCquizez/pmcWk1ch2PMandIT"
# filename = "PMCquizez/pmcWk2ch3ProcessGroups"
# filename = "PMCquizez/pmcwk3ch4Integration"
filename = "PMCquizez/pmcwk4ch5Scope"
# filename = "PMCquizez/pmcwk5ch6Schedule"

# filename = "PMCquizez/LABS/lab1"
# filename = "PMCquizez/LABS/lab2"
# filename = "PMCquizez/LABS/lab3"
# filename = "PMCquizez/LABS/lab4"




# filename = "PMCquizez/pmcwk6ch7Cost"
# filename = "PMCquizez/pmcwk6ch7Cost_to_learn"
# filename = "PMCquizez/pmcwk8ch8Quality"
# filename = "PMCquizez/wk9ch9ProjectResourceMngmt"
# filename = "PMCquizez/wk10ch10Communication"
# filename = "PMCquizez/wk10ch11Risk"
# filename = "PMCquizez/wk11ch12Procurement"
# filename = "PMCquizez/wk11ch13Stakeholders"
# filename = "PMCquizez/wk12closing"


# filename = "PMCquizez/LABS/lab5"
# filename = "PMCquizez/LABS/lab6"
# filename = "PMCquizez/LABS/lab7"
# filename = "PMCquizez/LABS/lab8"

# filename = "PMCquizez/midtermQuestions"
filename = "PMCquizez/finalExamPractice"


# C:\Users\Eric Rak\Desktop\semester4andHalf\quizAppSourceCode\quizDataFiles\PMCquizez\midtermQuestions.json
# PMCquizez\midtermQuestions

# filename = "webWeek3content"
# filename = "webWeek4content"
# filename = "webWeek5content"
# filename = "WEBquizez/webWeek7content"
# filename = "WEBquizez/webWeek10content"
# filename = "WEBquizez/webWeek11content"
# filename = "WEBquizez/webWeek12content"



fullFilename = filename + ".json"


directory = 'C:/Users/Eric Rak/Desktop/semester4andHalf/quizAppSourceCode/quizDataFiles/'
# directory = 'path/to'
# filename = fullFilename

file_path = os.path.join(directory, fullFilename)
print(file_path)  # Output: path/to/file.txt

# data = []
fileForLearning = os.path.join(directory, filename + "_to_learn.json")


setAttempts = 0


def updateFileFromObjectData(question_array):
    dict_array = []

    # we need to turn these objects into a regular dictionary array.
    for question in question_array:
        question_dict = {
            'question': question.question,
            'answer': question.answer,
            'incorrect': question.incorrect
        }
        dict_array.append(question_dict)

    data = {"results": dict_array, "setAttempts": setAttempts}

    # update the file.
    with open(fileForLearning, 'w+') as file:
        json.dump(data, file, indent=2, separators=(',', ': '))


try:
    with open(fileForLearning, 'r', encoding='utf-8') as file:
        # with open(fileForLearning + 'practice', 'r') as file:
        # with open(fileForLearning , 'r') as file:
        contents = file.read()
    data = json.loads(contents)
    if len(data["results"]) == 0:
        raise ValueError("No questions found in the results array.")
    print("reading from learning")

    try:
        data["setAttempts"] += 1

    except Exception as e:
        print("Error:", e)
        # there is no setCount Variable in the json file, we have to add it.

        data["setAttempts"] = 1  # Adding "setCount" variable with initial value

    print("increased setAttempts to: " + str(data["setAttempts"]))

    setAttempts = data["setAttempts"]

except (FileNotFoundError, ValueError) as e:
    print("Error:", e)
    with open(file_path, 'r', encoding='utf-8') as file:
        original_data = file.read()
    data = json.loads(original_data)
    try:
        data["setCount"] = data["setCount"] + 1

    except Exception as e:
        print("Error:", e)
        # there is no setCount Variable in the json file, we have to add it.

        data["setCount"] = 1  # Adding "setCount" variable with initial value
        # since it may be first time using this file, try to remove duplicate questions:

        duplicateDeletedCount = 0
        results = data["results"]
        length = len(results)
        i = 0

        while i < length:
            n = i+1
            # n = i
            while n < length:
                # n -= duplicateDeletedCount
                if i != n and results[i]["question"].lower() == results[n]["question"].lower():
                    results.pop(n)
                    duplicateDeletedCount += 1
                    length -= 1
                else:
                    n += 1
            i += 1
        print("Deleted duplicates: " + str(duplicateDeletedCount))

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    print("increased setCount to: " + str(data["setCount"]))

    # data = data['results']
    with open(fileForLearning, 'w+') as file:
        json.dump(data, file, indent=2, separators=(',', ': '))

question_data = data["results"]





