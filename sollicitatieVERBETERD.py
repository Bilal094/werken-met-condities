print('++++++++++++++++++++++++++++++++++++++++++++++++++++')                                                          
print('+    Sollicitatieformulier "Circusdirecteur"       +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Welkom bij de vacature voor Circusdirecteur te      ') 
print('Circus HotelDeBotel! Voordat u in aanmerking kan    ')
print('komen voor een sollicitatgesprek, dienen wij u als  ')
print('eerst een paar vragen te stellen. Gelieve deze      ')
print('eerlijk te beantwoorden. Succes!                    ')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
# Standaard vragen
name = input('Wat is uw naam? ')
jongleren = int(input('Voor hoeveel jaar heeft u ervaring met jongleren? '))
dierendressuur = int(input('Voor hoeveel jaar heeft u ervaring met dieren-dressuur? '))
acrobatiek = int(input('Voor hoeveel jaar heeft u ervaring met acrobatiek? '))
diploma = input('Heeft u een MBO 4 diploma in Ondernemen? ')
rijbewijs = input('Heeft u een rijbewijs? ')
hoed = input('Heeft u een hoge hoed? ')
massa = int(input('Wat is uw massa? '))
lengte = int(input('Wat is uw lengte in cm? '))
certificaat = input('Heeft u een certificaat \'Overleven met gevaarlijk personeel\'? ')
geslacht = input('Bent u een man of een vrouw? ')
# Geslachtsgerelateerde vragen hieronder, man
if geslacht == 'man':
    snor = input('Heeft u een snor? ')
    if snor == 'ja':
        snorlengte = int(input('Hoelang is uw snor in cm? '))
# Vrouw
if geslacht == 'vrouw':
        haar = input('Heeft u rood krullend haar? ')
        if haar == 'ja':
            haarlengte = int(input('Wat is uw haarlengte? '))
# Hieronder wordt de uitslag berekend
if (jongleren >= 5 or dierendressuur >= 4 or acrobatiek >= 3) and diploma == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and massa >= 90 and lengte >= 150 and certificaat == 'ja' and (geslacht == 'man' and snor == 'ja' and snorlengte >= 10 or geslacht == 'vrouw' and haar == 'ja' and haarlengte >= 10):
    print('U bent aangenomen!')
    input('')
else:
    print('U voldoet niet aan de eisen dus u bent niet aangenomen!')
    input('')