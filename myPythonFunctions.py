import random
import os
def getUserPoint(utilisateur):
    try:
        with open("userScores.txt","r") as fichier:
            for ligne in fichier:
                name,score=ligne.strip().split(", ")
                if name==utilisateur:
                    return int(score)
    except FileNotFoundError:
        pass
    return -1
def updateUserPoints(newUser,userName,score):
    if newUser:
        with open("userScores.txt","a") as fichier:
            fichier.write(userName+", "+str(score)+"\n")
    else:
        with open("userScores.txt","r") as fichier:
            lignes=fichier.readlines()
        with open("userScores.tmp","w") as fichier_temp:
            for ligne in lignes:
                nom,score2=ligne.strip().split(", ")
                if nom==userName:
                    fichier_temp.write(userName+", "+str(score)+"\n")
                else:
                    fichier_temp.write(ligne)
        os.remove("userScores.txt")
        os.rename("userScores.tmp","userScores.txt")
def generateQuestion():
    operandList=[random.randint(1,10) for _ in range(5)]
    operatorList=[]
    operatorDict={1:"+",2:"-",3:"*",4:"**"}
    for _ in range(4):
        while True:
            operateur=operatorDict[random.randint(1,4)]
            if operatorList and operatorList[-1]=="**" and operateur=="**":
                continue
            operatorList.append(operateur)
            break
    questionString=str(operandList[0])
    for i in range(4):
        questionString+=" "+str(operatorList[i])+" "+str(operandList[i+1])
    questionString=questionString.replace("**","^")
    result=eval(questionString)
    print("Calculer : "+questionString)
    return result