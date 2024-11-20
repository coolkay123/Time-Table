from datetime import datetime,timedelta
from tabulate import tabulate
import random
bool_ = True
K = 1

error_message = 'Invalid input. Please try again.'

#number of timetables
while bool_ == True:
    try:
        numberOfTT = int(input('Enter number of timetables (upto 2): '))
        if numberOfTT<1 or numberOfTT>2:
            print('Number should be either 1 or 2. Please try again.')
        else:
            bool_ = False    
    except:    
        print(error_message)
        bool_ = True

bool_ = True

#number of periods
while bool_ == True:
    try:
        numberOfPeriods =  int(input("Enter number of periods: "))
        if numberOfPeriods<=0:
            print(error_message)
        else:
            bool_ = False

    except:    
        print(error_message)   

bool_ = True         

#start time of school
while bool_ == True:
    try:
        start = input('Enter start time of school(For example - 5:30 pm): ').lower()

        if len(start)>8 or len(start)<7:
            print(error_message)


        elif int(start[:-6]) >12:
            print(error_message)
    
        elif int(start[-5:-3]) >60:
            print(error_message)

        else:
            bool_ = False    
    except:
        print(error_message) 

bool_ = True

#end time of school
while bool_ == True:
    try:
        end = input ('Enter end time of school: ' ).lower()

        if len(end)>8 or len(end)<7:
            print(error_message)
  

        elif int(end[:-6]) >12:
            print(error_message)
 
        elif int(end[-5:-3]) >60:
            print(error_message)

        else:
            bool_ = False
    except:
        print(error_message)            

bool_ = True

l = []
P = []
Z = 1
while Z<numberOfPeriods+1:
    P.append(Z)
    Z+=1

#time after which  period will be  first break
while bool_ == True:
    try:
        b1start =  int(input(f'Enter time after which period will be  first break (Enter period from the list) - {P} : ')) +1
        if b1start-1<P[0] or b1start-1>P[-1]:
            print(error_message)
          
        else:    
            bool_ = False
    except:
        print(error_message)    

bool_ = True

index = b1start-2

#to remove period number before first break
for periods in (index,0):
    P.pop(periods)


#time after which period will be  second break 
while bool_ == True:
    try:
        b2start =  int(input(f'Enter time after which period will be  second break (Enter period from the list) - {P} : '))+1
        if b2start-1<P[0] or b2start-1>P[-1]:
            print(error_message)
          
        else:    
            bool_ = False
    except:
        print(error_message)    

bool_ = True

#duration of first break 
while bool_ == True:
    try:
        b1period = int(input(f'Enter duration of first break (in minutes): '))
        if b1period>500:
            print('Break is too long. Please input smaller value ')
        elif b1period<=0:
            print('Break cannot be less than or equal to 0. Please try again.')
        else:
            bool_ = False
    except:
        print(error_message)

bool_ = True  

#duration of second break 
while bool_ == True:
    try:
        b2period = int(input(f'Enter duration of second break (in minutes): '))
        if b2period>500:
            print('Break is too long. Please input smaller value ')
        elif b2period<=0:
            print('Break cannot be less than or equal to 0. Please try again.')
        else:
            bool_ = False
    except:
        print(error_message)

bool_ = True

#Enter number of subjects
while bool_ == True:
    try:
        numberOfSubjects = int(input("Enter number of subjects: "))
        if numberOfSubjects > numberOfPeriods:
            print('Number of subjects cannot be more than number of periods. Please try again.')
        elif numberOfSubjects<=0:
            print('Number of subjects cannot be less than or equal to zero. Please try again.')
        else:
            bool_ = False

    except:
        print(error_message)                

bool_ = True

