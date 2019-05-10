
class Aging:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self):
    self.pages = {}

  def put(self, frameId):
    """Allocates this frameId for some page"""
    self.pages[frameId] = self.ALGORITHM_AGING_NBITS * '0'

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    min_count = 256
    for frameId in self.pages:
      page = self.pages[frameId]
      aux = int(page, 2)
      if aux < min_count:
        min_count = aux
        min_frameId = frameId
    self.pages.pop(min_frameId, None)
    return min_frameId

  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    for frameId in self.pages:
      self.pages[frameId] = '0' + self.pages[frameId][0:7]

  def access(self, frameId, isWrite):
      self.pages[frameId] = '1' + self.pages[frameId][0:7]
