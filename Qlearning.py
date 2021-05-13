class Qnode():
  def __init__(self,x,y):
    self.point = [0,0,0,0]
    self.position = [x,y]

  def getBestWay(self):
    best = self.point[0]
    bestWay = 0
    for i in range(4):
      if self.point[i] > best:
        best = self.point[i]
        bestWay = i
    return bestWay

  def getQvalue(self):
    value = 0
    for num in self.point:
      value += num

  def allExplored(self):
    hasExplored = True
    for num in self.point:
      if num == 0:
        hasExplored = False
    return hasExplored
        
  def getNotExplore(self):
    notExplore = []
    for i in range(4):
      if self.point[i] == 0:
        notExplore.push(i)
    return notExplore


class Qtable ():
  def __init__(self,size):
    self.table = []
    self.route = []
    self.createQtable(size)

  def record(self,qnode,direction,nextQnode):
    qnode.point[direction] = nextQnode.getQvalue()*0.8

  def getQnode(self,position):
    return self.table[position[0]][position[1]]

  def createQtable(self,size):
    for i in range(size):
      row = []
      for j in range(size):
        qnode = Qnode(size,i,j)
        if i == 0 :
          qnode.point[0] = 0
        if j == 0 :
          qnode.point[3] = 0
        if i == size-1:
          qnode.point[2] = 0
        if j == size-1:
          qnode.point[1] = 0
        row.append(qnode)
      self.table.append(row)