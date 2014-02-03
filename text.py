class AnimatedSprite:
    
    def __init__(self,fc,l):
        self.frameCount=fc
        self.location=l
        self.frames=[]
        self.currentFrame=0
        for i in range(self.frameCount):
            self.frames.append(pygame.image.load(self.location+'{:0>4}'.format(str(i+1))+'.jpg').convert())
            #self.frames.append(pygame.image.load(self.location+"000"+str((i+1))+".jpg").convert())

    def update(self):
        self.currentFrame=(self.currentFrame+1)%self.frameCount
        return self.frames[self.currentFrame]
    def current(self):
        return self.frames[self.currentFrame]

























import pygame, sys, time
from pygame.locals import *
pygame.mixer.pre_init(44100,-16,2, 512)
pygame.init()

WINDOWWIDTH=1000
WINDOWHEIGHT=1000
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)


BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

pygame.display.set_caption("Scrolling text test")

delay = 1
animDelay=3
textCounter = delay
animCounter=animDelay

basicFont=pygame.font.Font("pwinternational.ttf",10)

displayedText=basicFont.render('',True,BLACK)
textRect=displayedText.get_rect()


textRect.centerx=0
textRect.centery=windowSurface.get_rect().centery

windowSurface.fill(WHITE)



text = 'This is the sample text. Is it scrolling?'


mainClock=pygame.time.Clock()

mixer = pygame.mixer
mixer.set_num_channels(16)
mixer.music.load("113 Confrontation ~ Presto 2009.ogg")
#mixer.music.play(-1,0.0)


file = open("script\script.txt","r")


script=file.readlines()
for i in range(len(script)):
    script[i]=script[i][:-1]
#script=[text,"This is the second bit of text. If you can see this... yay!"]







maleBlip=mixer.Sound('sfx-blipmale.ogg')

pygame.display.update()

anim=AnimatedSprite(18, 'point_talk/phoenix-pointing(b)_frame_')
blinking=AnimatedSprite(1, 'point_blink/phoenix-pointing(a)_frame_')

for s in script:
    
    locInText=0
    output=""
    while locInText<len(s):

        breakFlag=False
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP or event.type==K_SPACE:
                maleBlip.play()
                output=s
                locInText=len(s)
                displayedText=basicFont.render(output,True,BLACK)
                windowSurface.blit(displayedText,textRect)
                pygame.display.update()
                breakFlag=True
                
        if breakFlag:
            break
            
        windowSurface.fill(WHITE)
        
        if animCounter>=animDelay:
            animCounter=-1
            windowSurface.blit(anim.update(),(0,0))
        else:
            windowSurface.blit(anim.current(),(0,0))
        
        if delay==textCounter:
            maleBlip.play(0,500)
            textCounter=-1
            output+=s[locInText]
            locInText=locInText+1
            displayedText=basicFont.render(output,True,BLACK)
            windowSurface.blit(displayedText,textRect)
        else:
            windowSurface.blit(displayedText, textRect)
            
        
        pygame.display.update()
        textCounter+=1
        animCounter+=1
        mainClock.tick(30)

    animCounter=animDelay
    advance=False
    while not advance:
        animCounter+=1
        if animCounter>=animDelay:
            windowSurface.fill(WHITE)
            windowSurface.blit(blinking.update(), (0,0))
            windowSurface.blit(displayedText, textRect)
            animCounter=-1
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP or event.type==K_SPACE:
                advance=True
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(30)
        
    
    pygame.display.update()
        #talk(text,delay)


#while True:
#
#            for event in pygame.event.get():
#                if event.type==QUIT:
#                    pygame.quit()
#                    sys.exit()
pygame.quit()
sys.exit()


def talk(text, delay):
    
    if text_counter==delay:
        text_counter=0
        #output+=

    #Need to also update sprite, independently of whether a character is displayed










    
    
