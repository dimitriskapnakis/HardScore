#<-------------------------FOOTBALL RANKS------------------------------->#

teams=["olympiakos","paok","arhs","aek","panathinaikos","asteras tripolhs","volos","pas giannina","atromhtos","lamia","apollwn smyrnhs","ofh","panaitwlikos","larisa"]

points=[87,64,60,59,53,48,43,35,34,32,31,31,27,24]

goal_yper=[78,60,41,53,40,35,34,27,29,20,27,28,18,23]

goal_kata=[18,33,26,45,30,38,36,32,40,42,39,45,42,47]

#<-------------------------BASKERTBALL RANKS---------------------------->#
teams_basket=["panathinaikos","laurio","promitheas","aek","paok_thessalonikhs","peristeri","kolossos","iwnikos","arhs","hraklhs","larisa","mesologgi"]

points_basket=[42,39,38,36,35,33,30,30,29,29,28,27]

kalathia_entos=[10,10,10,8,8,6,7,5,5,4,5,4]

kalathia_ektos=[10,7,6,6,5,5,1,3,2,3,1,1]

#<-------------------------PROTH FUNCTION------------------------------->#
def team1(omada1):
    #omada1=raw_input("Type the name of the first team as it is in the upper text")
    for i in range(0,13):
     if omada1==teams[i]:
      team_chance1=(0.5*points[i])+(0.25*goal_yper[i])+(0.25*goal_kata[i])
      print("The chances of the first team to win are: ")
      print(team_chance1)
      
#<------------------------DEYTERH FUNCTION------------------------------>#  
    
def team2(omada2):
    #omada2=raw_input("Type the name of the second team as it is in the upper text")
    for i in range(0,13):
     if omada2==teams[i]:
      team_chance2=(0.5*points[i])+(0.25*goal_yper[i])+(0.25*goal_kata[i])
      print("The chances of the second team to win are: ")
      print(team_chance2)
      
#<-------------------------TRITH FUNCTION------------------------------->#

def basket1(omadaa1):
    for i in range(0,11):
     if omadaa1==teams_basket[i]:
      team_chance1_basket=(0.5*points_basket[i])+(0.15*kalathia_entos[i])+(0.35*kalathia_ektos[i])
      print("The chances of the first team to win are: ")
      print(team_chance1_basket)
      
#<------------------------TETARTH FUNCTION------------------------------>#

def basket2(omadaa2):
    for i in range(0,11):
     if omadaa2==teams_basket[i]:
      team_chance2_basket=(0.5*points_basket[i])+(0.25*kalathia_entos[i])+(0.25*kalathia_ektos[i])
      print("The chances of the second team to win are: ")
      print(team_chance2_basket)
      
#<-------------------------MAIN PROGRAMMA------------------------------->#

print("Welcome to Hardscore!!  Get ready to start your betting course!!")
shmaia=False
def shmaia():
    global shmaia
    shmaia=True
def login(onoma,kodikos):  
    success=False
    file=open("user_details.txt","r")
    for i in file:
        a,b = i.split (",")
        b=b.strip()
        if (a==onoma and b==kodikos):
            success=true
            break
        file.close()
        if (success) : 
            print("log in succesful")
        else:
                print("wrong username or password")




def register(onoma,kodikos):
    file.open("user_details.txt","a")
    file.write("/n"+onoma+","+kodikos)
    file.close()
    grant()
def access(option):
    global onoma
    if(option=="login"): 
        onoma=input("enter your name: ")
        kodikos=input("enter your password: ")
        login(onoma,kodikos)
    else:
         print("enter your name and password to register: ")
         onoma=input("enter your name:")
        kodikos=input("enter your password: ")
       register(onoma,kodikos)
def begin():

  global option
  print("Welcome to HardScore!")
  option=input("login or register (login,reg): ")
  if (option!="login" and option!="reg"):
      begin()
      begin()

      access(option)
if(shmaia):
    print("welcome to HardScore")
    print("### users details###")
    print("username:",onoma)

epilogh=raw_input("To start a new bet type START : ")
if epilogh=="START":
 print("Now it's time to choose a sport!!")
 print("In order to choose football type FOOTBALL")
 print("In order to choose basketball type BASKETBALL")
 choice=raw_input("I choose: ")
 d=0
 while d==0:
  if choice==("FOOTBALL"):
      d=d+1
  elif choice==("BASKETBALL"):
      d=d+1
  else:
      choice=raw_input("Please type again the right sport of your choice")
    
 if choice=="FOOTBALL":
  print("Nice you chose football!Now it is time to start the betting game.")
  print("These are all the teams you can choose:")
  for x in teams:
   print(x)
  print("Instructions: ") 
  print("You enter 2 teams and the team with the highest persentage is most likely to win!")
  omada1=raw_input("Type the name of the first team as it is in the upper text")
  a=0
  while a==0:
   for i in range(0,13):
     if omada1==teams[i]:
      a=a+1
      break
   else:
    omada1=raw_input("You gave wrong input!Try again please: ")
  

  team1(omada1)
  omada2=raw_input("Type the name of the first team as it is in the upper text")
  a=0
  while a==0:
   for i in range(0,13):
      if omada2==teams[i]:
       a=a+1
       break
   else:
    omada2=raw_input("You gave wrong input!Try again please: ")

  team2(omada2)
  
 elif choice=="BASKETBALL":
    print("Nice you chose basketball!Now it is time to start the betting game.")
    print("These are all the teams you can choose:")
    for x in teams_basket:
       print(x)
    print("Instructions: ")    
    print("You enter 2 teams and the team with the highest persentage is most likely to win!")
    omadaa1=raw_input("Type the name of the first team as it is in the upper text : ")
    b=0
    while b==0:
     for i in range(0,11):
       if omadaa1==teams_basket[i]:
         b=b+1
         break
       else:
        omadaa1=raw_input("You gave wrong input!Try again please: ")
  

     basket1(omadaa1)
    omadaa2=raw_input("Type the name of the second team as it is in the upper text : ")
    b=0
    while b==0:
     for i in range(0,11):
      if omadaa2==teams_basket[i]:
       b=b+1
       break
      else:
       omadaa2=raw_input("You gave wrong input!Try again please: ")

    basket2(omadaa2)
else:
 print("Bye!")

print("Thanks for using Hardscore!")

