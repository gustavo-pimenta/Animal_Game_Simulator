import PySimpleGUI as sg
import time


sg.theme('DarkAmber') # window theme

cash=77

layout = [
    #RAW 1
    [sg.Text('Bet Mode:')],
    #RAW 2
    [
        sg.Radio('Dry','mode', key='dry', default=True), 
        sg.Radio('Siege', 'mode', key='siege', default=False),
        sg.Radio('Decade Dry', 'mode', key='decade_d', default=False),
        sg.Radio('Decade Siege', 'mode', key='decade_s', default=False),
        sg.Radio('Hundred Dry', 'mode', key='hundred_d', default=False)
    ],
    #RAW 3
    [
        sg.Radio('Hundred Siege', 'mode', key='hundred_s', default=False),
        sg.Radio('Thousand Dry', 'mode', key='thousand_d', default=False),
        sg.Radio('Thousand Siege', 'mode', key='thousand_s', default=False)
    ],
    #RAW 4 
    [sg.Text('')],
    #RAW 5
    [sg.Text('Game Bet:')],
    #RAW 6
    [sg.Slider(range=(0, cash), orientation='h', size=(50, 15), default_value=0, tick_interval=(int(cash/4)), key='bet')],     
    #RAW 7
    [sg.Text('')],
    #RAW 8
    [sg.Text('Made by [insert a galera here]                       '), sg.Button('Stop', size=(10,1)), sg.Button('Start', size=(10,1))]   
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
