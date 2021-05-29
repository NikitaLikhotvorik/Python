img1 = 0
img2=0
img3=0
img4=0
img5=0
img6=0
StartIndex = 0
Dver = 0
player = 0
biff=0
lst = []
NewLvL=1
def Ending():
    global img2,StartIndex
    img2= loadImage('Finale.jpg')
    image(img2,0,0,800,700)
    textSize(18)
    fill(255)
    rect(300,300,150,50)
    rect(300,650,150,50)
    fill(500,0,0)
    text('Try Again?',340,340)
    text('Good Job! You have completed the game!',5,285)
    text('Exit',350,675)
    fill(255)
    if mousePressed and mouseX>300 and  mouseX<450 and mouseY>300 and mouseY<350 and StartIndex==5:
        StartIndex=1
        op_list.charge_(StartIndex)
        player.x=400
        player.y=625
    if mousePressed and mouseX>300 and  mouseX<450 and mouseY>650 and mouseY<700:
        exit()
    
def MenuMoe():
    global img1, StartIndex
    img1 = loadImage('background.jpg');
    k = loadFont("JasmineUPCBoldItalic-45.vlw")
    textFont(k)
    image(img1,0,0,800,700)
    textSize(20)
    fill(255)
    rect(300,300,150,50)
    rect(300,650,150,50)
    fill(500,0,0)
    text('start',350,335)
    text('Labyrint',350,200)
    text('exit',350,670)
    fill(255)
    if mousePressed and mouseX>300 and  mouseX<450 and mouseY>300 and mouseY<350 and StartIndex==0:
        StartIndex=1
    if mousePressed and mouseX>300 and  mouseX<450 and mouseY>650 and mouseY<700:
        exit()
class ListPrepyatstvia:
    def __init__(self):
        self.charge_(1)
    def charge_(self,StartIndex):
        self.lst=[]
        if StartIndex == 1:
            Opasnost = Prepyatstvie(100,0,750,50)
            self.lst.append(Opasnost)
            self.append_(0,-350,685,50)
        if StartIndex == 2:
            self.append_(90,0,620,50)
            self.append_(0,-325,300,50)
            self.append_(90,-325,50,275)
            self.append_(620,-425,50,240)
            self.append_(620,-425,200,50)
            self.append_(315,-500,305,50)
        if StartIndex == 3:
            self.append_(0,-25,75,75)
            
            self.append_(60,0,75,75, random(1.4,2.5))
            self.append_(150,-50,75,75, random(1.4,2.2))
            self.append_(227,-75,75,75, random(1.4,2.5))
            self.append_(360,-100,75,75, random(1.4,2.5))
            self.append_(725,-10,75,75, random(1.4,2.5))
            self.append_(645,0,75,75, random(1.4,2.5))
            self.append_(575,-50,75,75, random(1.4,2.5))
            self.append_(200,-400,570,50,1.6)
            self.append_(0,-700,600,50,1.6)
            self.append_(0,-400,50,300,1.6)
        if StartIndex == 4:
            self.append_(0,0,160,50,2)
            self.append_(160,-150,160,50,2)
            self.append_(320,-400,160,50,2)
            self.append_(480,-150,160,50,2)
            self.append_(640,0,160,50,2)
            self.append_(0,-300,160,50,2)
            self.append_(160,-700,160,50,2)
            self.append_(320,-800,160,50,2)
            self.append_(480,-550,160,50,2)
            self.append_(640,-300,160,50,2)
            self.append_(0,-600,160,50,2)
            #self.append_(0,0,50,350)
            #self.append_(0, 425,50,275)
            #for item in range(4,12):
             #   op_list.fall_(x+1)
            #self.append_(750,0,50,350)
            #self.append_(750, 425,50,275)
            #for item in range(6,8):
                #lst[item].x-=diff
            #self.append_(350,0,100,50)
            
    def append_(self,x,y,dx,dy,speed = 1.35):
        Opasnost = Prepyatstvie(x,y,dx,dy , speed)
        self.lst.append(Opasnost)
    def fall_(self, diff):
        for item in self.lst:
            item.y += item.speed
        
    def draw_(self):
        for item in self.lst:
            item.draw_()
    def check_(self,player):
        check = 1
        for item in self.lst:
            check = item.check_(player.x+15 , player.y)*\
            item.check_(player.x+ 15 , player.y)*\
            item.check_(player.x + 55 , player.y)*\
            item.check_(player.x+ 55 , player.y+10)*\
            item.check_(player.x+ 75 , player.y+10)*\
            item.check_(player.x + 15 , player.y + 15)*\
            item.check_(player.x +75, player.y + 75)
            item.check_(player.x , player.y + 75)
            item.check_(player.x+75 , player.y + 35)
            item.check_(player.x , player.y + 35)
            if check == 0:
                return check
        return check
def NextOne(biff):
    global player, StartIndex
    if player.y<=0:
            StartIndex = biff
            player = Igrok(400,625)
            op_list.charge_(StartIndex)
class Igrok:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw_(self):
        image(img6,self.x,self.y,75,75)
def GameItself():
    image(img4,0,0)
#    background(0)
    player.draw_()

class Prepyatstvie:
    def __init__(self,x,y,dx,dy, speed = 1.35):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.speed = speed
    def draw_(self):
        rect(self.x,self.y,self.dx,self.dy)
        fill(100,100,100)
    def check_(self,x,y):
        if x >= self.x and x <= self.x+self.dx and y >= self.y and y <= self.y + self.dy:
            return 0
        else:
            return 1
def Dead():
    global StartIndex, img3
    img3 = loadImage('YouDed.jpg');
    image(img3,0,0,800,700)
    rect(375,575,150,50)
    textSize(20)
    fill(200,0,0)
    text('YOU DIED!', 400,400)
    text('try again?', 400,600)
    fill(255)
    if mousePressed and mouseX>375 and  mouseX<425 and mouseY>575 and mouseY<625:
        StartIndex = 1
        op_list.charge_(StartIndex)
        player.x=400
        player.y=625
def setup():
    global  player, op_list, img4,img5,img6
    player = Igrok(400,625)
    op_list = ListPrepyatstvia()
    img1 = loadImage('background.jpg');
    img4= loadImage('dungeon.png');
    img5= loadImage('brick.jpg');
    img6= loadImage('IgrokMoy.png');
    size(800,700)

def draw():
    global StartIndex, player, op_list,NewLvL
    background(0)

    if StartIndex==0: 
        MenuMoe()
    if StartIndex==10:
        Dead() 
    if StartIndex==1: 
        GameItself()
        op_list.draw_()
        op_list.fall_(1)
        NextOne(2)
    if StartIndex==2:
        GameItself() 
        op_list.draw_()
        op_list.fall_(1.5)
        NextOne(3)
    if StartIndex==3:
        GameItself()
        op_list.draw_()
        op_list.fall_(2)
        NextOne(4)
    if StartIndex==4:
        GameItself()
        op_list.draw_()
        op_list.fall_(2)
        NextOne(5)
    if StartIndex==5:
        Ending()

    check = op_list.check_(player)
    if check == 0:
        StartIndex = 10
        println(StartIndex)
    if keyPressed:
        if keyCode== LEFT and player.x >= 0:
            player.x = player.x -3
        if keyCode== RIGHT and player.x <= 725:
            player.x = player.x + 3
        if keyCode== DOWN and player.y <= 625:
            player.y = player.y + 3
        if keyCode== UP:
            player.y = player.y-3
