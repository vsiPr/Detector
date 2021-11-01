import os
from subprocess import call
from index import *
call(["python", "index.py"])
print('aquit',Aquit)
if Aquit == 1:
    time.sleep(2)
    call(["python", "del.py"])
