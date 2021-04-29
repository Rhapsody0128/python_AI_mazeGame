import pygame as pg, random, math, time

#建立球體
class Ball(pg.sprite.Sprite):
    dx = 0         #x位移量
    dy = 0         #y位移量
    x = 0          #球x坐標
    y = 0          #球y坐標
    direction = 0  #球移動方向
    speed = 0      #球移動速度

    def __init__(self, sp, srx, sry, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        #繪製球體
        self.image = pg.Surface([radium*2, radium*2])  
        self.image.fill((255,255,255))
        pg.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)       #初始位置
        self.direction = random.randint(40,70)  #移動角度

 #球體移動 
    def update(self):         
        radian = math.radians(self.direction)    #角度轉為弳度
        self.dx = self.speed * math.cos(radian)  #球水平運動速度
        self.dy = -self.speed * math.sin(radian) #球垂直運動速度
        self.x += self.dx     #計算球新坐標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        #到達左右邊界
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
            self.bouncelr()
        elif(self.rect.top <= 10):  #到達上邊界
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):  #到達下邊界出界
            return True
        else:
            return False

    def bounceup(self):  #上邊界反彈
        self.direction = 360 - self.direction

    def bouncelr(self):  #左右邊界反彈
        self.direction = (180 - self.direction) % 360

#磚塊類別            
class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38, 13])  #磚塊長寬38x13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#板子類別
class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([99, 13])  #滑板圖片
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 30
        
#板子位置隨滑鼠移動 
    def update(self):  
        pos = pg.mouse.get_pos()  
        self.rect.x = pos[0]       #滑鼠x坐標
        #不要移出右邊界
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

#結束程式
def gameover(message): 
    global running
    #顯示訊息
    text = ffont.render(message, 1, (255,0,255))  
    screen.blit(text, (screen.get_width()/2-150,screen.get_height()/2-20))
    pg.display.update()  #更新畫面
    time.sleep(5)        #暫停5秒    
    running = False      #結束程式

pg.init()
score = 0  #得分
dfont = pg.font.SysFont("Arial", 20)    #下方訊息字體
ffont = pg.font.SysFont("SimHei", 32)   #結束程式訊息字體

#背景
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Sean's Brick Game")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pg.sprite.Group()  #建立全部角色群組
bricks = pg.sprite.Group()     #建立磚塊角色群組
ball = Ball(15, 300, 350, 10, (255,123,188)) #建立粉球
allsprite.add(ball)  #加入全部角色群組
pad = Pad()          #建立滑板球物件
allsprite.add(pad)   #加入全部角色群組

#建立磚塊
for row in range(0, 5):          #5列方塊
    for column in range(0, 15):  #每列15磚塊
        if row == 1 or row == 0: 
            brick = Brick((153,205,255), column * 40 + 1, row * 15 + 1)   #位置為40*15
        if row == 2: 
            brick = Brick((94,175,254), column * 40 + 1, row * 15 + 1)    
        if row == 3 or row == 4:  
            brick = Brick((52,153,207), column * 40 + 1, row * 15 + 1)  
        bricks.add(brick)     #加入磚塊角色群組
        allsprite.add(brick)  #加入全部角色群組
        
clock = pg.time.Clock()        
downmsg = "Press Left Click Button to start game!"  #起始訊息
playing = False  #開始時球不會移動
running = True

#運行的程式碼
while running:
    clock.tick(40)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
    if buttons[0]:            #按滑鼠左鍵後球可移動       
        playing = True
        
    #遊戲進行中
    if playing == True:  
        screen.blit(background, (0,0))  #清除繪圖視窗
        fail = ball.update()  #移動球體
        if fail:              #球出界
            gameover("You failed!See you next time~")
        pad.update()          #更新滑板位置
        #檢查球和磚塊碰撞
        hitbrick = pg.sprite.spritecollide(ball, bricks, True)  
        if len(hitbrick) > 0:  #球和磚塊發生碰撞
            score += len(hitbrick)  #計算分數
            ball.rect.y += 20  #球向下移
            ball.bounceup()    #球反彈
            if len(bricks) == 0:  #所有磚塊消失
                gameover("Congratulations!!")
        #檢查球和滑板碰撞
        hitpad = pg.sprite.collide_rect(ball, pad)  
        if hitpad:  #球和滑板發生碰撞
            ball.bounceup()  #球反彈
        allsprite.draw(screen)  #繪製所有角色
        downmsg = "Score: " + str(score)
    #繪製下方訊息    
    message = dfont.render(downmsg, 1, (255,0,255))
    screen.blit(message, (screen.get_width()/2-125,screen.get_height()-30))
    pg.display.update()
pg.quit()