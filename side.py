
#   Ky file permban serverin i cili ndegjon per mesazhe dhe forwardon ato.
#   Ne kete faqe useri nuk ka akses dhe dergon mesazhe te enkriptuara.
#   Funksion kryesor eshte te ndegjoj soketa, te krijoj lidhje
#   dhe te shfaq vizualisht komunikim ne chat room.
#   Serveri perdor local adreses.


# Thirr librarite per krijimin dhe manipulimin e soketave.
from socket import *
# Thirr librarite per krijimin dhe manipulimin e threadeve.
from threading import *

# Krijo nje array ku do te ruhet te dhenat e klienteve.
klientSRV = set()

# Krijo funksionin e cila perdor soketen dhe adresen per te shfaqur
# mesazhet ne server (te cilat vijne te enkriptuara), dhe perderisa
# te jete lidhja e ngritur, forwardon mesazhet ne chat app te secilit
# end client dhe shfaq nje mesazh ne server kur shkyqet nje user nga
# lidhja me server (apo mbyll dritaren).
def klientThreadi(klientSocket, adresaKlientit):
    # Perderisa te jete e ngritur lidhja...
    while True:
        # ... dhe dritarja te jete e hapur...
        try:
            # ... merr mesazhet nga perdoruasi neper soketa...
            msg = klientSocket.recv(1024).decode("utf-8")
            # ... shfaqi ne server...
            print(msg)
            # ... dhe per secilin mesazh te lexuar...
            for klienti in klientSRV:
                # ... i cili nuk eshte ne sokete te perdoruesit...
                if klienti is not klientSocket:
                    # ... forwardo mesazhin tek perdoruesi.
                    klienti.send((msg).encode("utf-8"))
        # Kur te mbyllet dritarja nga perdoruesi...
        except ConnectionResetError:
            # ... mbyll lidhjen e perdoruesit...
            klientSRV.remove(klientSocket)
            # ... shfaq ne server kush eshte larguar nga lidhja...
            print(adresaKlientit[0] + ":" + str(adresaKlientit[1]) +" u shkyq nga lidhja!")
            # ... dhe mbyll unazen per kontrollimin e gjendjes se lidhjes.
            break
    # Mbyll soketen kur te mbyllet lidhja.
    klientSocket.close()

# Krijo nje sokete.
hosti = socket(AF_INET, SOCK_STREAM)
# Vendos protokollin e soketave.
hosti.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

# Cakto host IP te serverit per komunikim.
hostIp = "127.0.0.1"
# Cakto portin e serverit.
porti = 19191
# Lidh/Bind IP adresen dhe portin e hostit.
hosti.bind((hostIp, porti))
# Fillo ndegjimin per kerkesa per lidhje ne host.
hosti.listen()
# Pas fillimit te ndegjimit, shfaq ne console
# se ka filluar ndegjimi.
print ("Duke pritur lidhje nga perdoruesit...")

# Perderisa programi ndegjon...
while True:
    # ... prit lidhjen e rradhes...
    klientSocket, clientAddress = hosti.accept()
    # ... shto soketen ne array...
    klientSRV.add(klientSocket)
    # ... shfaqe ne console lidhjen e krijuar...
    print ("Lidhja u ngrit me adresen: ", clientAddress[0] + ":" + str(clientAddress[1]))
    # ... krijo nje thread me soketen e re...
    thread = Thread(target=klientThreadi, args=(klientSocket, clientAddress, ))
    # ... dhe fillo threadin per soketen e re.
    thread.start()
