from personAnimationSprites import *


class PersonAnimation:
    def __init__(self):
        self.animationCount = {'run': -1, 'idle': 0, 'jump': -1, 'fall': -1}
        self.runMax = 13
        self.idleMax = 15
        self.jumpMax = 3
        self.fallMax = 1

    def setImage(self, turn):
        for item in self.animationCount:
            if self.animationCount[item] != -1:
                count = self.animationCount[item]
                if turn == 'left':
                    if item == 'run':
                        return runL[count]
                    if item == 'idle':
                        return idleL[count]
                    if item == 'jump':
                        return jumpL[count]
                    if item == 'fall':
                        return fallL[count]
                else:
                    if item == 'run':
                        return runR[count]
                    if item == 'idle':
                        return idleR[count]
                    if item == 'jump':
                        return jumpR[count]
                    if item == 'fall':
                        return fallR[count]

    def jumpAnimation(self):
        self.reset('jump')
        if self.animationCount['jump'] < self.jumpMax:
            self.animationCount['jump'] += 1

    def idleAnimation(self):
        self.reset('idle')
        if self.animationCount['idle'] < self.idleMax:
            self.animationCount['idle'] += 1
        else:
            self.animationCount['idle'] = 0

    def fallAnimation(self):
        self.reset('fall')
        if self.animationCount['fall'] < self.fallMax:
            self.animationCount['fall'] += 1

    def runAnimation(self):
        self.reset('run')
        if self.animationCount['run'] < self.runMax:
            self.animationCount['run'] += 1
        else:
            self.animationCount['run'] = 0

    def reset(self, type):
        for item in self.animationCount:
            if item != type:
                self.animationCount[item] = -1


'''
test = PersonAnimation()
test.idleAnimation()
print(test.animationCount)
'''
