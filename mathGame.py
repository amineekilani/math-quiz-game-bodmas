import myPythonFunctions
try:
    userName=input("Votre nom : ")
    userScore=myPythonFunctions.getUserPoint(userName)
    newUser=userScore==-1
    if newUser:
        userScore=0
    userChoice=0
    while userChoice!="-1":
        result=myPythonFunctions.generateQuestion()
        while True:
            try:
                reponse=int(input("Votre réponse : "))
                if reponse==result:
                    print("Vrai!")
                    userScore+=1
                else:
                    print("Faux! La réponse est",result)
                break
            except ValueError:
                print("Ce n'est pas valide!")
        userChoice=input("Cliquez Enter pour une nouvelle question ou type '-1' pour quitter : ")
    myPythonFunctions.updateUserPoints(newUser,userName,userScore)
    print("Votre score final :",userScore)
except Exception as e:
    print("Erreur :",e)