#function used to create timetable
def table():
    global  C, B, y, _BREAK, period, s, e, hr, HR, DE, de,tab,l,l1,l2,l3,l4,l5,l6,K,l9,b,V,classname
    classname = input('Enter name of timetable: ')
    # a = int(input("Enter number of subjects: "))
    G1 = 0
    G2 = 0
    # numberOfPeriods=  int(input("Enter number of periods: "))
    # start = input('Enter start time of school(For example - 5:30 pm): ') 
    # end = input ('Enter end time of school: ' )

   
    period  = 0


    C = 0
    B = 0
    b1 = 0
    b2 = 0

    # code to convert time to am/pm after each period
    def am_pm(_hr,_de,_B1,_durationofperiod):
        global l 
        global C,B
        global b1,b2,y

        
        if start == '7:50 am':
            A = str(round(_hr + _de,2))
        else:  
            A = str(_hr + _de)
        if A.__contains__('.'):
            dot = A.index('.')
            f_string = ''

            B = int(A[:dot])
            if start=='7:50 am':
                C = round(int(A[dot+1:])*0.6)
            else:
                C = round(int(A[dot+1:])*6,2)
            

        if start.__contains__('am'):
            st = start[:-3]
        else:
            hour = str(int(start[:-6])+12)    
            st = hour+start[-6:-3]

        stic = datetime.strptime(st, "%H:%M")

        y = 0
        while y<numberOfPeriods+2:

            if start.__contains__('am'):
    
                if y ==  b1start-1 or y== b2start:
                        
                        if  y ==  b1start-1:


                        
                            st_ = str(stic+timedelta(minutes = b1period))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                        
                    
                    
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1
                           
                        elif y ==  b2start:
                        
                            st_ = str(stic+timedelta(minutes = b2period))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                        
                    
                    
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1

                            
        

                else:        
                        
                    
                            st_ = str(stic+timedelta(minutes = durationofperiod))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                            
                        
                        
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1


            elif start.__contains__('pm'):
    
                if y ==  b1start-1 or y== b2start:
                        
                        if  y ==  b1start-1:


                        
                            st_ = str(stic+timedelta(minutes = b1period))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                        
                    
                    
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1
                           
                        elif y ==  b2start:
                        
                            st_ = str(stic+timedelta(minutes = b2period))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                        
                    
                    
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1

                            
        

                else:        
                        
                    
                            st_ = str(stic+timedelta(minutes = durationofperiod))
                            kk2 = str(st_[-8:-3])
                            

                            kk1 = datetime.strptime(kk2, "%H:%M")
                    
                            f_string = f'{stic.strftime("%I:%M %p")} - {kk1.strftime("%I:%M %p")}'
                            stic = kk1

 
            l+=[f_string]
            y+=1                

                

    _BREAK = 0

    #sums up both the breaks
    def _break(_b1period,_b2period):
        global _BREAK
        _BREAK = _b1period+_b2period

    #converts am - pm to 24 hour time
    def times(strt,nd):
        kk = True
        global period
        global s
        global e, hr, HR, DE, de


        if strt.__contains__(':'):
            f = strt.index(':')   
            g = nd.index(':')     
            hr = int(strt[:f]) 
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
                e =round(HR + DE+ 12,2)

            elif end.__contains__('am'):
                e = round(HR + DE,2)       
                
    


        while kk == True:

            if strt.__contains__('pm') and nd.__contains__('am'):
                period = e - s + 12
                kk = False

            elif strt.__contains__('am') and nd.__contains__('pm'):
                period = e - s 
                kk = False

            elif strt.__contains__('pm') and nd.__contains__('pm'):
                if e>s:
                    period = e-s
                    kk = False

                else:
                    print("Timetable cannot be more than 24 hours. ")
                    kk = False
                    exit()   

            elif strt.__contains__('am') and nd.__contains__('am'):
                if e>s:
                    period = e-s-12 
                    kk = False
                else:
                    print("Timetable cannot be more than 24 hours. ")
                    kk = False
                    exit() 
                

    times(start,end)
    period1 = period
    s1 = s #starttime in 24 hour
    e1 =e #endtime in 24 hour
    hr1 = hr   #hour part of start time
    HR1 = HR   #hour part of end time
    DE1 = DE   # convert decimal to minutes in minute part of start time
    de1 = de   # convert decimal to minutes in minute part of end time





    #converting the break from minutes to hour
    B1PERIOD = b1period//60
    B2PERIOD = b2period//60

    #sums up both the breaks
    _break(b1period, b2period)

    
    rr  = (period1 - (_BREAK/60))/numberOfPeriods # duration of each period in hour
    ROUND = round(rr,2)
    p = str(ROUND)
    DOT = p.index('.')
    B1 = int(p[:DOT]) 
  
    durationofperiod = round(rr*60) 

  
    am_pm(hr1,de1,B1,durationofperiod)



    z = 0


    l2 = []
       
    F = 0
    l9 = []
    l10 = []
    count2 = 1

    if K==1:
        while z<numberOfSubjects:
            b = input("Enter subject: ")
            l2.append(b)
            l10.append(b)
            l9.append(b)
            z+=1
        print(l2)
        V = len(l2)
        while V<numberOfPeriods:
            l9.append(random.choice(l2))
            V+=1 

        while count2 < (len(l9)- len(l2)+1):
            l10.pop(-1)
            count2+=1


        list1 = list(dict.fromkeys(l9))
        print('list1 ',list1)
        print('l9 ',l9)

        if numberOfPeriods!= numberOfSubjects:
            for count1 in l10:
                list1.remove(count1)
                
                l2.append(random.choice(list1))
                list1.append(count1)

                print('aa',list1)
                print('bb',l2)

                if l2.count(count1)> (numberOfPeriods/numberOfSubjects):
                    list1.remove(count1)
                    l2.pop(-1)
                    l2.append(random.choice(list1))
                    list1.append(count1)
        
        print('aaa',list1)
        print('bbb',l2)


        
               
    print('\n')        
    

    def insertbreak(list1):

        list1.insert(b1start-1,'BREAK 1')
        list1.insert(b2start, 'BREAK 2')
        return list1    


    # def swapPositions(list, pos1, pos2):
        
    #         list[pos1], list[pos2] = list[pos2], list[pos1]
    #         return list 

    def listshuffler():
        l_ = random.sample(l2, len(l2))
        
        return  l_


    
    if K ==1:
        l1 = listshuffler()
        l3= listshuffler()
        l4= listshuffler()
        l5= listshuffler()
        l6 = listshuffler()


        l1 = insertbreak(l1)
        l3= insertbreak(l3)
        l4= insertbreak(l4)
        l5= insertbreak(l5)
        l6 = insertbreak(l2)


    A1 = l1
    A6 = l6
    A3 = l3
    A4 = l4
    A5 = l5

    def func(x):
        l = x
        f = []
       
        l.remove('BREAK 1')
        l.remove('BREAK 2')
        a1 = l
        # for numberOfPeriodsin l:
        #     a1.append(j)
        a1 = list(dict.fromkeys(a1))
  


        for i in l:
            a1.remove(i)

            f.append(random.choice(a1))
            a1.append(i)

            if f.count(i)> (numberOfPeriods/numberOfSubjects):
                a1.remove(i)
                f.pop(-1)
                f.append(random.choice(a1))
                a1.append(i)

      



        f.insert(b1start-1,'BREAK 1')
        f.insert(b2start,'BREAK 2')
          

        return f

    if K > 1:
        l1 = func(A1)
        l6 = func(A6)
        l3 = func(A3)
        l4 = func(A4)
        l5 = func(A5)


    info = {'': l, 'Monday': l6, 'Tuesday': l3, 'Wednesday': l4,'Thursday':l1,'Friday':l5 }

    print(classname)
    print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
    print('\n')
    l = []
    K+=1
    return tabulate(info, headers='keys', tablefmt='fancy_grid')

file_object  = open("timetable.txt", "a")
count = 0

while count < numberOfTT:
    T1 = table()
    f = file_object.write(classname+'\n'+'\n'+ T1+'\n'+'\n')
    count+=1
file_object.close()    
    