import PySimpleGUI as sg
import time


sg.theme('DarkAmber') # window theme

cash=77
last_game = 'resultado do ultimo jogo\nperiquito\n\nvc ganhou 3 real'
week_output = 'pipipi popopo'



layout = [
    # RAW 1
    [
        sg.Frame('Last Week Results',[
            [
                sg.Text(last_game,size=(30, 8))
            ],
        ]),
        sg.Frame('This Week',[
            [
                sg.Text(week_output,size=(30, 8))
            ],
        ])
    ],
    #RAW 2
    [
        sg.Frame('Do your Bet:',[
            [
                sg.Frame('Bet Mode:',[
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
                sg.Text('Game Bet:')
            ],
            [
                sg.Slider(range=(0, cash), orientation='h', size=(50, 15), default_value=0, tick_interval=(int(cash/4)), key='bet')
            ]

        ])
    ],
    #RAW 3
    [
        
    ],
    #RAW 4 
    [sg.Text('')],
    #RAW 5
    
       
    #RAW 7
    
    #RAW 8
    [
        sg.Text('Made by [insert a galera here]                       '), 
        sg.Button('Stop', size=(10,1)), sg.Button('Start', size=(10,1))
    ],
    # RAW 9
    # [sg.Multiline(size=(30, 5), key='textbox')]
]

janela = sg.Window('Jogo do Bicho', layout) 
        

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
