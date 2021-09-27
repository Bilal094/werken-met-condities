Munten = 1
Health = 100
print('---------------------------------------------------------------------------------------------')
print('| Als toerist lijkt je het leuk om op trip te gaan naar de Sahara-woestijn in Noord-Afrika. |')
print('| Maar plotseling weet je je weg niet meer terug te vinden door de hitte van de zon...      |')
print('| Je raakt in paniek maar tegelijkertijd denk je ook dat paniek het maar erger maakt en je  |')
print('| denkt dat je de weg wel terug zal vinden. Je hebt een grote rugzak met daarin 3 flessen   |')
print('| water en je drink er 1 op wegens de dorst die door de hitte is veroorzaakt. Daarnaast heb |')
print('| je een tent bij je en een slaapzak. Het is op dit moment het heetste moment van de dag... |')
print('---------------------------------------------------------------------------------------------')
from time import sleep
sleep(15)
print('Level-1: Je loopt al een eindje door het zand en er blijkt geen hoop te zijn. Wat doe je nu?')
from time import sleep
sleep(2.5)

print('1: Je loopt nog een eindje door in de hoop dat je misschien een klein onderdakje tegenkomt')
print('2: Je besluit om op een kleine rots te gaan zitten en uit te rusten')

lvl1 = input('Type je keuze door alleen het cijfer in te typen ')
from time import sleep
sleep(0.5)
if lvl1 == '1':
    print('Level-2: Je hebt een grot gevonden die naar een onbekende plek leidt')
    from time import sleep
    sleep(1)
    print('1: Je gaat er naar binnen om te verkennen')
    print('2: Je bent onzeker en je gebruikt je tent om te schuilen van de zon')
    lvl2 = input('')
    if lvl2 == '1':
        from time import sleep
        sleep(0.5)
        print('Level-2: Het is veelste donker om te kunnen zien dus je gebruikt je zaklamp')
        from time import sleep
        sleep(1)
        print('Je schijnt je zaklamp op een reuze, giftige zandadder!')
        from time import sleep
        sleep(0.5)
        print('Health = 100')
        print('1: Doodt het met een steen')
        print('2: Loop eromheen')
        lvl3 = input('')
        if lvl3 == '1':
            print('Je pakt een grote steen en plet de slang ermee')
            from time import sleep
            sleep(1)
            print('Level-3: Je loopt verder en ziet vele gangen en je hebt de angst om verdwaald te raken. Je maakt een keuze tussen 3 gangen')
            from time import sleep
            sleep(1.3)
            print('1: De linkergang')
            print('2: De middelste gang')
            print('3: De rechtergang')
            lvl4 = input('')
            if lvl4 == '1':
                print('De linkergang loopt dood')
            elif lvl4 == '2':
                print('Level-4: Je komt een magiër tegen en hij biedt je een dolk aan tegen 10 munten. Je hebt 25 munten.')
                from time import sleep
                sleep(1)
                print('1: Koop de dolk')
                print('2: Sla het aanbod af')
                lvl5 = (input(''))
                if lvl5 == '1' and Munten >= 10:
                    print('Level-5: Je bent nu in bezit van een dolk en je wist een jager schorpioen te doden.')
                    from time import sleep
                    sleep(1.5)
                    print('Na een tijdje doorgebracht te hebben in de grot, begin je honger te krijgen')
                    from time import sleep
                    sleep(1.5)
                    print('Je komt erachter dat je geen proviand bij je hebt')
                    from time import sleep
                    sleep(1.5)
                    print('Je hebt nu een keuze om uit de grot te gaan om voedsel te zoeken')
                    from time import sleep
                    sleep(1.5)
                    print('...of je blijft in de grot voor je eigen veiligheid en misschien vind je wel voedsel in de grot')
                    from time import sleep
                    sleep(2)
                    print('1: Blijf in de grot')
                    print('2: Ga de grot uit om voedsel te vinden')
                    lvl6 = input('')
                    if lvl6 == '1':
                        print('Je hebt besloten om in de grot te blijven')
                        from time import sleep
                        sleep(1.8)
                        print('Je hebt na een lange tijd geprobeerd om voedsel te vinden om je honger te stillen')
                        from time import sleep
                        sleep(1)
                        print('Het was geen succes...')
                        from time import sleep
                        sleep(1)
                        print('Game over!')
                    elif lvl6 == '2':
                        print('Je vindt een ander uitweg uit de grot en je ziet in de verte...')
                        from time import sleep
                        sleep(1.5)
                        print('...een oase! Perfect om te overleven...')
                        from time import sleep
                        sleep(1.5)
                        print('...en je komt een handelaar tegen met een mooie aanbod...')
                        from time import sleep
                        sleep(1.5)
                        print('De handelaar biedt je veedieren aan zodat je een bron hebt van vlees en melk')
                        from time import sleep
                        sleep(1.5)
                        print('of je maakt je voedsel door zelf zaadjes te planten')
                        from time import sleep
                        sleep(1.5)
                        print('De kosten zijn 20 munten. Je hebt 15 munten')
                        from time import sleep
                        sleep(1.5)
                        print('1: Sla het bod af')
                        lvl7 = input('')
                        if lvl7 == '1' and Munten <= 20:
                            print('Je saldo is helaas lager dan 20 munten en je moest de aanbod afslaan')
                            from time import sleep
                            sleep(1.5)
                            print('Level-8: Terwijl je de oase aan het verkennen bent, kom je vijandige buren tegemoet.')
                            from time import sleep
                            sleep(1.5)
                            print('1: Probeer te onderhandelen')
                            print('2: Gebruik je dolk')
                            lvl8 = input('')
                            if lvl8 == '1':
                                print('Je probeert te onderhandelen maar de vijandige nomaden zijn er niet van gediend')
                                from time import sleep
                                sleep(1.5)
                                print('Game over!')
                            elif lvl8 == '2':
                                print('Je gebruikt je dolk die je had gekocht')
                                from time import sleep
                                sleep(1.5)
                                print('Je verwondt er één en je bent gestoken in je been')
                                from time import sleep
                                sleep(1.5)
                                print('Health = 60, Level-9')
                                print('1: Gebruik een pijlenboog die je op de grond ziet')
                                print('2: Gebruik je dolk')
                                lvl9 = input('')
                                if lvl9 == '1':
                                    print('Je grijpt naar de pijlenboog van de grond')
                                    from time import sleep
                                    sleep(1,5)
                                    print('Je schiet er 2 neer en verjaagt de rest')
                                    from time import sleep
                                    sleep(1,5)
                                    print('De oase is nu vrij van elk gevaar')
                                    from time import sleep
                                    sleep(1.5)
                                    print('De oase ligt toevallig naast een handelsroute - iets waarvan jij gebruik van kan maken!')
                                    from time import sleep
                                    sleep(1.5)
                                    print('Win!')
                                elif lvl9 == '2':
                                    print('Je gebruikt je dolk maar die breekt in het midden van de gevecht')
                                    from time import sleep
                                    sleep(2)
                                    print('Health = 0, game over!')
                            else:
                                ('Type a.u.b een gegeven keuze')
                elif lvl5 == '2':
                    print('Je hebt de aanbod afgewezen, of je hebt te weinig munten.')
                    from time import sleep
                    sleep(1.5)
                    print('Level-6: Je loopt verder en je komt weer een zandadder tegen!')
                    from time import sleep
                    sleep(1.5)
                    print('1: Spring erover heen')
                    print('2: Probeer de slang te grijpen en ermee te slingeren')
                    lvl6 = input('')
                    if lvl6 == '1':
                        print('Je probeert eroverheen te springen maar de adder weet jou net te bijten')
                        from time import sleep
                        sleep(1.5)
                        print('Game over!')
                    elif lvl6 == '2':
                        print('Je probeert de adder te grijpen...')
                        from time import sleep
                        sleep(1.5)
                        print('...maar bijt jou voordat je je handen op hem legt')
                        from time import sleep
                        sleep(1.5)
                        print('Game over!')
                    else:
                        ('Type a.u.b een gegeven keuze')
            elif lvl4 == '3':
                print('In de rechtergang nestelt zich een zaagchubadder, maar je wist ze te vermijden')
                from time import sleep
                sleep(1.5)
                print('Voordat je dieper in gaat, zie je een gat boven je, maar je kunt daar niks zien door de stralen van de zon')
                from time import sleep
                sleep(1.5)
                print('Level-4: Je vermoedt dat er mensen boven zijn, omdat je geklets en menselijke activiteiten hoort')
                print('1: Ga dieper de grot in')
                print('2: Klim uit het gat')
                lvl5 = input('')
                if lvl5 == '1':
                    print('Je denkt niet dat het verstandig om uit het gat te klimmen...')
                    from time import sleep
                    sleep(1.5)
                    print('Je loopt door en je gaat maar dieper... dieper...')
                    from time import sleep
                    sleep(1.5)
                    print('...totdat je de weg kwijt bent en verder niks kan doen dan alleen op de dood wachten')
                    from time import sleep
                    sleep(1.5)
                    print('Game over!')
                elif lvl5 == '2':
                    print('Je klimt uit het gat...')
                    from time import sleep
                    sleep(1.5)
                    print('...en het is waar: je bent in een dorp terechtgekomen en dus, gered!')
                    from time import sleep
                    sleep(1.5)
                    print('Win!')
                else:
                    print('Type a.u.b een gegeven keuze')
        elif lvl3 == '2':
            print('Je probeert eromheen te lopen maar de slang was sneller en was in staat om jou te bijten en te doden')
            from time import sleep
            sleep(1)
            print('Game over!')
        else:
            print('Type a.u.b een gegeven keuze')
    elif lvl2 == '2':
        print('Je pakt je tent en zet hem op. Al gauw wordt het donker, dus je pakt ook je slaapzak erbij')
        from time import sleep
        sleep(2)
        print('Het begint ook tegelijkertijd te gaan regenen, maar dat baart geen zorgen bij jou')
        from time import sleep
        sleep(2)
        print('Je sluit je ogen terwijl het buiten de tent spettert met regen')
        from time import sleep
        sleep(2.5)
        print('Verdrinking is de meest voorkomende doodsoorzaak in een woestijn, iets waar jij over zou twijfelen')
        from time import sleep
        sleep(2.5)
        print('Het begint langzaam te vloeden terwijl jij niks doorhebt en jij aan het pitten bent...')
        from time import sleep
        sleep(2.5)
        print('Het water reikt jouw mond en dringt zo je longen in en je \'verdrinkt\' in een zandwoestijn...')
        from time import sleep
        sleep(3)
        print('Game over!')
    else:
        print('Type a.u.b een gegeven keuze')
