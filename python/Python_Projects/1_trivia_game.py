import random
questions={
    "What keyword is used to import a module in python?":"import",
    "What is the extension used to save a python file?":".py",
    "Which keyword is used to define a function?":"def",
    "How to access list l having i values in reverse order?":"l[-i]",
    "What is the built in function used to find max element in a list ?":"max()",
    "What is the built in function used to find min element in a list ?":"min()"
}

questions_list=list(questions.keys())
#print(questions_list)
total_questions=3
score=0

selected_questions_list=random.sample(questions_list,total_questions)
#print(selected_questions_list)

for i,qn in enumerate(selected_questions_list):
    #print(question)
    print(f"{i+1}.{qn}")
    correct_ans=questions[qn]
    user_input=input("Enter your answer:").lower().strip()
    if correct_ans==user_input:
        print("Your answer is correct !")
        score+=1
    else:
        print("Your answer is wrong and the correct answer is ",correct_ans)

print(f"\nYour final score:{score}/{total_questions}\n")
