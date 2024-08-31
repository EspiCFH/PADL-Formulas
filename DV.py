import json
# Data Validation for {sheetname} page
#get sheet name
with open('config.json') as confile:
    conjson = json.load(confile)
    sheetname = conjson['Sheet Name']
print('Players?')
while True:
    players = input('')
    if players.isnumeric() == False:
        print('INVALID RESPONSE, please try again')
    else:
        players = int(players)
        break

print('\nFormulas will be printed in the following format:')
print('Data Validation\nDropdown (from range)\n')
def printDV(tera1,tera2,games1,games2,droprange1,droprange2):
    DVF = f'{sheetname}!J{tera1}:J{tera2},{sheetname}!L{games1}:L{games2},{sheetname}!P{games1}:P{games2},{sheetname}!T{games1}:T{games2},{sheetname}!X{games1}:X{games2},{sheetname}!AB{games1}:AB{games2},{sheetname}!AF{games1}:AF{games2},{sheetname}!AJ{games1}:AJ{games2},{sheetname}!AN{games1}:AN{games2},{sheetname}!AR{games1}:AR{games2},{sheetname}!AV{games1}:AV{games2},{sheetname}!AZ{games1}:AZ{games2},{sheetname}!BD{games1}:BD{games2},{sheetname}!BH{games1}:BH{games2},{sheetname}!BL{games1}:BL{games2},{sheetname}!BP{games1}:BP{games2},{sheetname}!BT{games1}:BT{games2},{sheetname}!BX{games1}:BX{games2}'
    DRR = f'={sheetname}!$B${droprange1}:$B${droprange2}'
    print(DVF+'\n'+DRR+'\n')
for i in range(0,players):
    t1 = 19*i+5
    t2 = t1+2
    g1 = t1
    g2 = g1+5
    dr1 = t1
    dr2 = dr1+11

    printDV(t1,t2,g1,g2,dr1,dr2)

input('PRESS ENTER TWICE TO EXIT')
input('')
