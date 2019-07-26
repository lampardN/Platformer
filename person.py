from personAnimation import *


class Person:
    def __init__(self, screenWidth, screenHeight):
        self.runStatus = {'left': False, 'right': False}
        self.turn = 'right'
        self.isJump = False
        self.inAir = True
<<<<<<< Updated upstream
        self.jumpCount = 10
=======
>>>>>>> Stashed changes
        self.neg = 1
        self.xPos = 0
        self.yPos = 0
        self.width = 58
        self.height = 58
        self.image =
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

    def onPlatform(self, objects):
        count = 0
        for obj in objects:
            if obj.top == self.rect.bottom:
                if not(obj.left <= self.rect.right and obj.right >= self.rect.left):
                    pass
                else:
                    count += 1
        if count == 0:
            return True
        else:
            self.inAir = False
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
            if key[py.K_SPACE] and not(self.inAir):
                self.isJump = True
        else:
                self.inAir = True
                self.jump()

        if self.onPlatform(objects):
            self.yPos += 1
        
        if key[py.K_UP]:
            self.yPos -= 2

            

        self.moveRect()

    def draw(self, display):



        display.blit(self.image, (self.xPos, self.yPos))
