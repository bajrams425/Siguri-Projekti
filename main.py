
#   Ky file permban programin kryesot ose Chat App.
#   Ne kete faqe useri degon dhe pranon mesazhe ne group chat.
#   Funksionet kryesore te faqes jane te enkriptoj, dekriptoj, dergoj,
#   te marre dhe te shfaq vizualisht komunikimin me mesazhe ne chat room.
#   Programi perdor local adreses per t'u lidhur me server.


# Thirr librarite per krijimin dhe manipulimin e soketave.
from socket import *
# Thirr librarite per krijimin dhe manipulimin e threadeve.
from threading import *
# Thirr librarite e tkinter.
from tkinter import *
# Thirr fajllin front dhe merre variablen user_Username nga ai fajll.
from front import user_Username

# Krijo nje qeles te enkriptimit.
key = 7

# Funksioni per enkriptim permes algorimit Ceasar Cipher
# me vlere hyerese variablen mesazhi.
def enkripto(msg):
    # Krijo nje variabel te zbrazet mesazhi i enkriptuar.
    msg_enkriptuar=''
    # Fillo loop unazen ne cdo karakter ne varbaiblen hyerese.
    for karakteri in msg:
        # Perderisa karakteri eshte space...
        if karakteri==' ':
            # ... vetem shto karakterin ne variablen e re...
            msg_enkriptuar = msg_enkriptuar+karakteri
        # ... perndryshe...
        else:
            # ... enkripto mesazhin permes algoritmit te Cezarit dhe qelsit fillestar.
            msg_enkriptuar = msg_enkriptuar + chr((ord(karakteri) + key))
    # Ne fund te egzekutimit kthe varbialen e re.
    return msg_enkriptuar

# Funksioni per dekriptim permes algorimit Ceasar Cipher
# me vlere hyerese variablen mesazhi.
def dekripto(msg):
    # Krijo nje variabel te zbrazet mesazhi i dekriptuar.
    msg_dekriptuar=''
    # Fillo loop unazen ne cdo karakter ne varbaiblen hyerese.
    for karakteri in msg:
        # Perderisa karakteri eshte space...
        if karakteri==' ':
            # ... vetem shto karakterin ne variablen e re...
            msg_dekriptuar = msg_dekriptuar+karakteri
        # ... perndryshe...
        else:
            # ... dekripto mesazhin permes algoritmit te Cezarit dhe qelsit fillestar.
            msg_dekriptuar = msg_dekriptuar + chr((ord(karakteri) - key))
    # Ne fund te egzekutimit kthe varbialen e re.
    return msg_dekriptuar

# Funksioni i cili dergon mesazhin ne input te perdoruesit.
def dergoMsg():
    # Merr inputin e userit dhe ruaje ne variablen clientMessage.
    clientMessage = shkruajMsg.get()
    # Shfaqe mesazhin ne dritare se bashku me username.
    mesazhet.insert(END, "\n" + user_Username.get() + ": " + clientMessage)
    # Krijo nje variabel me username dhe mesazhin e userit
    # e cila do te enkriptohet.
    sendMsg_paEnkriptuar = user_Username.get() + ": " + shkruajMsg.get()
    # Enkripto mesazhin.
    sendMsg_Enkriptuar = enkripto(sendMsg_paEnkriptuar)
    # Dergo mesazhin e enkriptuar ne server me enkodim utf-8.
    msgSoketa.send(sendMsg_Enkriptuar.encode("utf-8"))

# Funksioni i cili merr mesazhet nga perdoruesit e tjere dhe i shfaqe ne dritare.
def merrMsg():
    # Perderisa lidhja qendron e hapur:
    while True:
        # Merr mesazhin nga soketa dhe dekodo permes utf-8.
        serverMessage = msgSoketa.recv(1024).decode("utf-8")
        # Dekripto mesazhin e marre nga soketa.
        mesazhi_dekriptuar = dekripto(serverMessage)
        # Shfaq mesazhin e marre ne console.
        print(mesazhi_dekriptuar)
        # Shfaq mesazhin e marre ne dritare.
        mesazhet.insert(END, "\n"+mesazhi_dekriptuar)

# Krijo variablen per pointimin e hostit.
hosti = "127.0.0.1"
# Krijo variablen e portit te hostit.
porti = 19191

# Krijo nje sokete
msgSoketa = socket(AF_INET, SOCK_STREAM)
# Vendos protokollin e soketave.
msgSoketa.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Krijo nje lidhje me server.
msgSoketa.connect((hosti, porti))

# Krijo nje dritare te re me tkinter dhe ruaje si variabla 'chatApp'.
chatApp = Tk()
# Cakto titullin/header-in e faqes.
chatApp.title("Serveri: "+ hosti+ ":"+str(porti))

# Krijo nje objekt i cili shfaq te dhena tekstuale
# ne shume rreshta ne dritare.
mesazhet = Text(chatApp, width=50)
# Cakto poziten e objektit ne dritare.
mesazhet.grid(row=0, column=0, padx=10, pady=10)

# Krijo nje text field per input te pordoruesit
# i cili eshte nje rreshtor.
shkruajMsg = Entry(chatApp, width=50)
# Vendos nje 'prompt' text (ose text hyres).
shkruajMsg.insert(0,"Shkruaj mesazhin ketu!")
# Vendos input field ne dritare.
shkruajMsg.grid(row=1, column=0, padx=10, pady=10)

# Krijo butonin dhe caktoj tekstin e brendshem dhe funksionin
# te cilin do ta egzekutoj kur te klikohet.
btnSendMessage = Button(chatApp, text="Send", width=20, command=dergoMsg)
# Cakto poziten e butonit ne dritare.
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

# Krijo nje thread per marrjen e mesazheve.
merrMsgThread = Thread(target=merrMsg)
# Aktivizo thread daemon, i cili nuk pengon programin
# e egzekutuar te ndalet
merrMsgThread.daemon = True
# Fillo threadin e krijuar
merrMsgThread.start()

# Shfaq dritaren dhe ndegjo per komandat e rradhes.
# Kjo e le dritaren ne loop perderisa useri ta mbaje te hapur
# ose te thirre nje dritare te re.
chatApp.mainloop()