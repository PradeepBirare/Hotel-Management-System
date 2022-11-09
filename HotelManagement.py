import random
class hotelmanage:

    def __init__(self,id='',gt='',rt='',s=0,p=0,r=0,t=0,a=500,name='',address='',cindate='',coutdate='',rno=''):

        print ("\n\n*****WELCOME TO HOTEL SUNSHINE (PureVeg)*****\n")
        self.id=id
        self.gt=gt
        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
        '''for i in range(1,20):
            if self.rno>=20:
                print("your room is booked:")
            else:
                print("rooms are full") '''   
        
    def inputdata(self):
        self.id=int(input('\n Enter customer ID:'))
        self.name=str(input("\nEnter customer name:"))
        self.address=input("\nEnter customer address:")
        self.cindate=(input("\nEnter customer check in date:"))
        self.coutdate=(input("\nEnter customer checkout date:"))
        self.rno=[]
        for i in range(0,1):
         n = random.randint(1,30)
         self.rno.append(n)
        print("your room is booked") 
        print("Your room no is:",self.rno)
    
         
        

        
    def roomrent(self):#sel1353

        print ("We have the following rooms for you:-")

        print ("1.  Type A {Double with AC}---->rs 4000 PN\-")

        print ("2.  Type B {Single Bed with NON-AC}---->rs 1000 PN\-")

        print ("3.  Type C {Single bed with AC}---->rs 2000 PN\-")

        print ("4.  Type D {Double Bed with Non_AC}---->rs 3500 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have taken room Type A")

            self.s=4000*n

        elif (x==2):

            print ("you have taken room Type B")

            self.s=1000*n

        elif (x==3):

            print ("you have taken room Type C")

            self.s=2000*n

        elif (x==4):
            print ("you have taken room Type D")

            self.s=3500*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("BEVERAGES\n"
                "1.water--->Rs20","2.tea--->Rs15","3.Juice--->Rs30\n"
                "BREAKFAST\n"
                "4.Dosa--->Rs50","5.MasalaDosa--->Rs100\n",
                "6.Poha--->Rs30","7.Upma--->Rs40\n"
               "LUNCH\n"
               ,"8.Dalfry--->Rs80","9.Alookisabji--->120Rs\n",
               "10.BrownRice--->Rs100","11.MixSabji--->Rs120\n",
               "12.JeeraRice--->R70","13.Roti(4)--->40Rs\n"
               "DINNER\n"
               "14.PannerSabji--->Rs150\n",
               "15.CholeBhature--->Rs100","16.VegBiryani--->RS120\n",
               "17.VegFriedrice--->Rs160\n"
                "18.Exit"               )
        while (1):

            c=int(input("Enter your choice:"))

           
            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+15*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+30*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+100*d

            elif (c==6):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+30*d
            elif (c==7):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+40*d  
            elif (c==8):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+80*d
            elif (c==9):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+120*d   
            elif (c==10):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+100*d
            elif (c==11):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+120*d
            elif (c==12):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+70*d
            elif (c==13):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+40*d
            elif (c==14):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d 
            elif (c==15):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+100*d  
            elif (c==16):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+120*d  
            elif (c==17):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+160*d  
           
            elif (c==18):        
                    break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    def	laundrybill(self):
        print ("******LAUNDRY MENU*******")
        print ("1.Shorts----->Rs3","2.Trousers----->Rs4\n",
        "3.Shirt--->Rs5","4.Jeans---->Rs6\n",
        "5.Girlsuit--->Rs8","6.Womensclothes----->Rs10\n",
        "7.Exit")

        while (1):


            e=int(input("Enter your choice:"))
            

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                f=int(input("Enter the quantity:"))
                self.t=self.t+15*f
            
            elif(e==7):       
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print ("******GAME MENU*******")
        print (
        "1.Table tennis----->Rs60\n",
        "2.Bowling----->Rs80\n",
        "3.Snooker--->Rs70\n",
        "4.Video games---->Rs90\n",
        "5.Pool--->Rs50\n",
        "6.Exit")



        while (1):

            
            g=int(input("Enter your choice:"))
          

            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            
                
            

            elif(g==6):    

                break;

            else:

                print ("Invalid option")



        print ("Total Game Bill=Rs",self.p,"\n")

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r
        self.gt=self.rt+self.a

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.gt,"\n")

        

            

        

        

def main():

    a=hotelmanage()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Romms")

        print("3.Restaurant ")

        print("4.Laundry ")

        print("5. Game Parlor")

        print("6.Show total cost")

       

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

       

        if(b==7):    

            quit()



main()

