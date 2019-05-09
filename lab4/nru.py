
class NRU:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self):
    self.pages = []


  def put(self, frameId):
    """Allocates this frameId for some page"""
    self.pages.append([frameId, 1, 0])

  def get_class(self, page):
    if page[1] == 0:
      if page[2] == 0: return 0
      if page[2] == 1: return 1
    if page[1] == 1:
      if page[2] == 0: return 2
      if page[2] == 1: return 3

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    min_page_idx = 0
    min_class = self.get_class(self.pages[0])
    for idx, page in enumerate(self.pages):
      aux = self.get_class(page)
      if aux < min_class:
        min_page_idx = idx
        min_class = aux
    return self.pages.pop(min_page_idx)[0]

  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    for page in self.pages:
      if page[1] == 1:
        page[1] =  0 

  def access(self, frameId, isWrite):
    referred_page = []
    for page in self.pages:
      if page[0] == frameId:
        referred_page = page
    if isWrite: 
      referred_page[2] = 1
    referred_page[1] = 1
