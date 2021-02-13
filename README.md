                                      
                                     Prezantimi
                                     
                                     
Python është një gjuhë e shkëlqyeshme programimi për rrjetat kompjuterike. Na lejon të krijojmë aplikacione solide shumë shpejt dhe lehtë. Ne do të kemi një server që pret bisedën dhe shumë klientë që lidhen me të dhe komunikojnë me njëri-tjetrin. 


Arkitektura Klient-Server

Për aplikimin tonë, ne do të përdorim arkitekturën klient-server. Kjo do të thotë që ne do të kemi shumë klientë (përdoruesit) dhe një server qendror që pret gjithçka dhe siguron të dhënat për këta klientë.
Ne rastin tonë kemi tri skripta Python. Një do të jetë per fillimin e serverit, një do të jetë preface për klientin dhe një do të jetë për chat-in. Ne do të duhet të ekzekutojmë serverin së pari, që klientët mund të lidhen me chat-room dhe të komunikojnë. Vetë klientët nuk do të komunikojnë drejtpërdrejt me njëri-tjetrin por përmes serverit qëndror i cili forwardon mesazhet nga një soket në tjetrën.


File i serverit

File side.py përmban kodin për serverin i cili do të ndëgjojë për soketa dhe forwardon mesazhet nëpër to. Në këtë pjesë useri nuk ka akses dhe dërgon mesazhe të enkriptuara. Funksion kryesor është pra të ndëgjoj në port për soketa, të krijoj lidhje dhe të shfaq vizualisht komunikim në chat room. Serveri përdor local adresses.

File i Chat

Një server është shumë i padobishëm pa klientë që lidhen me të. Përmes main.py ne do të implementojmë klientin tonë.
Ky file përmban programin kryesor ose Chat App. Në dritaren e këtij file useri dërgon dhe pranon mesazhe në group chat. Funksionet kryesore të tij janë të enkriptoj, dekriptoj, dërgoj, të marrë dhe të shfaqë vizualisht komunikimin me mesazhe në chat room. Programi përdor local adreses dhe porten e dhenë për t'u lidhur me server.

File i Klientit

File front.py përmban pamjen e parë që i paraqitet userit. Në dritaren e këtij file useri shtyp username-in që do shfaqet në chat app. Username nuk duhet të përmbaj 'whitespaces' si dhe mund të rizgjedhet disa herë. Pas zgjedhjes, useri shtyp butonin e fshehur paraprakisht 'Vazhdo' për të vazhduar në dritaren kryesore.
                                 
                                 Hapat e ekzekutimit


Për të ekzekutuar aplikacioni fillimisht ne duhet të ekzekutojm server side pastaj main side. Për të ekzektuar server side preferojme Pycharm e cila është vegël edituese, e cila kur të ekzekutojm python file shfaqet console dhe të njejtën kohë mund të shohim source kodin. Me Console mundemi me pa vizualisht çka po ndodhë në prapaskenë me serverin, kush bëhet login, kush po dërgon mesazhe të enkriptuara, kush po bëhet logout. Për të ekzekutuar aplikacionin kryesor përdorim command prompt (cmd). Me cmd mundë shkojmë te file ku është ruajtur kodi i klientit dhe thirrim me python + emrin e file komandën. Në rastin tonë e kemi main.py dhe kur ekzekutohet aplikacioni shfaqet preface dritarja front.py pasiqë main.py e bënë import dhe kërkon nga ajo një variabël e cila është username i perdoruesit. Front-i e ka për detyrë  që ta marrë user input dhe ta pasoj si username variabel te faqja main dhe pastaj mbyllet. Pasi që të hapet dritarja e main përdoruesi ka mundesi të dërgoj mesazha në group chat të enkriptuara përmes kodit te Cezarit dhe celesit static që e ka përbrenda. Keto mesazha dërgohen të enkriptuara në server i cili i 'forward'-on te soketat tjera. Pastaj ato merren, dekriptohen dhe shfaqen në textfield që shtyp mesazhat në chat room. Në vazhdim janë shfaqur të gjithë hapat e lartëcekur gjatë  ekzekutimit të kodit.




![1](https://user-images.githubusercontent.com/58037389/107862583-e6e16380-6e4d-11eb-897b-52680fd64efa.png)


pycharm vs console


![2](https://user-images.githubusercontent.com/58037389/107862652-64a56f00-6e4e-11eb-9e25-a547ecadc045.png)

running main.py me cmd. 
Pse cmd? 
Sepse përmes cmd mundemi të bëjmë run paralelisht 2+ klienta.


![3](https://user-images.githubusercontent.com/58037389/107862654-67a05f80-6e4e-11eb-8e4d-8dd28d19dfc5.png)



pas egzekutimit të komandës na shfaqet preface (për çdo klient, në rastin tonë 2)  



![4](https://user-images.githubusercontent.com/58037389/107862657-6e2ed700-6e4e-11eb-92ff-26d41bcd60e7.png)


Pasi ta  shkruajm  username shfaqet butoni në fundë të faqes 'Vazhdo'.
Kujdes: nëse username përmbanë vetëm whitespace karaktere, nuk na lejohet që të vazhdojmë më tutje


![5](https://user-images.githubusercontent.com/58037389/107862659-6ff89a80-6e4e-11eb-8dec-a7723041ac15.png)



Pasi të shkruajmë saktë username edhe klikojmë butonin vazhdo, dritarja e preface Front mbyllet dhe vazhdon të egzekutohet Main file dhe shfaqet dritarja e Main



![6](https://user-images.githubusercontent.com/58037389/107862662-71c25e00-6e4e-11eb-9515-ef95ef3645de.png)



Në console na paraqitet njoftimi pasi të kyqet një user.



![7](https://user-images.githubusercontent.com/58037389/107862665-7555e500-6e4e-11eb-8b8c-3b194335ea41.png)



Nga tani mund të filloj komunikimi. Kur një user shenon mesazh dhe klikon butonin dergo mesazhin shfaqet në dritare i dekriptuar




![8](https://user-images.githubusercontent.com/58037389/107862666-771fa880-6e4e-11eb-8a2b-feee5cb4c164.png)



Kurse në server, në console, shohim vetëm mesazhin e enkriptuar, i cili do të behet forward në soketat tjera



![9](https://user-images.githubusercontent.com/58037389/107862669-79820280-6e4e-11eb-9274-df741516d775.png)




Në rastin kur një user del nga chati apo terminon lidhjen dhe mbyll aplikacionin në server shfaqet njoftimi:




![10](https://user-images.githubusercontent.com/58037389/107862670-7b4bc600-6e4e-11eb-866a-96114696ea47.png)




Në rast se serveri ndalet na shfaqet mesazhi në console...
Nga ana e serverit:




![11](https://user-images.githubusercontent.com/58037389/107862673-7e46b680-6e4e-11eb-833c-c8039083968b.png)




Nga ana e klientit:




![12](https://user-images.githubusercontent.com/58037389/107862674-8141a700-6e4e-11eb-9508-ca5c419eebdb.png)



