import time
import os
import sys
sys.setrecursionlimit(10000)

def write(sdvig, obr):

    width = 210
    heigth = 49
    wh = width//heigth
    r = heigth/2
    pp = 24/11
    string = ''

    #while(True):
    if width == 210:
        for i in range(heigth):
            for j in range(width-1):

                x = (j-width/2)*wh
                y = ((i-heigth/2)*wh)*pp
                r = heigth*2
                if ((x-sdvig)**2+y**2)<= r**2:
                    string=string+'0'
                else:
                    string=string+' '
            string=string+'\n'

        print(string)
        
        #os.system('cls')
        if obr == True:
            if sdvig>-310:
                sdvig=sdvig-20
            else:
                obr = False

        elif obr==False:
            if sdvig<310:
                sdvig=sdvig+20
            else:
                obr = True
        time.sleep(0.04) 
        write(sdvig, obr)
        
        
write(0, False)