print('Players?')
while True:
    players = input('')
    if players.isnumeric() == False:
        print('INVALID RESPONSE, please try again')
    else:
        players = int(players)
        break

print('\nKills or Deaths?')
print('0 - Kills\n1 - Deaths')
while True:
    KorD = input('')
    if KorD == '0':
        key = 2
        break
    elif KorD == '1':
        key = 3
        break
    else:
        print('INVALID RESPONSE, please try again')

def printKD(up_bound,low_bound, colkey):
    KDF = f'=sum(iferror(VLOOKUP($B{up_bound}, $L${up_bound}:$N${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $P${up_bound}:$R${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $T${up_bound}:$V${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $X${up_bound}:$Z${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $AB${up_bound}:$AD${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $AF${up_bound}:$AH${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $AJ${up_bound}:$AL${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $AN${up_bound}:$AP${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $AR${up_bound}:$AT${low_bound}, {colkey}, 0), 0),iferror(VLOOKUP($B{up_bound}, $AV${up_bound}:$AX${low_bound}, {colkey}, 0), 0),iferror(VLOOKUP($B{up_bound}, $AZ${up_bound}:$BB${low_bound}, {colkey}, 0), 0),iferror(VLOOKUP($B{up_bound}, $BD${up_bound}:$BF${low_bound}, {colkey}, 0), 0),iferror(VLOOKUP($B{up_bound}, $BH${up_bound}:$BJ${low_bound}, {colkey}, 0), 0),iferror(VLOOKUP($B{up_bound}, $BL${up_bound}:$BN${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $BP${up_bound}:$BR${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $BT${up_bound}:$BV${low_bound}, {colkey}, 0), 0), iferror(VLOOKUP($B{up_bound}, $BX${up_bound}:$BZ${low_bound}, {colkey}, 0), 0))'
    print(KDF+'\n')

for i in range(0,players):
    upper = 19*i + 5
    lower = upper + 11
    printKD(upper,lower,key)
