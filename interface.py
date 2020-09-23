import PySimpleGUI as sg
import time
import random

sg.theme('DarkAmber') # window theme

cash=1000
last_game_notes = ['']
last_game=''
animal=0
bet=''

layout = [
    [    
        sg.Frame('',[
            [
                sg.Frame('Results',[
                    [
                        sg.Text(last_game,size=(55,16))
                    ],
                ]),
            ],
            #RAW 2
            [
                sg.Frame('Do your Bet',[
                    [
                        sg.Frame('Game Mode',[
                            [
                                sg.Radio('Dry','mode', key='dry', default=True), 
                                sg.Radio('Siege', 'mode', key='siege', default=False),
                                sg.Radio('Decade Dry', 'mode', key='decade_d', default=False),
                                sg.Radio('Decade Siege', 'mode', key='decade_s', default=False),
                                sg.Radio('Hundred Dry', 'mode', key='hundred_d', default=False),
                            ],
                            [
                                sg.Radio('Hundred Siege', 'mode', key='hundred_s', default=False),
                                sg.Radio('Thousand Dry', 'mode', key='thousand_d', default=False),
                                sg.Radio('Thousand Siege', 'mode', key='thousand_s', default=False)
                            ]              
                        ])
                    ],
                    [
                        sg.Frame('Value',[
                            [
                                sg.Slider(range=(0, cash), orientation='h', size=(45, 15), default_value=0, tick_interval=(int(cash/4)), key='bet'),
                                
                            ]
                        ])
                    ],
                ])
            ],
            # RAW 3
            [
            sg.Button('BET', size=(15,1)),
            sg.Frame('Wallet',[
                    [
                        sg.Text('R$'),
                        sg.Text(cash, size=(10, None), justification='Left') 
                    ],
            ]),
            sg.Button('Add Money', size=(15,1)),
            ]

        ]),
        sg.Frame('Animals',[
            [
                sg.Frame('',[
                    [
                        sg.Radio('Ostrich: 01, 02, 03, 04','animal', key='1', default=True), 
                        sg.Radio('Eagle: 05, 06, 07, 08', 'animal', key='2', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Donkey: 09, 10, 11, 12','animal', key='3', default=False), 
                        sg.Radio('Butterfly: 13, 14, 15, 16', 'animal', key='4', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Dog: 17, 18, 19, 20','animal', key='5', default=False), 
                        sg.Radio('Goat: 21, 22, 23, 24', 'animal', key='6', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Ram: 25, 26, 27, 28','animal', key='7', default=False), 
                        sg.Radio('Camel: 29, 30, 31, 32', 'animal', key='8', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Snake: 33, 34, 35, 36','animal', key='9', default=False), 
                        sg.Radio('Rabbit: 37, 38, 39, 40', 'animal', key='10', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Horse: 41, 42, 43, 44','animal', key='11', default=False), 
                        sg.Radio('Elephant: 45, 46, 47, 48', 'animal', key='12', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Rooster: 49, 50, 51, 52','animal', key='13', default=False), 
                        sg.Radio('Cat: 53, 54, 55, 56', 'animal', key='14', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Alligator: 57, 58, 59, 60','animal', key='15', default=False), 
                        sg.Radio('Lion: 61, 62, 63, 64', 'animal', key='16', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Monkey: 65, 66, 67, 68','animal', key='17', default=False), 
                        sg.Radio('Pig: 69, 70, 71, 72', 'animal', key='18', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Peacock: 73, 74, 75, 76','animal', key='19', default=False), 
                        sg.Radio('Peru: 77, 78, 79, 80', 'animal', key='20', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Bull: 81, 82, 83, 84','animal', key='21', default=False), 
                        sg.Radio('Tiger: 85, 86, 87, 88', 'animal', key='22', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Bear: 89, 90, 91, 92','animal', key='23', default=False), 
                        sg.Radio('Deer: 93, 94, 95, 96', 'animal', key='24', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Cow: 97, 98, 99, 00','animal', key='25', default=False), 
                    ]
                ]),
            ],
        ])
    ]
]

janela = sg.Window('Jogo do Bicho', layout)

        

def iniciar(self):
    global cash, playing, bet, animal
    while True:

        button, values = janela.Read() # get the window info

        if values['1'] == True: animal=1
        elif values['2'] == True: animal=2
        elif values['3'] == True: animal=3
        elif values['4'] == True: animal=4
        elif values['5'] == True: animal=5
        elif values['6'] == True: animal=6
        elif values['7'] == True: animal=7
        elif values['8'] == True: animal=8
        elif values['9'] == True: animal=9
        elif values['10'] == True: animal=10
        elif values['11'] == True: animal=11
        elif values['12'] == True: animal=12
        elif values['13'] == True: animal=13
        elif values['14'] == True: animal=14
        elif values['15'] == True: animal=15
        elif values['16'] == True: animal=16
        elif values['17'] == True: animal=17
        elif values['18'] == True: animal=18
        elif values['19'] == True: animal=19
        elif values['20'] == True: animal=20
        elif values['21'] == True: animal=21
        elif values['22'] == True: animal=22
        elif values['23'] == True: animal=23
        elif values['24'] == True: animal=24
        elif values['25'] == True: animal=25

        if values['dry'] == True: mode='dry'
        elif values['siege'] == True: mode='siege'
        else: last_game_notes=last_game_notes+'Unavailable Game Mode'

        bet = values['bet']

        if button == sg.WIN_CLOSED: 
            break

        if button == 'Add Money':
            cash=cash+1000
            janela.Refresh()
            break

        if button == 'BET':
            playing=False
            break

def sorteio(): # get the random result of the game
    num1 = random.randint(0,9999)
    num2 = random.randint(0,9999)
    num3 = random.randint(0,9999)
    num4 = random.randint(0,9999)
    num5 = random.randint(0,9999)

    num1 = str(num1).zfill(4)
    result1 = num1
    result1 = str(result1[2]+result1[3])

    num2 = str(num2).zfill(4)
    result2 = num2
    result2 = str(result2[2]+result2[3])

    num3 = str(num3).zfill(4)
    result3 = num3
    result3 = str(result3[2]+result3[3])

    num4 = str(num4).zfill(4)
    result4 = num4
    result4 = str(result4[2]+result4[3])
    
    num5 = str(num5).zfill(4)
    result5 = num5
    result5 = str(result5[2]+result5[3])

    return num1, num2, num3, num4, num5, result1, result2, result3, result4, result5     

while True:

    

    cash=1000
    last_game_notes = ['']
    last_game=''
    for line in last_game_notes:
        last_game = last_game + line + '\n' 

    playing = True
    while playing:
        iniciar(janela)
        time.sleep(0.5)
        
        
    
    num1, num2, num3, num4, num5, result1, result2, result3, result4, result5 = sorteio()

    janela.Refresh()

