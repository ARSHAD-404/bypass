import os, platform

bit = platform.architecture()[0]
 
if bit == '64bit':
 
    from Premium64 import approval
 
    approval()
 
elif bit == '32bit':
 
    from Premium32 import approval
 
    approval()
