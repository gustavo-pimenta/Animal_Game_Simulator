import PySimpleGUI as sg
import time


sg.theme('DarkAmber') # window theme

layout = [
    [sg.Text('pipipi:')],
    [sg.Radio('popopo','shot', key='single', default=True), sg.Radio('pipipi', 'shot', key='multiple', default=False)],  
    [sg.Text('')],
    [sg.Text('popopo:')],
    [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='recoil_size')],     
    [sg.Text('')],
    [sg.Text('pipipi:')],
    [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='fire_rate')],           
    [sg.Text('')],
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
