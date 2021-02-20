import pyttsx3 

engine= pyttsx3.init() #se crea un motor 
engine.setProperty("rate",150)#set la velocidad en la que se reproduce el audio"""
numero = input("digite un numero 3")
lenguage ='es'
engine.say(numero)#se dice el texto que se le pasa  
engine.runAndWait() #para que pare cuando termine """