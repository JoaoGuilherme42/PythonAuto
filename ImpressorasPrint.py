from turtle import title
import pyautogui
import time
import os
import webbrowser
import pymsgbox

num1 = int(pyautogui.prompt(text='Você deseja tirar um print de TODAS as impressoras por contrato ou individual?\nDigite 1 para TODAS\nDigite 2 para INDIVIDUAL',
           title='Developed by JoaoGuilherme'))

if(num1 == 1):
    num2 = int(pyautogui.prompt(text='Digite 1 para o contrato da H2L\nDigite 2 para o contrato da COPIER',
                                title='Developed by JoaoGuilherme'))
    if(num2 == 1):
        webbrowser.open('http://192.168.0.210/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        dptoScreen = pyautogui.screenshot()
        dptoScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Departamento Pessoal.png')
        webbrowser.open('http://192.168.0.211/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        recepScreen = pyautogui.screenshot()
        recepScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Recepção do Recanto.png')
        webbrowser.open('http://192.168.0.213/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        farmaScreen = pyautogui.screenshot()
        farmaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Farmácia.png')
        webbrowser.open('http://192.168.0.214/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        ambuScreen = pyautogui.screenshot()
        ambuScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Ambulatório.png')
        webbrowser.open('http://192.168.0.215/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        chefScreen = pyautogui.screenshot()
        chefScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Chefia de Enfermagem.png')
        webbrowser.open('http://192.168.0.220/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        finanScreen = pyautogui.screenshot()
        finanScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Financeiro.png')
        webbrowser.open('http://192.168.0.221/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        psicoScreen = pyautogui.screenshot()
        psicoScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Psicologia SUS.png')
        webbrowser.open('http://192.168.0.222/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        eletroScreen = pyautogui.screenshot()
        eletroScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Eletroencefalograma.png')
        webbrowser.open('http://192.168.0.223/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        almoxScreen = pyautogui.screenshot()
        almoxScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Almoxarifado.png')
        webbrowser.open('http://192.168.0.224/#hId-pgDevInfo')
        pyautogui.press('', interval=5)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Hospital Dia.png')
        webbrowser.open('http://192.168.0.212/sws/index.sws')
        pyautogui.press('', interval=7)
        pyautogui.click(x=390, y=170, interval=3)
        pyautogui.click(x=90, y=340, interval=3)
        faturaScreen = pyautogui.screenshot()
        faturaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Faturamento.png')
        webbrowser.open('http://192.168.0.225/sws/index.sws')
        pyautogui.press('', interval=7)
        pyautogui.click(x=390, y=170, interval=3)
        pyautogui.click(x=90, y=340, interval=3)
        faturaScreen = pyautogui.screenshot()
        faturaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Auditoria.png')

    elif(num2 == 2):
        webbrowser.open(
            'http://192.168.0.128/general/information.html?kind=item')
        pyautogui.press('', interval=5)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora da Ala Feminina SUS.png')
        webbrowser.open(
            'http://192.168.0.131/general/information.html?kind=item')
        pyautogui.press('', interval=5)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora da Ala Masculina SUS.png')
        webbrowser.open('http://192.168.0.178/sws/index.html')
        pyautogui.press('', interval=7)
        pyautogui.click(x=360, y=175, interval=3)
        pyautogui.click(x=100, y=335, interval=3)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora do Dr Antonio.png')
        pymsgbox.alert(text='Prints tirados com sucesso',
                       title='Finalizado', button='ok')
    else:
        pyautogui.alert(
            text='Você digitou um número inválido\nFeche o programa e inicie novamente', title='Developed by JoaoGuilherme', button='Ok')
elif(num1 == 2):
    num = int(pyautogui.prompt(text='Você escolheu tirar o print de UMA impressora, escolha:\nDepartamento Pessoal: 1 \nRecepcao Recanto: 2 \nFarmacia: 3\nAmbulatório: 4\nChefia da Enfermagem: 5\nFinanceiro: 6\nPsicologia SUS: 7\nEletroencefalograma: 8\nAlmoxarifado: 9\nHospital Dia: 10\nFaturamento: 11\nAuditoria: 12\nSUS Feminino: 13\nSUS Masculino: 14\nDr. Antônio: 15', title='Developed by JoaoGuilherme', default='0'))
    if(num == 1):
        webbrowser.open('http://192.168.0.210/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        dptoScreen = pyautogui.screenshot()
        dptoScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Departamento Pessoal.png')
    elif(num == 2):
        webbrowser.open('http://192.168.0.211/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        recepScreen = pyautogui.screenshot()
        recepScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Recepção do Recanto.png')
    elif(num == 3):
        webbrowser.open('http://192.168.0.213/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        farmaScreen = pyautogui.screenshot()
        farmaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Farmácia.png')
    elif(num == 4):
        webbrowser.open('http://192.168.0.214/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        ambuScreen = pyautogui.screenshot()
        ambuScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Ambulatório.png')
    elif(num == 5):
        webbrowser.open('http://192.168.0.215/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        chefScreen = pyautogui.screenshot()
        chefScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Chefia de Enfermagem.png')
    elif(num == 6):
        webbrowser.open('http://192.168.0.220/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        finanScreen = pyautogui.screenshot()
        finanScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Financeiro.png')
    elif(num == 7):
        webbrowser.open('http://192.168.0.221/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        psicoScreen = pyautogui.screenshot()
        psicoScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Psicologia SUS.png')
    elif(num == 8):
        webbrowser.open('http://192.168.0.222/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        eletroScreen = pyautogui.screenshot()
        eletroScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Eletroencefalograma.png')
    elif(num == 9):
        webbrowser.open('http://192.168.0.223/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        almoxScreen = pyautogui.screenshot()
        almoxScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Almoxarifado.png')
    elif(num == 10):
        webbrowser.open('http://192.168.0.224/#hId-pgDevInfo')
        pyautogui.press('', interval=3)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Hospital Dia.png')
    elif(num == 11):
        webbrowser.open('http://192.168.0.212/sws/index.sws')
        pyautogui.press('', interval=7)
        pyautogui.click(x=390, y=170, interval=3)
        pyautogui.click(x=90, y=340, interval=3)
        faturaScreen = pyautogui.screenshot()
        faturaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora do Faturamento.png')
    elif(num == 12):
        webbrowser.open('http://192.168.0.225/sws/index.sws')
        pyautogui.press('', interval=7)
        pyautogui.click(x=390, y=170, interval=3)
        pyautogui.click(x=90, y=340, interval=3)
        faturaScreen = pyautogui.screenshot()
        faturaScreen.save(
            r'.\PrintsImpressoras\H2L\Numero de serie e contador da impressora da Auditoria.png')
    elif(num == 13):
        webbrowser.open(
            'http://192.168.0.128/general/information.html?kind=item')
        pyautogui.press('', interval=3)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora da Ala Feminina SUS.png')
    elif(num == 14):
        webbrowser.open(
            'http://192.168.0.131/general/information.html?kind=item')
        pyautogui.press('', interval=3)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora da Ala Masculina SUS.png')
    elif(num == 15):
        webbrowser.open('http://192.168.0.178/sws/index.html')
        pyautogui.press('', interval=3)
        pyautogui.click(x=360, y=175, interval=1)
        pyautogui.click(x=100, y=335, interval=1)
        hospdScreen = pyautogui.screenshot()
        hospdScreen.save(
            r'.\PrintsImpressoras\Copier\Numero de serie e contador da impressora do Dr Antonio.png')
    else:
        pyautogui.alert(
            text='Você digitou um número inválido\nFeche o programa e inicie novamente', title='Developed by JoaoGuilherme', button='Ok')
else:
    pyautogui.alert(
        text='Você digitou um número inválido\nFeche o programa e inicie novamente', title='Developed by JoaoGuilherme', button='Ok')

pymsgbox.alert(text='Prints tirados com sucesso',
               title='Finalizado', button='ok')