import aminofix
from os import path
import json
from time import sleep
from pyfiglet import figlet_format
from colored import fore, style

print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
    Chat reputation v2
Script by Lucas Day
Github : https://github.com/LucasAlgerDay"""
)
print(figlet_format("Chat reputation version private", font="fourtops"))



THIS_FOLDER=path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,'accounts.json')
dictlist=[]
client = aminofix.Client()
email = input("Email of the account of host:  ")
password =input("Password:  ")
client.login(email, password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]

cooldown = int(input("Cooldown por cuenta: "))
with open(emailfile)as f:dictlist=json.load(f)


print(f"{len(dictlist)} cuentas cargadas")

for acc in dictlist:
    email = acc['email']
    password =  acc['password']
    device = acc['device']
    cliente = aminofix.Client(deviceId = device)
    try:
        cliente.login(email=email, password=password)
        cliente.join_community(communityid)
        sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
        sub_client.join_chat(chatx)
        cliente.join_video_chat_as_viewer(comId=communityid, chatId=chatx)
        print(f"{email} Ingresado en el chat, esperando {cooldown} para la siguiente cuenta")
        sleep(cooldown)
    except Exception as e:
        print(f"Error en la siguiente cuenta {email}: {e} \n\n\n Esperando {cooldown} para la siguiente cuenta.")
        sleep(cooldown)
        pass
