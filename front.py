
#   Ky file permban pamjen e pare qe i paraqeitet userit.
#   Ne kete faqe useri shtyp username-in qe do shfaqet
#   Username nuk duhet te permbaj 'whitespaces'
#   si dhe mund te rizgjedhet disa her.
#   Pas zgjedhjes, useri shtyp butonin e fshehur paraprakisht
#   'Vazhdo' per te kaluar ne Chat-App.


# Thirr librarite e tkinter.
from tkinter import *

# Funksioni i cili do shikoj nese useri ka shtypyr nje username te pranueshem.
# Ne rastin se ka shtypur nje username te sakte, shfaq butonin vazhdo.
# Nese rishtyp username dhe nuk eshte i sakte, largohet labela 2 dhe butoni vazhdo.
def merrUsername():
    # Shiko nese inputi ka karaktere dhe nuk ka vetem whitespaces.
    # Funksioni .get() kthen vlere string, e cila eshte true ne krahasim
    # vetem kur permban karaktere.
    if username.get() and not username.get().isspace():
        # Nderro textin e labeles dhe shfaq username e deshiruar.
        labela1["text"] = "Urime keni marre username: " + username.get()
        # Nderro lebel e rradhes dhe shfaq butinon vazhdo duke e vendosur ne grid layout.
        # Perdoret vetem per udhezim.
        labela2["text"] = "Klikoni butonin 'Vazhdo' per te vazhduar ne faqen tjeter..."
        btnVazhdo.grid(row=3, column=0, padx=10, pady=10)
        # Merr vleren e inputit dhe ruaje si string (nevojitet per te shfaqur username te
        # perdoruesve ne chat).
        user_Username.set(username.get())
    # Ne rast te rishtypjes se inputit gabim.
    else:
        # Nderro labelen 1 per te udhezuar.
        labela1["text"] = "Username nuk duhet te jete i zbrazet"
        # Largo labelen 2 te udhezimit per vazhdon.
        labela2["text"] = ""
        # Fsheh butonin per te vazhduar.
        btnVazhdo.grid_forget()
        # Largo username e shtypyr nga variabla string.
        user_Username.set('')

# Funksioni per te vazhduar ne faqen e chat-it.
def hapeFaqen():
    # Mbyll faqen momentale per input te username-it.
    faqja.destroy()

# Krijo nje dritare te re me tkinter dhe ruaje si variabla 'faqja'.
faqja= Tk()
# Cakto titullin/header-in e faqes.
faqja.title("Cakto Username")
# Krijo labelen 1 por te zbrazet.
labela1 = Label(faqja, text='')
# Krijo labelen 2 por te zbrazet.
labela2 = Label(faqja, text='')
# Cakto pozitat relative te labelave.
labela1.place(x=100,y=25)
labela2.place(x=100,y=45)
# Krijo input field, nje rreshtor.
username = Entry(faqja, width=50)
# Vendos nje 'prompt' text (ose text hyres).
username.insert(0, "Username te cilin deshironi ta perdorni?")
# Vendos input field ne dritare.
username.grid(row=1, column=0, padx=100, pady=75)

# Krijo nje string variabel e cila do te merr inputin e userit.
# si username (per ta pasuar ne chat app).
user_Username = StringVar()

# Krijo butonin, vendose ne faqe dhe jepi funksionin pas shtypjes.
btnUsername = Button(faqja, text="Cakto", width=20, command=merrUsername)
# Cakto poziten e butonit ne faqe.
btnUsername.grid(row=2, column=0, padx=10, pady=10)

# Krijo butonin, vendose ne faqe dhe jepi funksionin pas shtypjes.
btnVazhdo = Button(faqja, text="Vazhdo", width=20, command=hapeFaqen)
# Cakto poziten e butonit ne faqe.
btnVazhdo.grid(row=3, column=0, padx=10, pady=10)
# Fshehe butonin.
btnVazhdo.grid_forget()

# Shfaq dritaren dhe ndegjo per komandat e rradhes.
# Kjo e le dritaren ne loop perderisa useri ta mbaje te hapur
# ose te thirre nje dritare te re.
faqja.mainloop()
