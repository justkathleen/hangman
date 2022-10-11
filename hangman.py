# max word for this game is 10
import pygame
import wordgenerator

pygame.init()

#window display
win = pygame.display.set_mode((950,500))
def redrawGameWindow(ans, man):
    pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
    for but in layer1:
        but.draw()
    for alpha in layer2:
        alpha.draw()
    for bet in layer3:
        bet.draw()
    ans.drawword()
    man.draw()
    #the hangman position
    # pygame.draw.rect(win, (0,0,0), (620, 50, 300, 400))
    pygame.display.update() 



def getClick(ans, man):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and a.invisible == False:
        a.invisible = True
        if not(ans.evaluateGuess('a')):
            man.trials += 1
    if keys[pygame.K_b] and b.invisible == False:
        b.invisible = True
        if not(ans.evaluateGuess('b')):
            man.trials += 1
    if keys[pygame.K_c] and c.invisible == False:
        c.invisible = True
        if not(ans.evaluateGuess('c')):
            man.trials += 1
    if keys[pygame.K_d] and d.invisible == False:
        d.invisible = True
        if not(ans.evaluateGuess('d')):
            man.trials += 1
    if keys[pygame.K_e] and e.invisible == False:
        e.invisible = True
        if not(ans.evaluateGuess('e')):
            man.trials += 1
    if keys[pygame.K_f] and f.invisible == False:
        f.invisible = True
        if not(ans.evaluateGuess('f')):
            man.trials += 1
    if keys[pygame.K_g] and g.invisible == False:
        g.invisible = True
        if not(ans.evaluateGuess('g')):
            man.trials += 1
    if keys[pygame.K_h] and h.invisible == False:
        h.invisible = True
        if not(ans.evaluateGuess('h')):
            man.trials += 1
    if keys[pygame.K_i] and i.invisible == False:
        i.invisible = True
        if not(ans.evaluateGuess('i')):
            man.trials += 1
    if keys[pygame.K_j] and j.invisible == False:
        j.invisible = True
        if not(ans.evaluateGuess('j')):
            man.trials += 1
    if keys[pygame.K_k] and k.invisible == False:
        k.invisible = True
        if not(ans.evaluateGuess('k')):
            man.trials += 1
    if keys[pygame.K_l] and l.invisible == False:
        l.invisible = True
        if not(ans.evaluateGuess('l')):
            man.trials += 1
    if keys[pygame.K_m] and m.invisible == False:
        m.invisible = True
        if not(ans.evaluateGuess('m')):
            man.trials += 1
    if keys[pygame.K_n] and n.invisible == False:
        n.invisible = True
        if not(ans.evaluateGuess('n')):
            man.trials += 1
    if keys[pygame.K_o] and o.invisible == False:
        o.invisible = True
        if not(ans.evaluateGuess('o')):
            man.trials += 1
    if keys[pygame.K_p] and p.invisible == False:
        p.invisible = True
        if not(ans.evaluateGuess('p')):
            man.trials += 1
    if keys[pygame.K_q] and q.invisible == False:
        q.invisible = True
        if not(ans.evaluateGuess('q')):
            man.trials += 1
    if keys[pygame.K_r] and r.invisible == False:
        r.invisible = True
        if not(ans.evaluateGuess('r')):
            man.trials += 1
    if keys[pygame.K_s] and s.invisible == False:
        s.invisible = True
        if not(ans.evaluateGuess('s')):
            man.trials += 1
    if keys[pygame.K_t] and t.invisible == False:
        t.invisible = True
        if not(ans.evaluateGuess('t')):
            man.trials += 1
    if keys[pygame.K_u] and u.invisible == False:
        u.invisible = True
        if not(ans.evaluateGuess('u')):
            man.trials += 1
    if keys[pygame.K_v] and v.invisible == False:
        v.invisible = True
        if not(ans.evaluateGuess('v')):
            man.trials += 1
    if keys[pygame.K_w] and w.invisible == False:
        w.invisible = True
        if not(ans.evaluateGuess('w')):
            man.trials += 1
    if keys[pygame.K_x] and x.invisible == False:
        x.invisible = True
        if not(ans.evaluateGuess('x')):
            man.trials += 1
    if keys[pygame.K_y] and y.invisible == False:
        y.invisible = True
        if not(ans.evaluateGuess('y')):
            man.trials += 1
    if keys[pygame.K_z] and z.invisible == False:
        z.invisible = True
        if not(ans.evaluateGuess('z')):
            man.trials += 1
        



#letter button
class letter():
    def __init__(self, str, x, y, side):
        self.str = str
        self.x = x
        self.y = y
        self.side = side
        self.font = pygame.font.SysFont("comicsans", 30, True)
        self.text = self.font.render(str, 1, (255,255,255))
        self.invisible = False
    def draw(self):
        if self.invisible == False:
            pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.side, self.side))
            win.blit(self.text, (self.x +8,self.y))

