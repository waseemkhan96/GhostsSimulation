import math

BLOCKSIZE = 3.5
HBLOCKSIZE = 1.75
BEPSILON = 0.01

UP = 0
DOWN = 2
RIGHT = 1
LEFT = 3

class Pos:
	def __init__(self, coord, o):
		self.orient = o
		if len(coord) == 2:
			self.x = coord[0]
			self.y = coord[1]
			self.updateInd()
		elif len(coord) == 4:
			self.x1 = coord[0]
			self.x2 = coord[1]
			self.y1 = coord[2]
			self.y2 = coord[3]
			self.updatePos()

	def updateInd(self):
		m = self.x / BLOCKSIZE;
		self.x1 = int(m)
		r = self.x - self.x1 * BLOCKSIZE;
		if abs(r - HBLOCKSIZE) < BEPSILON * 5.0:
			self.x2 = self.x1
		elif r >= HBLOCKSIZE:
			self.x2 = self.x1 + 1
		else:
			self.x2 = self.x1
			self.x1 -= 1
		m = self.y / BLOCKSIZE;
		self.y1 = int(m);
		r = self.y - self.y1 * BLOCKSIZE;
		if abs(r - HBLOCKSIZE) < BEPSILON * 5.0:
			self.y2 = self.y1
		elif r >= HBLOCKSIZE:
			self.y2 = self.y1 + 1
		else:
			self.y2 = self.y1;
			self.y1 -= 1
		self.y1 += 1
		self.y2 += 1
		self.x1 += 1
		self.x2 += 1

	def updatePos(self):
		self.x = ((self.x1 - 1.0) * 0.5 + (self.x2 - 1.0) * 0.5) * BLOCKSIZE + HBLOCKSIZE
		self.y = ((self.y1 - 1.0) * 0.5 + (self.y2 - 1.0) * 0.5) * BLOCKSIZE + HBLOCKSIZE

	def nPos(self): #get next position based on current position
		if self.orient == UP:
			y1n = self.y1 - 1
			y2n = self.y2 - 1
			return Pos((self.x1, self.x2, y1n, y2n), UP)
		elif self.orient == DOWN:
			y1n = self.y1 + 1
			y2n = self.y2 + 1
			return Pos((self.x1, self.x2, y1n, y2n), DOWN)
		elif self.orient == LEFT:
			x1n = self.x1 - 1
			x2n = self.x2 - 1
			return Pos((x1n, x2n, self.y1, self.y2), LEFT)
		elif self.orient == RIGHT:
			x1n = self.x1 + 1
			x2n = self.x2 + 1
			return Pos((x1n, x2n, self.y1, self.y2), RIGHT)
		else: return None

	def adjPos(self):
		rOrient = (self.orient + 1) % 4
		lOrient = (self.orient - 1) % 4
		lPos = Pos((self.x1, self.x2, self.y1, self.y2), lOrient).nPos()
		rPos = Pos((self.x1, self.x2, self.y1, self.y2), rOrient).nPos()
		fPos = Pos((self.x1, self.x2, self.y1, self.y2), self.orient).nPos()
		return lPos, fPos, rPos

	def dist(self, pos2):
		return math.sqrt(math.pow((self.x - pos2.x), 2) + math.pow((self.y - pos2.y),2))

	def equals(self, pos2):	
		if ((self.x1 == pos2.x2 or self.x2 == pos2.x1) and self.y1 == pos2.y1)  or ((self.y1 == pos2.y2 or self.y2 == pos2.y1) and self.x1 == pos2.x1):
			return True
		return False

	def printC(self):
		print self.x1, self.x2 
		print self.y1, self.y2
		self.printOrient()

	def printD(self):
		print self.x, self.y
		self.printOrient()

	def printOrient(self):
		if self.orient == UP: print "UP"
		elif self.orient == LEFT: print "LEFT"
		elif self.orient == RIGHT: print "RIGHT"
		else: print "DOWN"