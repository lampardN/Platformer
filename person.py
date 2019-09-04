from personAnimation import *


class Person:
    def __init__(self, screenWidth, screenHeight):
        self.runStatus = {'run': False, 'stay': True}
        self.turn = 'right'
        self.isJump = False
        self.inAir = True
        self.neg = 1
        self.xPos = 0
        self.yPos = 0
        self.width = 58
        self.height = 58
        self.animation = PersonAnimation()
        self.image = self.animation.setImage(self.turn)
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
            self.isJump = False
            return False

    def jump(self):
        self.yPos -= 1

    def move(self, key, objects):

        if key[py.K_LEFT] and self.xPos > 0:
            self.xPos -= 5
            self.runStatus['run'] = True
            self.runStatus['stay'] = False
            self.turn = 'left'

        elif key[py.K_RIGHT] and self.xPos < self.screenWidth - self.width:
            self.xPos += 5
            self.runStatus['run'] = True
            self.runStatus['stay'] = False
            self.turn = 'right'

        else:
            self.runStatus['run'] = False
            self.runStatus['stay'] = True

        if not(self.isJump):
            if key[py.K_SPACE] and not(self.inAir):
                self.isJump = True
        else:
                self.inAir = True
                self.jump()

        if self.onPlatform(objects) and not(self.isJump):
            self.yPos += 1
        
        if key[py.K_UP]:
            self.yPos -= 2

        self.moveRect()

    def draw(self, display):

        if self.runStatus['stay'] and (not(self.isJump and not(self.inAir))):
            self.animation.idleAnimation()
        elif self.runStatus['run'] and (not(self.isJump and not(self.inAir))):
            self.animation.runAnimation()
        else:
            if self.isJump and self.inAir:
                self.animation.jumpAnimation()
            if not(self.isJump) and self.inAir:
                self.animation.fallAnimation()

        self.image = self.animation.setImage(self.turn)

        display.blit(self.image, (self.xPos, self.yPos))
