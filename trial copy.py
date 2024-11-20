from datetime import datetime
from tabulate import tabulate
import random

# a = 5
# j  = 10
# start = '7:50 am'
# end = '3:30 pm'
a = int(input("Enter number of subjects: "))
j =  int(input("Enter number of periods: "))
start = input('Enter start time of school(For example - 5:30 pm): ') 
end = input ('Enter end time of school: ' )
# c = float(input("Duration of time you want to study in a day(in hours): "))
period  = 0


C = 0
B = 0

def minc(_hr,_de,_B1,_C1):
    global l 
    global C,B
   # y*(40/60)
    
    if start == '7:50 am':
        A = str(round(_hr + _de,2))
    else:  
        A = str(_hr + _de)
    if A.__contains__('.'):
        dot = A.index('.')
        f_string = ''
        # print(A)
        B = int(A[:dot])
        if start=='7:50 am':
            C = round(int(A[dot+1:])*0.6)
        else:
            C = round(int(A[dot+1:])*6,2)
        
        # print(B)
        # print(C)

    
    y = 0
    while y<j+2:

        if start.__contains__('am'):
            


                if C>=60:
                    B = B+(C//60)
                    C = C % 60
        
                
                B9 = str(B)
                C9 = ':'+str(C)

                C_ = (C+_C1)
                B_ = B + _B1


                if y ==  b1start-1 or y== b2start+1:
                    
                    if  y ==  b1start-1:
                        C_ = (C+b1period)
                        B_ = B + B1PERIOD
                        if C_ >= 60:
                            B_ =B_+(C_//60)
                            C_ = C_ % 60
                        B8 =  str(B_) 
                        C8 =   ':'+str(C_)
                        D9 = B9+C9
                        D8 = B8+C8  
                        dic = datetime.strptime(D9, "%H:%M")
                        sic = datetime.strptime(D8, "%H:%M")
                        f_string = f'{dic.strftime("%I:%M %p")} - {sic.strftime("%I:%M %p")}'
                        
                          
                        if not(C_< C1):
                            C = -(C_ -C1)
                        else:
                            C= C_- C1    



                    elif y ==  b2start+1:
                        C_ = (C+b2period)
                        B_ = B + B2PERIOD
                        if C_ >= 60:
                            B_ =B_+(C_//60)
                            C_ = C_ % 60
                        B8 =  str(B_) 
                        C8 =   ':'+str(C_)
                        D9 = B9+C9
                        D8 = B8+C8  
                        dic = datetime.strptime(D9, "%H:%M")
                        sic = datetime.strptime(D8, "%H:%M")
                        f_string = f'{dic.strftime("%I:%M %p")} - {sic.strftime("%I:%M %p")}'

                        if not(C_< C1):
                            C = (C_ -C1)
                        else:
                            C= -(C_- C1)    

    
                    
                
                        

                else:        
                    
                    B9 = str(B)
                    C9 = ':'+str(C)
                    if C9.__contains__('-'):
                        C9.replace('-','')

                    if C_ >= 60:
                        B_ =B_+(C_//60)
                        C_ = C_ % 60



                    B8 =  str(B_) 
                    C8 =   ':'+str(C_)
                    D9 = B9+C9
                    D8 = B8+C8  

                    

                    # print('mmmmmmmmmm',B)
                    dic = datetime.strptime(D9, "%H:%M")
                    sic = datetime.strptime(D8, "%H:%M")
                    
                
                
                    f_string = f'{dic.strftime("%I:%M %p")} - {sic.strftime("%I:%M %p")}'



                    # else:
                    #     f_string = f'{B}:{f"{int(C):02d}"}am - {B_}:{f"{int(C_):02d} am69"}'


                    
                        
                

        elif start.__contains__('pm'):
            
        
                B9 = str(B)
                C9 = ':'+str(C)

                C_ = (C+_C1)
                B_ = B + _B1


                if y ==  b1start-1 or y== b2start-1:
                    if  y ==  b1start-1:
                        C_ = (C+b1period)
                        B_ = B + B1PERIOD

                    elif y ==  b2start-1:
                        C_ = (C+b2period)
                        B_ = B + B2PERIOD

                    if C_ >= 60:
                        B_ =B_+(C_//60)
                        C_ = C_ % 60    




                    B8 =  str(B_) 
                    C8 =   ':'+str(C_)
                    D9 = B9+C9
                    D8 = B8+C8  

                   

                    # print('mmmmmmmmmm',B)
                    dic = datetime.strptime(D9, "%H:%M")
                    sic = datetime.strptime(D8, "%H:%M")
                    
                
                
                    f_string = f'{dic.strftime("%I:%M %p")} - {sic.strftime("%I:%M %p")}'
                


        
        l+=[f_string]
        B=B+ _B1 
        C=C+_C1
        y+=1
             

_BREAK = 0

def _break(_b1period,_b2period):
    global _BREAK
    _BREAK = _b1period+_b2period

def times(strt,nd):
    kk = True
    global period
    global s
    global e, hr, HR, DE, de


    if strt.__contains__(':'): #strt = 7:30 am
        f = strt.index(':')   #f = 1
        g = nd.index(':')     
        hr = int(strt[:f]) #hr  = 7
        mi = float(strt[f+1:-3])

        de = round(mi/60,2)
        
        if strt.__contains__('pm'):
            s = round(hr + de + 12,2)
        elif strt.__contains__('am'):
            s = round(hr + de,2)

        HR = int(nd[:g])
        MI = float(nd[g+1:-3])
        DE =round(MI/60,2)
        # print(s)

        if end.__contains__('pm'):    
            e =round(HR + DE+ 12)

        elif end.__contains__('am'):
            e = round(HR + DE,2)       
            
        # print(e)    


    # else:    

    #     if strt.__contains__('pm'):
    #         s = float(strt[:len(strt)-2])+12
    #     elif strt.__contains__('am'):
    #         s = float(strt[:len(strt)-2]) 

    #     if end.__contains__('pm'):    
    #         e =float(nd[:len(nd)-2])+12
    #     elif end.__contains__('am'):
    #         e = float(nd[:len(nd)-2]) 


    while kk == True:

        if strt.__contains__('pm') and nd.__contains__('am'):
            period = e - s + 12
            kk = False

        elif strt.__contains__('am') and nd.__contains__('pm'):
            period = e - s 
            kk = False

        elif strt.__contains__('pm') and nd.__contains__('pm'):
            if e>=s:
                period = e-s
                kk = False

            else:
                print("Cannot be more than 24 hours. ")
                kk = False
                exit()   

        elif strt.__contains__('am') and nd.__contains__('am'):
            if e>=s:
                period = e-s-12
                kk = False
            else:
                print("Cannot be more than 24 hours. ")
                kk = False
                exit() 
            
          
l = []
P = []
Z = 1
while Z<j+1:
    P.append(Z)
    Z+=1

b1start =  int(input(f'Enter time after which period will be  first break - {P} (Enter period from the list)')) +1

for ele in P:
    if ele >= b1start:
        P.remove(ele)



b2start =  int(input(f'Enter time after which period will be  second break - {P} (Enter period from the list)'))+1

times(start,end)
period1 = period
s1 = s
e1 =e
hr1 = hr   
HR1 = HR
DE1 = DE
de1 = de



b1period = int(input(f'Enter duration of first break: (in minutes))'))
b2period = int(input(f'Enter duration of second break: (in minutes))'))

B1PERIOD = b1period//60
B2PERIOD = b2period//60

_break(b1period, b2period)
# print(_BREAK)

rr  = (period1 - round(_BREAK/60))/j #8-1/10
ROUND = round(rr,2)
p = str(ROUND)
DOT = p.index('.')
B1 = int(p[:DOT]) 
C1 = round(float(p[DOT+1:])*0.06)*10



minc(hr1,de1,B1,C1)



km = True
while km == True:
    if _BREAK > period1:
        print("Break cannot be more than study time")
        break
    else:    
        km = False
        


# day = {1:"Saturday", 2:"Sunday", 3:"Monday", 4:"Tuesday", 5:"Wednesday", 6:"Thursday", 7:"Friday"}

z = 0
l1 = []
l2 = []
F = 0

# while z<a:
#     b = input("Enter subject: ")

#     while V<a:
#         l2.insert(-(j-z),b)
#         z+=1

#         l2.append('')
#         V+=1
#     l2.insert(-(j-z),b)
#     z+=1

while z<a:
  b = input("Enter subject: ")
  l2.append(b)
  l1.append(b)
  z+=1





    

while F<j+3:
    if F == b1start:
        l2.insert(b1start-1,'BREAK 1')
        

    elif F == b2start-4:
        l2.insert(b2start+4, 'BREAK 2') 
        F += 1

    F+=1

V = len(l2)
while V<j+2:
    l2.append(random.choice(l1))
    V+=1



info = {'': l, 'Monday': l2, 'Tuesday': l2, 'Wednesday': l2,'Thursday':l2,'Friday':l2 }

print(tabulate(info, headers='keys', tablefmt='fancy_grid'))