class word():
    def __init__(self, string):
        self.string = string
        self.length = len(string) - 1
        self.array = list(string)
        self.notYetGuessed = list(set(list(self.string)))
        if '\n' in self.notYetGuessed:
            self.notYetGuessed.remove('\n')
        self.font = pygame.font.SysFont("comicsans", 30, True)


    def drawword(self):
        count = 0
        init_x = (600 - self.length * 50) / 2
        letter_x = init_x + 15
        start_letter = letter_x
        y = 200
        while count < self.length:
            if not(self.array[count] in self.notYetGuessed):
                toPrint = self.font.render(self.array[count], 1, (0,0,0))
                win.blit(toPrint, (letter_x, y - 45))
            pygame.draw.rect(win, (0,0,0), (init_x, y, 40, 10))
            count += 1
            init_x += 50
            letter_x += 50
    def evaluateGuess(self, char):
        if char in self.notYetGuessed:
            self.notYetGuessed.remove(char)
            return True
        else:
            return False
    def guessedCorrectly(self):
        if not self.notYetGuessed:
            return True
        else:
            return False

class hangman():
    def __init__(self):
        self.trials = 0
        self.maxchance = 9
        self.steps = [pygame.image.load('0.png'), pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('4.png'), pygame.image.load('5.png'),pygame.image.load('6.png'),pygame.image.load('7.png'),pygame.image.load('8.png') ]
    def draw(self):

        if self.trials < self.maxchance:
            win.blit(self.steps[self.trials], (620, 50))
        else:
            win.blit(self.steps[8], (620, 50))


class button():
	def __init__(self, image, x, y, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		win.blit(self.image, (self.rect.x, self.rect.y))

		return action






def playGame(answer):
    ans = word(answer)
    run = True
    man = hangman()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quitgame = True
        if ans.guessedCorrectly():
            correct = pygame.image.load('check.png')
            pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
            win.blit(correct,(320,150))
            pygame.display.update() 
            pygame.time.delay(1000)
            break
            #guessed correctly procedure
        getClick(ans, man)
        if man.trials == 8:
            print("dead")
            wrong = pygame.image.load('dead.png')
            scaledWrong = (300,300)
            wrong = pygame.transform.scale(wrong, scaledWrong)
            pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
            win.blit(wrong,(320,100))
            pygame.display.update() 
            pygame.time.delay(1000)
            pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
            displayanswer = "the answer is " + answer
            font = pygame.font.SysFont("comicsans", 30, True)
            text = font.render(displayanswer, 1, (0,0,0))
            win.blit(text,(300,200))
            pygame.display.update()
            pygame.time.delay(2000)
            break
        redrawGameWindow(ans,man)






def startNewGame():
    newgame = pygame.image.load('new.png')
    exit = pygame.image.load('exit.png')
    newgame = pygame.transform.scale(newgame, (200,100))
    exit = pygame.transform.scale(exit, (200,99))
    newGameButton = button(newgame, 200, 200,1)
    exitButton = button(exit, 500, 200,1)   
    loop = True
    start = False
    while loop:
        pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
        if newGameButton.draw():
            start = True
            return True
        if exitButton.draw():
            return False
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quitgame:
                loop = False
        pygame.display.update()






#main loop

playing = True
quitgame = False
newgame = pygame.image.load('new.png')
exit = pygame.image.load('exit.png')
newgame = pygame.transform.scale(newgame, (200,100))
exit = pygame.transform.scale(exit, (200,99))
newGameButton = button(newgame, 200, 200,1)
exitButton = button(exit, 500, 200,1)


continueGame = True
while continueGame:
    pygame.draw.rect(win, (51,255,255), (0, 0, 950, 500))
    pygame.display.update()
    anss = "invalid"
    while anss == "invalid":
        userinput = input("please select mode[dogbreed, country, sport]:")
        anss = wordgenerator.getCount(userinput)

    #create all the button for first layer
    q = letter("Q", 10, 300,50)
    w = letter("W", 70, 300,50)
    e = letter("E", 130, 300, 50)
    r = letter("R", 190,  300, 50)
    t = letter("T", 190 + 60, 300, 50)
    y = letter("Y", 250 + 60, 300, 50)
    u = letter("U", 310 + 60, 300, 50)
    i = letter("I", 370 + 60, 300, 50)
    o = letter("O", 430 + 60, 300, 50)
    p = letter("P", 490 + 60, 300, 50)
    layer1 = [q,w,e,r,t,y,u,i,o,p]

    # button layer 2
    a = letter("A", 35, 360, 50)
    s = letter("S", 35 + 60, 360, 50)
    d = letter("D", 95 + 60, 360, 50)
    f = letter("F", 155+60, 360, 50)
    g = letter("G", 215 + 60, 360, 50)
    h = letter("H", 275 + 60, 360, 50)
    j = letter("J", 335 + 60, 360, 50)
    k = letter("K", 395 + 60, 360, 50)
    l = letter("L", 455 + 60, 360, 50)
    layer2 = [a,s,d,f,g,h,j,k,l]

#button layer 3
    z = letter("Z", 60, 420, 50)
    x = letter("X", 60 + 60, 420, 50)
    c = letter("C", 120 + 60, 420, 50)
    v = letter("V", 180 + 60, 420, 50)
    b = letter("B", 240 + 60, 420, 50)
    n = letter("N", 300 + 60, 420, 50)
    m = letter("M", 360 + 60, 420, 50)
    layer3 = [z,x,c,v,b,n,m]
    playGame(anss)
    continueGame = startNewGame()








pygame.quit()