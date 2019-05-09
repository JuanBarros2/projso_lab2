class FIFO:

  def __init__(self):
    self.pages = []

  def put(self, frameId):
    self.pages.append(frameId)

  def evict(self):
    return self.pages.pop(0)

  def clock(self):
    pass    

  def access(self, frameId, isWrite):
    pass
