
class Aging:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self):
    self.pages = []

  def put(self, frameId):
    """Allocates this frameId for some page"""
    self.pages.append([frameId, self.ALGORITHM_AGING_NBITS * '0', 0])

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    min_count = 256
    min_idx = -1
    for idx, page in enumerate(self.pages):
      aux = int(page[1], 2)
      if aux < min:
        min_count = aux
        min_idx = idx
    return self.pages.pop(min_idx)[0]

  def shift(self, page):
    bits = str(page[2])
    for i in range(1, 7):
      bits += page[1][i]
    page[1] = bits
    page[2] = 0

  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    for page in self.pages:
      self.shift(page)

  def access(self, frameId, isWrite):
    for page in self.pages:
      if page[0] == frameId: page[2] = 1
