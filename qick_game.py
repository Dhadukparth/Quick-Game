print("----------------------------------------------------------------------------------------------------")
# import quick_game_module as qgm

playgame = input("You are play the quick game (Y/N) : ").lower()

if playgame != "y":
    quit()

questionlist = [
    ['1', 'HTML full form', 'Hyper Text make learn', 'Hyper transfer Maker Language', 'Hyper Text Markup Language', 'Hyper Text Many Language', '3'],
    ['2', 'JS Full form', 'Jone Search', 'Java Script', 'Java SCripting', 'Script Java', '2'],
    ['3', 'CSS full form', 'Cascading Sort Sheets', 'Cast Sort Sheet', 'Cascading Style Sort', 'Cascading Style Sheets', '4'],
    ['4', 'PHP full form', 'Personal Home Page', 'Personal Home Pages', 'Preper Home Page', 'Personal House Page', '1'],
    ['5', 'What is python framework? (True/False)', 'No', 'Yes', 'True', 'False', '2'],
    ['6', 'How to List first value access', 'list[1]', '[1]list', 'list[0]', '[0]list', '3'],
    ['7', 'How to tuple bracket use in python', '()', '{}', '[]', 'About Nothing', '1'],
    ['8', 'What is django?', 'Web framework', 'Language', 'App Develop', 'Cloud System', '1'],
    ['9', 'what is ASCII value this sign (A) ?', '65', '78', '42', '85', '1'],
    ['10', 'What is java script?', 'Scripting', 'Script Language', 'Web language', 'app language', '2'],
]

while True:
    currctans = 0
    for i, que, o1, o2, o3, o4, ans in questionlist:


        print("------------------------- Your Question "+ i + " -------------------------")
        print(que)

        print("------------------------- Your Options -------------------------")
        print("Options 1 : ", o1)
        print("Options 2 : ", o2)
        print("Options 3 : ", o3)
        print("Options 4 : ", o4)
        
        print("------------------------- Your Answer -------------------------")
        user = int(input("Choose the option : "))


        print("------------------------- Result -------------------------")
        if user == int(ans):
            print("Corrent")
            currctans += 1
        else:
            print("not corrent")
            print("Current Answer : ", ans)
        questionlength = len(questionlist)
        if int(i) == questionlength:
            break
        else:
            print("------------------------- Next Question -------------------------")
            nextque = input("Next question (Y/N) : ").lower()
            if nextque != "y":
                break
            print("\n")

    print("------------------------- All Currect  Answer -------------------------")
    print("\nYour currect answer : ", currctans)

    print("--------------------------------------------------")
    playagain = input("Play Again This Game (Y/N) : ")
    if playagain != "y":
        print("------------------------- Thansk For the play game -------------------------")
        break



print("----------------------------------------------------------------------------------------------------")