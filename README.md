                                      
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


Për të ekzekutuar aplikacioni fillimisht ne duhet të ekzekutojm server side pastaj main side. Për të ekzektuar server side preferojme Pycharm e cila është vegël edituese, e cila kur të ekzekutojm python file shfaqet console dhe te njejten kohe mund te shohim source kodin. Me Console mundemi me pa vizualisht cka po ndodhe në prapaskene me serverin, kush bëhet login, kush po dërgon mesazhe te enkriptuara, kush po bëhet logout. Për të ekzekutuar aplikacionin kryesor përdorim command prompt (cmd). Me cmd mund shkojm te file ku eshte ruajtur kodi i klientit dhe thirrim me python + emrin e file komanden. Në rastin tone e kemi main.py dhe kur ekzekutohet aplikacioni shfaqet preface dritarja front.py pasiqe main.py e ben import dhe kerkon nga ajo nje variabel e cila eshte username i perdoruesit. Front-i e ka për detyrë  që ta marre user input dhe ta pasoj si username variabel te faqja main dhe pastaj mbyllet. Pasi që të hapet dritarja e main perdoruesi ka mundesi te dërgoj mesazha ne group chat të enkriptuara përmes kodit te Cezarit dhe celesit static që e ka përbrenda. Keto mesazha dërgohen të enkriptuara në server i cili i 'forward'-on te soketat tjera. Pastaj ato merren, dekriptohen dhe shfaqen në textfield që shtyp mesazhat ne chat room. Ne vazhdim jane shfaqur te gjithe hapat e lartecekur gjate  ekzekutimit te kodit.




![1](https://user-images.githubusercontent.com/58037389/107862583-e6e16380-6e4d-11eb-897b-52680fd64efa.png)


pycharm vs console


![2](https://user-images.githubusercontent.com/58037389/107862652-64a56f00-6e4e-11eb-9e25-a547ecadc045.png)

running main.py me cmd. 
Pse me cmd? 
Se permes cmd mujna me bo run paralelisht 2+ clienta.


![3](https://user-images.githubusercontent.com/58037389/107862654-67a05f80-6e4e-11eb-8e4d-8dd28d19dfc5.png)



na shfaqet preface front.py dy here per dy cmd    



![4](https://user-images.githubusercontent.com/58037389/107862657-6e2ed700-6e4e-11eb-92ff-26d41bcd60e7.png)


Pasi ta  shkruajm  username shfaqet butoni ne fund te faqes vazhdo
Kujdes: nese username permban veq ëhitespace karaktere nuk na lejohet qe te vazhdojm me tutje


![5](https://user-images.githubusercontent.com/58037389/107862659-6ff89a80-6e4e-11eb-8dec-a7723041ac15.png)



Pasi ta shkruajm sakte username edhe klikojme vazhdo dritarja e preface front mbyllet dhe vazhdon te egzekutohet main file edhe shfaqet dritarja e main



![6](https://user-images.githubusercontent.com/58037389/107862662-71c25e00-6e4e-11eb-9515-ef95ef3645de.png)



Ne console na paraqitet njoftimi qe u kyq nje user.



![7](https://user-images.githubusercontent.com/58037389/107862665-7555e500-6e4e-11eb-8b8c-3b194335ea41.png)



Tani mund te filloj komunikimi. Kur nje user shenon mesazh dhe klikon butonin dergo mesazhi shfaqet ne dritare i dekriptuar




![8](https://user-images.githubusercontent.com/58037389/107862666-771fa880-6e4e-11eb-8a2b-feee5cb4c164.png)



Ne server ne console shohim vetem mesazhin e enkriptuar




![9](https://user-images.githubusercontent.com/58037389/107862669-79820280-6e4e-11eb-9274-df741516d775.png)




ne rastin kur nje user del nga chati apo terminon lidhjen dhe mbyll aplikacionin




![10](https://user-images.githubusercontent.com/58037389/107862670-7b4bc600-6e4e-11eb-866a-96114696ea47.png)




Ne rast se serveri ndalet na shfaqet mesazhi ne console:
Nga ana e serverit




![11](https://user-images.githubusercontent.com/58037389/107862673-7e46b680-6e4e-11eb-833c-c8039083968b.png)




Nga ana e klientit




![12](https://user-images.githubusercontent.com/58037389/107862674-8141a700-6e4e-11eb-9508-ca5c419eebdb.png)



