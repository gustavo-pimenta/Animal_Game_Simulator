import PySimpleGUI as sg
import time
import random
import sys

sg.theme('DarkAmber') # window theme

# start variables
cash=1000
last_game_notes = ['']
last_game=''
animal=0
bet=''
mode=''

def create_layout(cash): # set the layout of the window
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
                                    sg.Radio('Dry','mode', key='dry', default=False), 
                                    sg.Radio('Siege', 'mode', key='siege', default=True),
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

    return layout      

def iniciar(window): # get informations collected from the screen and the screen events
    global cash, bet, animal, mode, game
    while True:

        button, values = window.Read() # get the window info

        try:
            if values['1'] == True: animal=[1,2,3,4]
            elif values['2'] == True: animal=[5,6,7,8]
            elif values['3'] == True: animal=[9,10,11,12]
            elif values['4'] == True: animal=[13,14,15,16]
            elif values['5'] == True: animal=[17,18,19,20]
            elif values['6'] == True: animal=[21,22,23,24]
            elif values['7'] == True: animal=[25,26,27,28]
            elif values['8'] == True: animal=[29,30,31,32]
            elif values['9'] == True: animal=[33,34,35,36]
            elif values['10'] == True: animal=[37,38,39,40]
            elif values['11'] == True: animal=[41,42,43,44]
            elif values['12'] == True: animal=[45,46,47,48]
            elif values['13'] == True: animal=[49,50,51,52]
            elif values['14'] == True: animal=[53,54,55,56]
            elif values['15'] == True: animal=[57,58,59,60]
            elif values['16'] == True: animal=[61,62,63,64]
            elif values['17'] == True: animal=[65,66,67,68]
            elif values['18'] == True: animal=[69,70,71,72]
            elif values['19'] == True: animal=[73,74,75,76]
            elif values['20'] == True: animal=[77,78,79,80]
            elif values['21'] == True: animal=[81,82,83,84]
            elif values['22'] == True: animal=[85,86,87,88]
            elif values['23'] == True: animal=[89,90,91,92]
            elif values['24'] == True: animal=[93,94,95,96]
            elif values['25'] == True: animal=[97,98,99,0]
            if values['dry'] == True: mode='dry'
            elif values['siege'] == True: mode='siege'
            else: mode=''
            bet = values['bet']
            bet=int(bet)
        except:
            pass

        if button in (sg.WIN_CLOSED, '_EXIT_', 'Close', 'Quit'):
            window.Close()
            game=False
            break
            
        if button == 'Add Money':
            cash=cash+1000
            break

        if button == 'BET':
            cash=cash-bet
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

    global animal

    if animal==1: animal=[1,2,3,4]

def get_result(result1, result2, result3, result4, result5): # verify if the player number is one of the winner numbers and apply the prize
    global cash, bet, animal, last_game_notes

    win = False

    if mode=='dry':
        for number in animal:
            if int(result1)==number:
                cash=cash+(bet*18)
                last_game_notes.append(('You Win R$ '+(str(bet*18))))
                break

    elif mode=='siege':
        for number in animal:
            if int(result1)==number:
                cash=cash+(bet*3.6)
                last_game_notes.append(('You Win R$ '+(str(bet*3.6))))
                break
            if int(result2)==number:
                cash=cash+(bet*3.6)
                last_game_notes.append(('You Win R$ '+(str(bet*3.6))))
                break
            if int(result3)==number:
                cash=cash+(bet*3.6)
                last_game_notes.append(('You Win R$ '+(str(bet*3.6))))
                break
            if int(result4)==number:
                cash=cash+(bet*3.6)
                last_game_notes.append(('You Win R$ '+(str(bet*3.6))))
                break
            if int(result5)==number:
                cash=cash+(bet*3.6)
                last_game_notes.append(('You Win R$ '+(str(bet*3.6))))
                break

    else: last_game_notes.append('Unavailable Game Mode') 

def write_results(): # write the random numbers to be printed in screen
    global num1, num2, num3, num4, num5, result1, result2, result3, result4, result5, last_game_notes

    last_game_notes.append(num1)  
    last_game_notes.append(num2)
    last_game_notes.append(num3)
    last_game_notes.append(num4)
    last_game_notes.append(num5)
    last_game_notes.append('')

# game main loop
game=True
turn=1
while game:

    # clean some variables in each loop
    animal=0
    bet=''
    mode=''

    # this for loop crate a list, to be printed 
    for line in last_game_notes:
        last_game = last_game + line + '\n' 

    # this 2 options makes 2 screen
    # the second screen opens after the first closes
    # and the first open after the second closes
    # this way, we keep the interface in the screen all time
    if turn==1:
        janela = sg.Window('Jogo do Bicho', create_layout(cash), location=(10,10), no_titlebar=True, grab_anywhere=False).Finalize()
        iniciar(janela)
        try:
            janela2.Close()
        except:
            pass
        turn=0
    else:
        janela2 = sg.Window('Jogo do Bicho', create_layout(cash), location=(10,10), no_titlebar=True, grab_anywhere=False).Finalize()
        iniciar(janela2)
        try:
            janela.Close()
        except:
            pass
        turn=1
            
    # clean the result messages of the last game  
    last_game_notes = ['']
    last_game=''
    
    # get the ramdom numbers
    num1, num2, num3, num4, num5, result1, result2, result3, result4, result5 = sorteio()

    # write the results to be printed in the screen 
    write_results()

    # verify if the player number is one of the winner numbers and apply the prize
    get_result(result1, result2, result3, result4, result5)

# emergency close window in case o program crash
try:
    janela.Close()
except:
    pass
try:
    janela2.Close()
except:
    pass
    