import tweepy
from colorama import Fore, init

init()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(Fore.LIGHTCYAN_EX + """___________         .__   __     __                   __________          __   
\__    ___/__  _  __|__|_/  |_ _/  |_   ____ _______  \______   \  ____ _/  |_ 
  |    |   \ \/ \/ /|  |\   __\\   __\_/ __ \\_  __ \  |    |  _/ /  _ \  __/
  |    |    \     / |  | |  |   |  |  \  ___/ |  | \/  |    |   \(  <_> )|  |  
  |____|     \/\_/  |__| |__|   |__|   \___  >|__|     |______  / \____/ |__|  
                                           \/                 \/               """)

choice = int(input("""Entrez le chiffre corresepondant:

1. Envoyer un tweet
2. Supprimer un tweet
3. Retweet
4. Unreweet
5. Follow
6. Unfollow
7. Bloquer
8. Débloquer
9. Masquer
10. Démasquer

[>] """))

if choice == 1:    
    try:   
        message = input("Veuillez entrer le message a envoyer: ")
        api.update_status(message)
        print(Fore.GREEN + "Tweet réussi")
    except:
        print("Erreur dans la requête a Twitter.")
if choice == 2:
    try:
        id = int(input("Entrez l'id du Tweet: "))
        api.destroy_status(id)
        print(Fore.GREEN + "Suppresion réussi")
    except:
        print("Erreur dans la requête a Twitter.") 
if choice == 3:
    try:
        id = int((input("Entrez l'id du Tweet: ")))
        api.retweet(id)
        print(Fore.GREEN + "Retweet réussi")    
    except:
        print("Erreur dans la requête a Twitter.") 
if choice == 4:
    try:
        id = int((input("Entrez l'id du Tweet: ")))
        api.unretweet(id)
        print(Fore.GREEN + "Unretweet réussi")    
    except:
        print("Erreur dans la requête a Twitter.")     
if choice == 5:
    try:
        name = input("Entrez le nom de la personne a follow: ") 
        api.create_friendship(name)  
        print(Fore.GREEN + "Le follow a bien été effectué.")    
    except:
        print("Erreur dans la requête a Twitter.")  
if choice == 6:
    try:
        name = input("Entrez le nom de la personne a unfollow: ")
        api.destroy_friendship(name)
        print(Fore.GREEN + "Le unfollow a bien été effectué.") 
    except:
        print("Erreur dans la requête a Twitter.")     
if choice == 7:
    try:
        name = input("Entrez le nom de la personne a bloquer: ")
        api.create_block(name)
        print(Fore.GREEN + "Bloquage réussi")
    except:
        print("Erreur dans la requête a Twitter.")
if choice == 8:
    try:
        name = input("Entrez le nom de la personne a débloquer: ")
        api.destroy_block(name)
        print(Fore.GREEN + "Débloquage réussi")
    except:
        print("Erreur dans la requête a Twitter.")
if choice == 9:
    try:
        name = input("Entrez le nom de la personne a masquer: ")
        api.create_mute(name)
        print(Fore.GREEN + "Masquage réussi")
    except:
        print("Erreur dans la requête a Twitter.")
if choice == 10:
    try:
        name = input("Entrez le nom de la personne a démasquer: ")
        api.destroy_mute(name)
        print(Fore.GREEN + "Démasquage réussi")
    except:
        print("Erreur dans la requête a Twitter.")
