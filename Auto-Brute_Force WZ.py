import pyautogui
import time
import ctypes

pyautogui.FAILSAFE=False

def run(code,x,y):

    for i in code:
    
        t1 = 0.001
        
        if i=='0':
            pyautogui.moveTo(0.5*x,0.596*y,duration=t1)
            pyautogui.click(0.5*x,0.596*y)
        elif i=='1':
            pyautogui.moveTo(0.442*x,0.323*y,duration=t1)
            pyautogui.click(0.442*x,0.323*y)
                    
        elif i=='2':
            pyautogui.moveTo(0.5*x,0.323*y,duration=t1)
            pyautogui.click(0.5*x,0.323*y)
        elif i=='3':
            pyautogui.moveTo(0.558*x,0.323*y,duration=t1)
            pyautogui.click(0.558*x,0.323*y)
        elif i=='4':
            pyautogui.moveTo(0.442*x,0.413*y,duration=t1)
            pyautogui.click(0.442*x,0.413*y)
        elif i=='5':
            pyautogui.moveTo(0.5*x,0.413*y,duration=t1)
            pyautogui.click(0.5*x,0.413*y)
        elif i=='6':
            pyautogui.moveTo(0.558*x,0.413*y,duration=t1)
            pyautogui.click(0.558*x,0.413*y)
        elif i=='7':
            pyautogui.moveTo(0.442*x,0.504*y,duration=t1)
            pyautogui.click(0.442*x,0.504*y)
            
        elif i=='8':
            pyautogui.moveTo(0.5*x,0.504*y,duration=t1)
            pyautogui.click(0.5*x,0.504*y)
        elif i=='9':
            pyautogui.moveTo(0.558*x,0.504*y,duration=t1)
            pyautogui.click(0.558*x,0.504*y)

def pos(mouse):
    pos_x=""
    pos_y=""
    x_detect=False
    y_detect=False

    for i in mouse:

        if i==",":
            x_detect=False
            pos_x=int(pos_x)
            
        if i==")":
            y_detect=False
            pos_y=int(pos_y)
            

        if x_detect:
            if i!=",":
                if i != "=":
                    pos_x=pos_x+i
        
        if y_detect:
            if i!=",":
                if i!="=":
                    pos_y=pos_y+i

        if i=="x":x_detect=True
        if i=="y":y_detect=True
        
    return (pos_x,pos_y)
        

def bforce(code):

    end=False

    timer=8

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    
    x=screensize[0]
    y=screensize[1]

    xy=pos(str(pyautogui.position()))
    pos_x=xy[0]
    pos_y=xy[1]
    
    while pos_x>10 or pos_y<y-10:
        xy=pos(str(pyautogui.position()))
        pos_x=xy[0]
        pos_y=xy[1]
        time.sleep(0.25)
            
    time.sleep(1.25)

        
    for i in code:
        
        run(i,x,y)
        
        for i in range(8):

            xy=pos(str(pyautogui.position()))
            pos_x=xy[0]
            pos_y=xy[1]

            if pos_x<10 and pos_y<10:
                end=True
                break
            
            elif pos_x>x-10 and pos_y<10:

                print()
                print("Program paused.")

                while pos_x<x-10 or pos_y<y-10:

                    xy=pos(str(pyautogui.position()))
                    pos_x=xy[0]
                    pos_y=xy[1]
                    
                    if pos_x<10 and pos_y<10:
                        end=True
                        break
                    time.sleep(0.25)

                if not end:
                    print()
                    print("Program resumed.")

                else:break

                time.sleep(1)
            
            time.sleep(0.25)
            
            
        if end:break
        


def check_room(code):

    room=""
    c=0
    n=0
    h=0
    valid=False
    dgt_lis=[]
    dgt_cpt=0
    
    for i in code:

        if not i.isdigit() and i!="c" and i!="n" and i!="h":
            c,n=0,0
            break
        
        if i.isdigit():
            dgt_lis.append(i)

        
        if i=="c":
            c=c+1

        elif i=="n":
            n=n+1

        elif i=="h":
            h=h+1

    if c==0 and n==3 and h==2:
        room="china"

    elif c==1 and n==2 and h==2:
        room="nose"

    elif c==1 and n==3 and h==1:
        room="house"

    if room=="china" or room=="nose" or room=="house":
        valid=True

    if len(code)!=8:valid=False

    for i in dgt_lis:
        for f in dgt_lis:
            if f==i:
                dgt_cpt+=1
                
    if dgt_cpt>3:valid=False

    return (room,valid)


def skip_check(c1,c2):

    room1,room2,skip="","",False
   
    room1=check_room(c1)
    room2=check_room(c2)

    if room1[0]!=room2[0] and room1[1]==room2[1]==True:
        skip=True

    return skip


