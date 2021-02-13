                                      
                                     Prezantimi
                                     
                                     
Python është një gjuhë e shkëlqyeshme programimi për rrjetat kompjuterike. Na lejon të krijojmë aplikacione solide shumë shpejt dhe lehtë. Ne do të kemi një server që pret bisedën dhe shumë klientë që lidhen me të dhe komunikojnë me njëri-tjetrin. 


Arkitektura Klient-Server

Për aplikimin tonë, ne do të përdorim arkitekturën klient-server. Kjo do të thotë që ne do të kemi shumë klientë (përdoruesit) dhe një server qendror që pret gjithçka dhe siguron të dhënat për këta klientë.
Prandaj, do të duhet të shkruajmë tri skripta Python. Një do të jetë për fillimin e serverit ,një do të jetë për klientin dhe nje do te jete per chat-in. Ne do të duhet të ekzekutojmë serverin së pari, në mënyrë që të ketë një bisedë, me të cilën klientët mund të lidhen. Vetë klientët nuk do të komunikojnë drejtpërdrejt me njëri-tjetrin por përmes serverit qendror.


Zbatimi i serverit

Ky file permban serverin i cili ndegjon per mesazhe dhe forwardon ato.Ne këtë faqe useri nuk ka akses dhe dërgon mesazhe të enkriptuara.Funksion kryesor është të ndëgjoj soketa, të krijoj lidhje dhe të shfaq vizualisht komunikim ne chat room. Serveri perdor local adreses.

Zbatimi i Chat

Një server është shumë i padobishëm pa klientë që lidhen me të. Deri tani ne do të implementojmë klientin tonë. 
Ky file permban programin kryesot ose Chat App. Në këtë faqe useri dërgon dhe pranon mesazhe ne group chat. Funksionet kryesore te faqes jane të enkriptoj, dekriptoj, dërgoj,të marre dhe te shfaq vizualisht komunikimin me mesazhe në chat room.  Programi përdor local adreses per t'u lidhur me server.

Zbatimi i Klientit
Ky file përmban pamjen e parë që i paraqitet userit.Në këtë faqe useri shtyp username-in që do shfaqet Username nuk duhet të permbaj 'whitespaces' si dhe mund të rizgjedhet disa her. Pas zgjedhjes, useri shtyp butonin e fshehur paraprakisht.
                                 
                                 Hapat e ekzekutimit


Për të ekzekutuar aplikacioni fillimisht ne duhet të ekzekutojm server side pastaj main side.  Për të ekzektuar server side ne perdorim Pycharm e cila është vegël edituese, kur të ekzekutojm pycharm shfaqet console .Me Console mundemi me e pa cka po ndodhe në prapasken me serverin , kush po bëhet login , kush po dërgon mesazhe te enkriptuara, kush po bëhet logout . Për të ekzekutuar  aplikacionin kryesor  përdorim command prompt(cmd) .Me cmd mund  të shkojm te file ta thirrim me python emrin e file në rastin ton e kemi main.py  kur ekzekutohet aplikacioni shfaqet faqja front së pari  ekzekutohet prej importit  file front . Front-i e ka për detyrë  që ta mar  user input që ka me mar si username ku user input ka me dërgu te faqja main që të mbyllet fronti . Pasi që të  hapet dritarja e main  perdorusi ka me dërgu mesazha të enkriptuara përmes kodit te Cezarit përmes celesit static që e ka përbrenda edhe dërgohen të enkriptuara në server  edhe i dërgon te socet tjera.Atëher ato merren dhe dekriptohen në textfield që paraqitet mesazhi .Ne vazhdim jane shfaqur te gjithe hapat e lartecekur gjate te ekzekutimit te kodit.



![1](https://user-images.githubusercontent.com/58037389/107862583-e6e16380-6e4d-11eb-897b-52680fd64efa.png)
pycharm vs console
![2](https://user-images.githubusercontent.com/58037389/107862652-64a56f00-6e4e-11eb-9e25-a547ecadc045.png)

