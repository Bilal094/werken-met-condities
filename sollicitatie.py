print('++++++++++++++++++++++++++++++++++++++++++++++++++++')                                                          
print('+    Sollicitatieformulier "Circusdirecteur"       +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Welkom bij de vacature voor Circusdirecteur te      ') 
print('Circus HotelDeBotel! Voordat u in aanmerking kan    ')
print('komen voor een sollicitatgesprek, dienen wij u als  ')
print('eerst een paar vragen te stellen. Gelieve deze      ')
print('eerlijk te beantwoorden. Succes!                    ')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
name = input('Wat is uw naam? ')
Ervaring = input('Heeft u ervaring met het volgende: dierendressuur of jongleren of acrobatiek? ')
if Ervaring == 'dierendressuur' or Ervaring == 'jongleren' or Ervaring == 'acrobatiek':
    JaarErvaring = int(input('Hoeveel jaar ervaring heeft u met de gekozen baan? Type alleen het getal. '))
    if JaarErvaring >= 4 or JaarErvaring >= 5 or JaarErvaring >= 3:
        Diploma = input('Heeft u een MBO 4 diploma in Ondernemen? J/N ')
        if Diploma == 'j' or Diploma == 'J':
            Rijbewijs = input('Heeft u een geldig vrachtwagenrijbewijs in bezit? J/N ')
            if Rijbewijs == 'j'or Rijbewijs == 'J':
                Hoed = input('Heeft u een hoge hoed? J/N ')
                if Hoed == 'j' or Hoed == 'J':
                    Geslacht = input('Bent u een man of een vrouw? ')
                    if Geslacht == 'man':
                        Snor = input('Heeft u een snor breder van 10 cm? J/N ')
                        if Snor == 'j' or Snor == 'J':
                            Massa = input('Is uw massa zwaarder dan 90 kg? J/N ')
                            if Massa == 'j' or Massa == 'J':
                                Certificaat = input('Heeft u een certificaat \'Overleven met gevaarlijk personeel\'? J/N ')
                                if Certificaat == 'j' or Certificaat == 'J':
                                    print('en dan nu de laatste vragen...')
                                    Hobby = input('Bent u als een clown en vindt u het leuk om mensen aan het lachen te krijgen? J/N ')
                                    if Hobby == 'j' or Hobby == 'J':
                                        Dier = input('Bent u comfortabel met (circus) dieren? J/N ')
                                        if Dier == 'j' or Dier == 'J':
                                            Act = input('Bent u goed in acteren? J/N ')
                                            if Act == 'j' or Act == 'J':
                                                print('Gefeliciteerd, '+ str(name) +'! U bent een geschikte kandidaat en u komt in aanmerking voor een persoonlijk gesprek.')
                                            elif Act == 'n' or Act == 'N':
                                                print('Sorry ' + str(name) + ', u kunt niet acteren dus u komt niet in aanmerking voor een persoonlijke gesprek.')
                                            else:
                                                print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                        elif Dier == 'n' or Dier == 'N':
                                            print('Sorry ' + str(name) + ', u bent niet comfortabel met dieren dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                        else:
                                            print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                    elif Hobby == 'n' or Hobby == 'N':
                                        print('Sorry ' + str(name) + ', u heeft niet de juiste hobbies voor de functie, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                    else:
                                        print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                elif Certificaat == 'n' or Certificaat == 'N':
                                    print('Sorry ' + str(name) + ', u heeft geen certificaat \'Overleven met gevaarlijk personeel\' in bezit, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                else:
                                    print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                            elif Massa == 'n' or Massa == 'N':
                                print('Sorry ' + str(name) + ', uw massa is kleiner dan 90 kg, dus u komt niet in aanmerking voor een sollicitatiegesprek.')
                            else:
                                print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                        elif Snor == 'n' or Snor == 'N':
                            print('U heeft geen snor of een snor die breder is dan 10 cm, dus u komt niet in aanmerking voor een sollicitatiegesprek.')
                        else:
                            print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                    elif Geslacht == 'vrouw':
                        Haar = input('Draagt u rood krulhaar langer dan 10 cm? J/N ')
                        if Haar == 'j' or Haar == 'J':
                            Massa2 = input('Is uw massa zwaarder dan 90 kg? J/N ')
                            if Massa2 == 'j' or Massa2 == 'J':
                                Certificaat2 = input('Heeft u een certificaat \'Overleven met gevaarlijk personeel\'? J/N ')
                                if Certificaat2 == 'j' or Certificaat2 == 'J':
                                    print('en dan nu de laatste vragen...')
                                    Hobby = input('Bent u als een clown en vindt u het leuk om mensen aan het lachen te krijgen? J/N ')
                                    if Hobby == 'j' or Hobby == 'J':
                                        Dier = input('Bent u comfortabel met (circus) dieren? J/N ')
                                        if Dier == 'j' or Dier == 'J':
                                            Act = input('Bent u goed in acteren? J/N ')
                                            if Act == 'j' or Act == 'J':
                                                print('Gefeliciteerd, '+ str(name) +'! U bent een geschikte kandidaat en u komt in aanmerking voor een persoonlijk gesprek.')
                                            elif Act == 'n' or Act == 'N':
                                                print('Sorry ' + str(name) + ', u kunt niet acteren dus u komt niet in aanmerking voor een persoonlijke gesprek.')
                                            else:
                                                print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                        elif Dier == 'n' or Dier == 'N':
                                            print('Sorry ' + str(name) + ', u bent niet comfortabel met dieren dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                        else:
                                            print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                    elif Hobby == 'n' or Hobby == 'N':
                                        print('Sorry ' + str(name) + ', u heeft niet de juiste hobbies voor de functie, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                    else:
                                        print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                                elif Certificaat2 == 'n' or Certificaat2 == 'N':
                                    print('Sorry ' + str(name) + ', u heeft geen certificaat \'Overleven met gevaarlijk personeel\' in bezit, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
                                else:
                                    print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                            elif Massa2 == 'n' or Massa2 == 'N':
                                print('Sorry ' + str(name) + ', uw massa is kleiner dan 90 kg, dus u komt niet in aanmerking voor een sollicitatiegesprek.')
                            else:
                                print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
                        else:
                            print('Sorry ' + str(name) + ', u heeft geen (rode) krulhaar (langer dan 10 cm), dus u komt niet in aanmerking voor een persoonlijk gesprek')
                    else:
                        print('Type uw geslacht in')
                elif Hoed == 'n' or Hoed == 'N':
                    print('Sorry ' + str(name) + ', u heeft geen hoed in bezit dus u komt niet in aanmerking voor ene persoonlijk gesprek.')
                else:
                    print('Beantwoordt alsutblieft met \'j/J\' of \'n/N\'.')
            elif Rijbewijs == 'n' or Rijbewijs == 'N':
                print('Sorry ' + str(name) + ', u heeft geen (geldig) vrachtwagenrijbewijs, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
            else:
                print('Beantwoordt alsutblieft met \'j/J\' of \'n/N\'.')
        elif Diploma == 'n':
            print('Sorry ' + str(name) + ', u heeft geen MBO 4 diploma in Ondernemen, dus u komt niet in aanmerking voor een persoonlijk gesprek.')
        else:
            print('Beantwoordt alsublieft met \'j/J\' of \'n/N\'.')
    else:
        print('Sorry ' + str(name) + ', u heeft weinig ervaring met '+ str(Ervaring) +', dus u komt niet in aanmerking voor een persoonlijk gesprek.')
elif Ervaring == 'n' or Ervaring == 'N':
    print('Sorry ' + str(name) + ', u bezit niet over de juiste ervaring, dus u komt niet in aanmerking voor een persoonlijke gesprek.')
else:
    print('Beantwoordt alsutblieft met de 3 gegeven keuzes.')