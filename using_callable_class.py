from EXAMPLES.memorychecker import MemoryChecker

mc = MemoryChecker()

print(mc())   # mc.check_memory()

x = [0] * 100000000

print(mc())

del x

print(mc()
      
      )