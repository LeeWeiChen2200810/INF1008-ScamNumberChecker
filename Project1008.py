import json

class Node:
    def __init__(self, question):
        self.question = question
        self.next = None

# Load questions from JSON file
def load_questions():
    try:
        with open('./Data/questions.json', 'r') as file:
            questions_data = json.load(file)
        return questions_data
    except FileNotFoundError:
        print("Error: The questions JSON file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse the questions JSON file.")
        return []

# Create linked list of nodes from questions
questions = load_questions()
head = None
prev = None
for question_data in questions:
    question_text = question_data['question']
    node = Node(question_text)

    if prev is None:
        head = node
    else:
        prev.next = node

    prev = node

# Perform the questionnaire
redflagcount = 0
current = head
while current is not None:
    print(redflagcount)
    print(current.question)
    answer = input("Y/N: ").lower().strip()

    while answer != "y" and answer != "n":
        print("Sorry, the input was not recognized. Please input either Y or N (not case sensitive)")
        answer = input("Y/N: ").lower().strip()

    if answer == "y":
        redflagcount += 1

    current = current.next

print("The number of red flags is", redflagcount)
if redflagcount <= 1:
    print("Although the caller has not said anything too concerning, please exercise caution.")
elif 1 < redflagcount <= 2:
    print("There is a good chance this is a scam. You should probably hang up now.")
elif redflagcount > 2:
    print("This is definitely a scam.")


