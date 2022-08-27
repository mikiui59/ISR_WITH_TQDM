import shutil
import os

os.remove('/usr/local/lib/python3.7/dist-packages/ISR/models/imagemodel.py')
shutil.move('ISR_TQ/models/imagemodel.py','/usr/local/lib/python3.7/dist-packages/ISR/models/imagemodel.py')