def print_list(lis):
    
    lim=len(lis)
    ind_stk=0

    for cpt in range(lim):

        x=cpt
        ind_stk=cpt
        stk=lis[cpt]

        for i in lis[cpt:]:

            if int(i)<int(stk):

                ind_stk=x
                stk=i
                
            x=x+1

        tamp=lis[cpt]
        lis[cpt]=lis[ind_stk]
        lis[ind_stk]=tamp

    cpt=0

    bforce(lis)
    

def china_room(code):

    print()
    print("Lucky code detected. Easy to brute-force")
   
    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    lis=[]
   
    for i in num:
        found=False
        for f in code:
            if f==i:
                found=True
        if not found:
            lis_h=lis_h+str(i)

    for h in lis_h:
        lis_n=""
        for i in lis_h:
            if i!=h:
                lis_n=lis_n+i
               
        for n in lis_n:
            
            comb=""
            for i in code:
               
                if i.isdigit():
                    comb=comb+i
                elif i.isalpha:
                    if i=="h":
                        comb=comb+h
                    elif i=="n":
                        comb=comb+n

            lis.append(comb)
                
    print_list(lis)
                   
               
             
def nose_room(code):

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_n=""
    lis_c=""
    lis=[]

    for i in code:
        if i.isdigit():
            lis_n=lis_n+i

    for i in num:
            found=False
            for f in code:
                if f==i:
                    found=True
            if not found:
                lis_c=lis_c+str(i)

    for n in lis_n:

        for c in lis_c:
            lis_h=""
           
            for i in lis_c:
                if i!=c:
                    lis_h=lis_h+i
         
            for h in lis_h:
        
                comb=""
                for i in code:
                   
                    if i.isdigit():
                        comb=comb+i
                    elif i.isalpha:
                        if i=="c":
                            comb=comb+c
                        elif i=="n":
                            comb=comb+n
                        elif i=="h":
                            comb=comb+h
                           
                lis.append(comb)

    print_list(lis)



def house_room(code):

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    lis_c=""
    lis=[]

    for i in code:
        if i.isdigit():
            lis_h=lis_h+i

    for i in num:
            found=False
            for f in code:
                if f==i:
                    found=True
            if not found:
                lis_c=lis_c+str(i)

           
    for h in lis_h:

        for c in lis_c:
            lis_n=""
           
            for i in lis_c:
                if i!=c:
                    lis_n=lis_n+i
         
            for n in lis_n:
            
                comb=""
                for i in code:
                   
                    if i.isdigit():
                        comb=comb+i
                    elif i.isalpha:
                        if i=="c":
                            comb=comb+c
                        elif i=="n":
                            comb=comb+n
                        elif i=="h":
                            comb=comb+h
                           
                lis.append(comb)

    print_list(lis)
       


def code1(c1):
    
    print()
    print("Open game tab and place cursor on lower left corner to start.")
    
    room=check_room(c1)[0]

    if room=="china":
        china_room(c1)

    elif room=="nose":
        nose_room(c1)

    elif room=="house":
        house_room(c1)
   




def code2(c1,c2):

    print()
    print("2 valid codes detected.")
    print()
    print("Open game tab and place cursor on lower left corner to start.")
    
    pile=[]

    c,n,h=-1,-1,-1

    for i in range(8):
        if c1[i].isalpha() and c2[i].isdigit():
            if c1[i]=="c":
                c=int(c2[i])
            elif c1[i]=="n":
                n=int(c2[i])
            elif c1[i]=="h":
                h=int(c2[i])

        if c2[i].isalpha() and c1[i].isdigit():
            if c2[i]=="c":
                c=int(c1[i])
            elif c2[i]=="n":
                n=int(c1[i])
            elif c2[i]=="h":
                h=int(c1[i])


    if c==-1:
        stk="c"

    if n==-1:
        stk="n"
       
    if h==-1:
        stk="h"

    code=""

    for i in c1:
        if i.isdigit():
            code=code+i
        elif i.isalpha():
           
            if i=="c" and c>-1:
                code=code+str(c)
               
            elif i=="n" and n>-1:
                code=code+str(n)
               
            elif i=="h" and h>-1:
                code=code+str(h)
               
            else:
                code=code+i

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis=""

    for i in num:
        found=False
        for f in code:
            if f==i:
                found=True
        if not found:
            lis=lis+str(i)


    for i in lis:
        bforce_code=""
       
        for f in code:
            if f==stk:
                bforce_code=bforce_code+i
            else:
                bforce_code=bforce_code+f
               
            
           
        pile.append(bforce_code)


    bforce(pile)


valid=False

while not valid:

    c1=input(("code 1: ")).lower()
    c2=input(("code 2: ")).lower()
    
    if c2=="":
        valid = check_room(c1)[1]
        if valid==True: 
            code1(c1)
        

    elif skip_check(c1,c2):
        code2(c1,c2)
        valid=True
        
    if not valid:
        print()
        print("INVALID CODE(S). TRY AGAIN.")
        print()

print()
print("PROGRAM FINISHED") 
