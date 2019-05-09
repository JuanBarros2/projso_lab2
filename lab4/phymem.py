# This is the only file you must implement

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you which

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class PhysicalMemory:
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self, algorithm, impl):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    if algorithm == "fifo":
      from fifo import FIFO
      self.strategy = FIFO()
    elif algorithm == "nru":
      from nru import NRU
      self.strategy = NRU()
    elif algorithm == "aging":
      from aging import Aging
      self.strategy = Aging()
    elif algorithm == "second-chance":
      from secondchance import SecondChance
      self.strategy = SecondChance()


  def put(self, frameId):
    return self.strategy.put()

  def evict(self):
    return self.strategy.evict()

  def clock(self):
    return self.strategy.clock()

  def access(self, frameId, isWrite):
    return self.strategy.access()
