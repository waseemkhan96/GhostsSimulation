from pos import Pos
from grid import Map

Map = Map()

class Ghost:
	def __init__(self, _p):
		self.pos = _p

	def dec(self, tpos):
		nextPos = self.pos.nPos()
		val = Map.valPos(nextPos)
		while val < 3:
			self.pos.orient = (self.pos.orient + 1) % 4
			nextPos = self.pos.nPos()
			val = Map.valPos(nextPos)
		if val == 8:
			lPos, fPos, rPos = nextPos.adjPos()
			lDist = 1000000
			fDist = 1000000
			rDist = 1000000
			if Map.valPos(lPos) > 2:
				lDist = lPos.dist(tpos)
			if Map.valPos(rPos) > 2:
				rDist = rPos.dist(tpos)
			if Map.valPos(fPos) > 2:
				fDist = fPos.dist(tpos)
			minDist = min(lDist, rDist, fDist)
			self.pos = nextPos
			if minDist == lDist: 
				self.pos.orient = (self.pos.orient - 1) % 4
			elif minDist == rDist:
				self.pos.orient = (self.pos.orient + 1) % 4
		else:
			self.pos = nextPos