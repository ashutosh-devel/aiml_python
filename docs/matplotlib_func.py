#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:46:08 2023

@author: shweta
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as img


#x=[10,20,30,40]
#y=[20,30,40,50]
#plt.plot(x,y)
#plt.title('Simple plot')
#plt.ylabel("y-axis")
#plt.xlabel("x-axis")
#plt.show()



#x=np.arange(0,10,0.1)
#y=np.sin(x)
#y1=np.cos(x)
#plt.figure(figsize=(6, 6), dpi=144)
#plt.plot(x, y,'^', label='First Line',color="red")
#plt.plot(x, y1, label='Second line',color="blue")
#plt.xlabel('Plot number',fontsize=10)
#plt.ylabel('Data',fontsize=10)
#plt.title('Line graph',fontsize=30)#fontweight='bold')
#plt.legend(loc='best',fontsize=10)
#plt.grid()
#plt.show()
##plt.savefig("test.png")      #to save as png
##plt.savefig("test.pdf")      #to save as pdf



##y-axis value
#y=np.array([12,80,30,65,60,73,55,54])
##Function to plot histogram
#plt.hist(y, bins='auto')
#plt.xlabel('Marks',fontsize=10)
#plt.ylabel('Students',fontsize=10)
#plt.title('Histogram',fontsize=30)#fontweight='bold')
##Function to show the plot
#plt.show()




#x=np.arange(10)
#y=np.arange(10)
##plt.figure(figsize=(6, 6), dpi=144)
#plt.plot(x, y, label='First Line',color="red")
#plt.xlabel('X',fontsize=10)
#plt.ylabel('Y',fontsize=10)
#plt.xticks(range(0,10,1),fontsize=10)
#plt.yticks(range(0,10,2),fontsize=10)
#plt.xlim(0,10)
#plt.ylim(0,10)
#plt.title('LinePlot',fontsize=30)#fontweight='bold')




#section=['A','B','C','D']
#students=[23,17,19,25]
##Function to plot bar graph
#plt.bar(section, students)
##Function to show the plot
#plt.show()



#girls_grades=[83,90,71,40,56,31,62,88,100,75]
#boys_grades=[100,95,76,39,44,58,67,82,50,90]
#grades_range=np.arange(0,100,10)
#plt.scatter(grades_range, girls_grades)
#plt.scatter(grades_range, boys_grades)
#plt.xlabel('Grades range',fontsize=10)
#plt.ylabel('Grades scored',fontsize=10)
#plt.show()



#x=[25,30,45,10,50]
#labels=['A','B','C','D','E']
#plt.pie(x,labels=labels)
#plt.legend()
#plt.show()




#plt.subplot(1,2,1)
#plt.plot([1,2,3],[3,2,2],'o-')
#plt.title('I plot')
#plt.subplot(1,2,2)
#plt.plot([2,3,3],[3,2,2],'r^')
##plt.plot([2,3,3],[3,2,2],'.-')
#plt.title('II plot')
#plt.show()



##fig1 = plt.figure()
#testImage=img.imread('/netapp/scratch/shweta/test.png')
#plt.imshow(testImage)          
#lum_img=testImage[:,:,0]
#imgplot=plt.imshow(lum_img)
#imgplot.set_cmap('hot')        #'gist_rainbow','hot','gray','spectral'
#print(imgplot.shape)
##plt.colorbar()   #to add color scale
##plt.axis("off")     #to remove the axes
##plt.imsave('/netapp/scratch/shweta/test_out.png',testImage)
##print(testImage)
##print(testImage.shape)
#
##Psuedocolor is only relevant to single-channel, grayscale images


#fig = plt.figure()
#ax = fig.add_subplot(111)
#t = np.arange(0.0, 5.0, 0.01)
#s = np.cos(2*np.pi*t)
#line, = ax.plot(t, s, lw=2)
##ax.annotate("local maximum", xy=(2, 1), xytext=(3, 1.5),
##            arrowprops=dict(facecolor='gray', shrink=0.05))
##ax.annotate('local maximum', xy=(3, 1), xycoords='data',
##xytext=(0.8, 0.95), textcoords='axes fraction',
##arrowprops=dict(facecolor='gray', shrink=0.05, fc="yellow", ec="green"),
##horizontalalignment='right', verticalalignment='top',
##)
#ax.text(3,1,"Sine",bbox=dict(boxstyle="rarrow,pad=0.3",facecolor='gray', fc="yellow", ec="green"))
#ax.set_ylim(-2,2)
#plt.show()



from mpl_toolkits import mplot3d
fig = plt.figure()
ax=plt.axes(projection='3d')
z=np.linspace(0,1,100)
X=z*np.sin(25*z)
Y=z*np.cos(25*z)

#ax.plot3D(X,Y,z)
ax.scatter(X,Y,z)

#X=np.outer(np.linspace(-2,2,10),np.ones(10))
#Y=X.copy().T
#z=np.cos(X**2+Y**2)

ax.plot_surface(X,Y,z)
ax.set_title('surface')
plt.show()


















































