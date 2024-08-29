import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()



#step 1 create your virutal environment so pc" py -3 -m venv myvenv" for mac "python3 -m venv myvenv" myvenv could change so be any name
# not in parent folder just do it in normal folder
#step 2 Activate your virtual environemnt pc".myvenve\Scripts\activate" for mac "source myvenv/bin/activate"
#step 3 install 3rd party libraries "pip3 install matplotlib" matplotlib can also change name no matter what
#in bottom right make sure it is the right interpreter
#if you skip step 2 it will go into your root folder 

#source control vs version control
# version control is a project as a whole so a website could have a logo, documents, etc.... version control is project level
#source control is just the code that makes it work so how it runs 

#we use those to track our projects
#github we are clonning a repository 