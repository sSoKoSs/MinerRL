import random


class mapper:
    def __init__(self, mmapy = 300, mmapx = 15):
        #map Initialization y = rows x = columns
        self.map = []
        self.mmapy = mmapy
        self.mmapx = mmapx

        for y in xrange(0,self.mmapy):
            self.map.append([])
            for x in xrange(0,self.mmapx):
                self.map[y].append('.')

        #map generation functions
        self.surface()
        self.caverns(230)
        self.border()

    def surface(self):
        #where to start making digable rocks "#"
        startY = 3

        for y in range(startY, self.mmapy):
            for x in range(0, self.mmapx):
                self.map[y][x] = '#'

    def caverns(self, holes = 0):
        #where to start making caverns "."
        startY = 4

        for h in xrange(holes):
            y = random.randrange(startY, self.mmapy - 2)
            x = random.randrange(2, self.mmapx - 2)
            self.map[y][x] = '.'
            self.map[y][x-1] = '.'
            self.map[y][x+1] = '.'
            self.map[y-1][x] = '.'
            self.map[y+1][x] = '.'

    def border(self):
        for x in xrange(0, self.mmapx):
            self.map[0][x] = '='

        for x in xrange(0, self.mmapx):
            self.map[self.mmapy-1][x] = '='

        for y in xrange(0, self.mmapy):
            self.map[y][0] = '='

        for y in xrange(0, self.mmapy):
            self.map[y][self.mmapx-1] = '='


#def hardRock():