elif lvl1 == '2':
    from time import sleep
    sleep(0.5)
    print('Level-2: Je krijgt het veelste warm van de zon en je hebt weer dorst')
    from time import sleep
    sleep(1.5)
    print('1: Drink nog 1 fles')
    print('2: Volhouden en hopen dat de dorst vanzelf verdwijnt')
    lvl2 = input('')
    if lvl2 == '1':
        print('Terwijl jij naar een fles aan het zoeken bent in je rugzak...')
        from time import sleep
        sleep(1.5)
        print('...verschijnt er ineens een gestreepte hyena achter je rug om!')
        from time import sleep
        sleep(1.5)
        print('Level-2: Wat doe je nu?')
        print('1: Vecht met de hyena')
        print('2: Doe alsof je dood bent')
        print('3: Schreeuw om hulp in een leeg woestijn')
        lvl3 = input('')
        if lvl3 == '1':
            print('Je dacht dapper te zijn om tegen de hyena te vechten...')
            from time import sleep
            sleep(1.5)
            print('...maar de gestreepte hyena is sterker dan jij en wint de duel')
            from time import sleep
            sleep(1.5)
            print('Game over!')
        elif lvl3 == '2':
            print('Je valt neer en doet alsof je dood bent')
            from time import sleep
            sleep(1.5)
            print('maar de hyena trapt er niet en verscheurt je  helemaal total-loss')
            from time import sleep
            sleep(1.5)
            print('Game over!')
        elif lvl3 == '3':
            print('Uit angst schreeuw je het allemaal uit')
            from time import sleep
            sleep(1.5)
            print('Zo hard dat er nomaden die in de buurt zitten het horen')
            from time import sleep
            sleep(1.5)
            print('Al gauw zien ze jou, doden de hyena en vangen ze jou open en je bent gered!')
            from time import sleep
            sleep(1.5)
            print('Win!')
        else:
            print('Type a.u.b een gegeven keuze')
    elif lvl2 == '2':
        print('Je probeert het nog even vol te houden...')
        from time import sleep
        sleep(1.5)
        print('...totdat je neervalt van uitdroging')
        from time import sleep
        sleep(1.5)
        print('Game over!')
    else:
        ('Type a.u.b een gegeven keuze')
else:
    print('Type a.u.b een gegeven keuze')