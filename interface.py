import PySimpleGUI as sg
import time


sg.theme('DarkAmber') # window theme

cash=77
energy = 50
last_game_notes = ['']
last_game=''
for line in last_game_notes:
    last_game = last_game + line + '\n' 
    print (last_game)
    
week_output = 'pipipi popopo'



layout = [

    # RAW 1
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
            ]

        ]),
        sg.Frame('Animals',[
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='1', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='2', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='1', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='2', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='3', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='4', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='5', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='6', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='7', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='8', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='9', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='10', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='11', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='12', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='13', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='14', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='15', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='16', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='17', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='18', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='19', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='20', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='21', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='22', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='23', default=True), 
                        sg.Radio('Águia: 05, 06, 07, 08', 'animal', key='25', default=False),
                    ]
                ]),
            ],
            [
                sg.Frame('',[
                    [
                        sg.Radio('Avestruz: 01, 02, 03, 04','animal', key='25', default=True), 
                    ]
                ]),
            ],
        ])
    ]

]

janela = sg.Window('Jogo do Bicho', layout)
# janela.Maximize()
        

def Iniciar(self):
    while True:

        button, values = janela.Read() # get the window info

        single = values['single']
        multiple = values['multiple']
        recoil_size = values['recoil_size']
        fire_rate = values['fire_rate']
        start_stop = button

        if button == sg.WIN_CLOSED: 
            break

        if button == 'Stop':
            print('parou')
            # break_program = True

        if button == 'Start':
            print('roda')
            # break_program = True

        # return single, multiple, recoil_size, fire_rate, start_stop
        print(single, multiple, recoil_size, fire_rate, start_stop)


Iniciar(janela)
