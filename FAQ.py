import random

class Node:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.neighbors = []

# questions = \
#     ["Does the caller claim to be from an official organization? (E.g, Police, Immigration)",
#      "Does the caller claim you need to act immediately or soon to avoid trouble/issues?",
#      "Is the caller asking for your bank details or credit card information?",
#      "Has the caller instructed you to install any software on your computer, such as team viewer?",
#      "Has the caller instructed you not to alert anyone, including the authorities and family?",
#      "Did the caller say you won the lottery/a prize in a competition you haven't partaken in?",
#      "The caller promised to make an investment with a promising return",
#      "The caller claims to have an easy job for you to make fast cash",
#      "Caller claims that this offer is for you, and only you exclusively.",
#      "Has the caller claimed that your family members are in trouble?",
#      "Does the caller claim to be your long lost friend?"]

# redflagcount = 0

# for i in questions:
#     print("Q", questions.index(i)+1, ".", i)
#     answer = input("Y/N : ")
#     answer = answer.lower()
#     answer = answer.replace(" ", "")
#     print(answer)

#     while answer != "y" and answer != "n":
#         print("Sorry, the input was not recognized. \nPlease input either Y or N (not case sensitive)")
#         print("Q", questions.index(i) + 1, ".", i)
#         answer = input("Y/N : ")
#         answer = answer.lower()
#         answer = answer.replace(" ", "")
#     if answer == "y":
#         redflagcount += 1
#     else:
#         redflagcount += 0

# print("The number of redflagcount is", redflagcount)
# if redflagcount <= 1:
#     print("Although the caller has not said anything too concerning, please exercise caution still.")
# elif redflagcount >1 <= 4:
#     print("There is a good chance this is a scam. Probs hangup now")
# elif redflagcount > 4:
#     print("this is def a scam")

#All the FAQ
faq = [
    {
        'question': 'What is vishing?',
        'answer': 'Vishing, short for "voice phishing," is a type of social engineering attack where scammers use phone calls or voice messages to deceive individuals into sharing sensitive information or performing certain, usually detrimental, actions. \nLink: https://www.fortinet.com/resources/cyberglossary/vishing-attack#:~:text=Contact%20Us,to%20gain%20a%20financial%20advantage.',
    },
    {
        'question': 'How do vishing attacks work?',
        'answer': 'Vishing attacks usually involve the scammer posing as a trustworthy entity, such as a bank representative, government official, or service provider. They oftne use persuasive tactics to manipulate victims into disclosing personal information, such as passwords, credit card details, or other types of personal information. \nLink: https://www.kaspersky.com/resource-center/definitions/vishing',
    },
    {
        'question': 'How can I identify a vishing attempt?',
        'answer': 'Vishing attempts often involve urgent or alarming messages that create a sense of panic or urgency. Scammers may pretend to address a security issue, account suspension, or offer exclusive deals. Be cautious if you receive unexpected calls requesting personal information or asking you to take immediate actions. \nLink: https://www.kaspersky.com/resource-center/definitions/vishing',
    },
    {
        'question': 'What should I do if I suspect a vishing attack?',
        'answer': "If you suspect a vishing attack, it's important to remain calm and not share any personally identifiable or financial information. Hang up the call and independently verify the caller's identity by contacting the official organisation directly using their official phone number or website. Report the incident to your local authorities or the organisation being impersonated. \nLink: https://us.norton.com/blog/online-scams/vishing",   
    },
    {
        'question': 'How can I protect myself from vishing attacks?',
        'answer': 'You can protect yourself by being cautious of unsolicited calls, never sharing sensitive information over the phone unless you initiated it, verifying the identity of the caller independently through official contact detals, keeping your personal information private and avoiding sharing it with unknown callers, regularly monitoring your financial accounts for any unauthorised activity, and considering using call-blocking services of apps to filter out potential vishing calls. \n A suggested website to use: https://www.dnc.gov.sg/index.html',
    },
    {
        'question': 'Are there any signs that can help me differentiate between a legitimate call and a vishing attempt?',
        'answer': 'Scammers may display some red flags, such as: \n-Requesting immediate action or creating a sense of urgency. \n-Pressuring you to disclose personal information or make payments.\n-Providing vague or inconsistent information. \n-Using threats or intimidation tactics. \n-Requesting payment through unconventional methods, such as gift cards or wire transfers.',
    },
    {
        'question': 'Can scammers spoof caller ID to make vishing calls appear legitimate?',
        'answer': "Yes, scammers can use caller ID spoofing techniques to make it appear as if the vishing calls are coming from a trusted entity or a legitimate phone number. It's important to remember that caller ID can be manipulated, so it's best if you independently verify the caller's identity.",
    },
    {
        'question': 'How can scammers obtain my phone number for vishing attacks?',
        'answer': "Scammers could potentially obtain phone numbers through various means, such as data breaches, public directories, social media profiles, or by purchasing lists from third-party sources. It's important to be cautious about sharing your phone number and consider privacy settings on online platforms.",
    }
]
#Creating the nodes
nodes = []
for item in faq:
    question = item['question']
    answer = item['answer']
    node = Node(question, answer)
    nodes.append(node)

#Randomising the connections between nodes (well more like shuffling the list of nodes)
random.shuffle(nodes)
for i in range(len(nodes) - 1):
    #Appends the neighbours to the nodes
    nodes[i].neighbors.append(nodes[i+1])

#Traveling through the graph
current_node = nodes[0]
while current_node:
    #Printing out the Q&A of the current node
    print("Question:", current_node.question)
    print("Answer:", current_node.answer, "\n")

    #Heads to a random neighbour of the current node
    if current_node.neighbors:
        current_node = random.choice(current_node.neighbors)
    else:
        print("For further reading, head to www.somewhere.com")
        break
    
