import time
import pyautogui

tentativa =  0
tentativaimg =  0
fase1 = 1
fase2 = 0
email = "exemplo@servidor.com"
senha = "SENHA"
x = 0
y = 0
im = pyautogui.screenshot("fullpic.png")

while (True): 

    while(fase1 == 1):

        try:
            x ,y = pyautogui.locateCenterOnScreen("buttonprenota.png")
            pyautogui.moveTo(x,y)
            pyautogui.click(clicks=1, interval=1)
            x = 0
            y = 0 
            while(x<1):
                try:
                    x ,y = pyautogui.locateCenterOnScreen("load.png")
                except:  
                    time.sleep(0.1) 
            fase1 = 0
        except:
            tentativaimg = tentativaimg +1 
        finally:               
            if(tentativaimg>5):
                try:
                    x ,y = pyautogui.locateCenterOnScreen("button.png")
                    pyautogui.moveTo(x,y)
                    pyautogui.click(clicks=1, interval=1)
                except: 
                    print("OK não encontrado")
                    try:                      
                        x ,y = pyautogui.locateCenterOnScreen("service.png")
                        x ,y = pyautogui.locateCenterOnScreen("load.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.moveTo(0,0)
                        x = 0
                        y = 0 
                        while(x<1):
                            try:
                                x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1) 
                    except:
                        print("Erro de Srvidor não encontrado")
                    try:                      
                        x ,y = pyautogui.locateCenterOnScreen("erro.png")
                        x ,y = pyautogui.locateCenterOnScreen("load.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.moveTo(x,y+100)
                        x = 0
                        y = 0
                        while(x<1):
                            try:
                                x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1) 
                    except:
                        print("Erro de load não encontrado")
                    try:
                        x ,y = pyautogui.locateCenterOnScreen("email.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.write(email)
                        pyautogui.moveTo(x,y+60)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.write(senha) 
                        x ,y = pyautogui.locateCenterOnScreen("loginbutton.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        x = 0
                        y = 0 
                        while(x<1):
                            try:
                                x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1)
                    except:
                        print("Login não encontrado")    

                
                tentativaimg = 0
               

    fase2 = 1
    tentativaimg = 0
    x = 0
    y = 0

    while(fase2 == 1):
        try:
            x ,y = pyautogui.locateCenterOnScreen("button.png")
            pyautogui.moveTo(x,y)
            pyautogui.click(clicks=1, interval=1)
            fase2 = 0
            fase1 = 1  
        except:
            tentativaimg = tentativaimg +1           
        finally:        
            if(tentativaimg>5):
                try:     
                    x ,y = pyautogui.locateCenterOnScreen("buttonprenota.png")
                    pyautogui.moveTo(x,y)
                    pyautogui.click(clicks=1, interval=1)
                    x = 0
                    y = 0 
                    while(x<1):
                        try:
                          x ,y = pyautogui.locateCenterOnScreen("load.png")
                        except:  
                            time.sleep(0.1)  
                except:
                    try:
                        x ,y = pyautogui.locateCenterOnScreen("service.png")
                        x ,y = pyautogui.locateCenterOnScreen("load.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.moveTo(0,0)
                        x = 0
                        y = 0 
                        while(x<1):
                            try:
                                x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1)
                    except:
                        print("Erro de servidor não encontrado")
                    try:                      
                        x ,y = pyautogui.locateCenterOnScreen("erro.png")
                        x ,y = pyautogui.locateCenterOnScreen("load.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.moveTo(0,0)
                        x = 0
                        y = 0 
                        while(x<1):
                            try:
                                x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1)
                    except:
                        print("Erro de load não encontrado")
                    try:
                        x ,y = pyautogui.locateCenterOnScreen("email.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.write(email)
                        pyautogui.moveTo(x,y+60)
                        pyautogui.click(clicks=1, interval=1)
                        pyautogui.write(senha) 
                        x ,y = pyautogui.locateCenterOnScreen("loginbutton.png")
                        pyautogui.moveTo(x,y)
                        pyautogui.click(clicks=1, interval=1)
                        x = 0
                        y = 0 
                        while(x<1):
                            try:
                                 x ,y = pyautogui.locateCenterOnScreen("load.png")
                            except:  
                                time.sleep(0.1)
                    except:
                        print("Login não encontrado")  
                tentativaimg = 0
                                            
    x = 0
    y = 0
    tentativa = tentativa + 1
    print("Tentativa", tentativa)
