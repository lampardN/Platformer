from sprites import *


class Person:
    def __init__(self, screenWidth, screenHeight):
        self.runCounter = 0
        self.runStatus = {'left': False, 'right': False}
        self.turn = 'right'
        self.idleCounter = 0
        self.isJump = False
        self.jumpCount = 10
        self.neg = 1
        self.xPos = 0
        self.yPos = 0
        self.width = 58
        self.height = 58
        self.image = idleR[0]
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width - 20
        self.moveRect()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def moveRect(self):
        if self.turn == 'left':
            self.rect.x = self.xPos
        else:
            self.rect.x = self.xPos + 20
        self.rect.y = self.yPos

    def onPlatform(self, obj):
        if obj.bottom == self.rect.bottom or obj.top == self.rect.bottom:
            if obj.left <= self.rect.right and obj.right >= self.rect.left:
                return True
            else:
                return False

    def jump(self):
        if self.jumpCount != 0:
            self.yPos -= 10
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10
        self.moveRect()

    def move(self, key, objects):

        if key[py.K_LEFT] and self.xPos > 0:
            self.xPos -= 5
            self.runStatus['left'] = True
            self.runStatus['right'] = False
            self.turn = 'left'

        elif key[py.K_RIGHT] and self.xPos < self.screenWidth - self.width:
            self.xPos += 5
            self.runStatus['right'] = True
            self.runStatus['left'] = False
            self.turn = 'right'

        else:
            self.runStatus['right'] = False
            self.runStatus['left'] = False

        if not(self.isJump):
            if key[py.K_SPACE]:
                self.isJump = True
        else:
            self.jump()


        if key[py.K_t]:
            print(self.rect.x, self.rect.y)

        for obj in objects:
            if not(self.onPlatform(obj)):
                self.yPos += 1

        self.moveRect()

    def draw(self, display):

        if self.runStatus['right']:
            self.image = runR[self.runCounter]

        elif self.runStatus['left']:
            self.image = runL[self.runCounter]

        else:

            if self.turn == 'right':
                self.image = idleR[self.idleCounter]
            else:
                self.image = idleL[self.idleCounter]

        if self.runStatus['right'] or self.runStatus['left']:
            self.runCounter += 1
            if self.runCounter >= run:
                self.runCounter = 0
        else:
            self.idleCounter += 1
            if self.idleCounter >= idle:
                self.idleCounter = 0

        display.blit(self.image, (self.xPos, self.yPos))
