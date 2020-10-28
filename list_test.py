#när vi hämtar datan så får vi typ ut nått som detta.
massa_data = {'frågor':[{'key_för_att_komma_åt_fråga':'själva frågan'},
                        {'key_för_att_komma_åt_rätt':'rätt svar'},
                        {'key-för fel_svar':['fel svar 1','fel svar 2']}]}

#så för att gå in i 'frågor' gör vi följande:

frågor = massa_data['frågor']

#nu har vi en variabel som har alla våra frågor, i detta fal 1, men det fungera på¨samma sätt om det hade varit fler.
#kör man en "print(type(frågor)) , så ser vi att det är en lista.
#medans vi inte kan gå in på speciella keys så är det ju lätt att använda listor i en for loop,
# då den börjar med första( [0], och kör tills det tar slut.

for fråga in frågor:
    print(fråga)
#här kollar den varje element(fråga) i frågor.
# om vi vill kan vi här gå in i varje dict som ligger i listan, genom att använda dom key vi har.
#i detta fall, vill vi skriva ut 'själva frågan'.
#då då får vi skriva något i stil med:
for fråga in frågor:
    print(fråga['key_för_att_komma_åt_fråga'])
#vill vi komma åt någon anna key, byter vi bara ut den. ex:
for fråga in frågor:
    print(fråga['key_för_att_komma_åt_rätt'])
    print(fråga['key_för_fel_svar'])
#när det kommer till fel svar så ligger dom i en lista,
# men eftersom det bara är två element kan vi använda slicing här.
# första elemente har [0], andra [1].
