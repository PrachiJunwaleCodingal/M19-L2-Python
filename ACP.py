#shutdown

import os
print("IMP Note- Do not write yes in class to shutdown")
sd = input("Shutdown comuter? (yes or no):")

if sd == 'no':
 exit()
else:
  os.system("shutdown /s /t 1")