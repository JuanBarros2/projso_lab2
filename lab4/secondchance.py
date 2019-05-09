
class SecondChance:
  def __init__(self):
    self.pages = []

  def put(self, frameId):
    self.pages.append([frameId, 0])

  def evict(self):
    i = 0
    length = len(self.pages)
    while (self.pages[i][1] != 0):
      self.put(self.pages.pop(i)[0])
      i = i + 1 if i != length else 0
    return self.pages.pop(i)[0]

  def clock(self):
    pass    

  def access(self, frameId, isWrite):
    frameIndex = -1
    for i in range(len(self.pages)):
      if self.pages[i][0] == frameId:
        frameIndex = i
        self.pages[i][1] = 1
      else:
        self.pages[i][1] = 0
    return self.pages[frameIndex]
