import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def GeneratePoints(N, r, x0=None, y0=None, plot=None):
    if x0 == None:
        x0 = np.random.rand()
    if y0 == None:
        y0 = np.random.rand()
        
    X, Y = [x0], [y0]
    for i in range(1, N):
        X.append((X[i-1] + r*(1-Y[i-1]))%1)
        Y.append((Y[i-1] + r*(1-X[i-1]))%1)
    if plot != False:
        plt.scatter(x=X,y=Y,s=15,)
        plt.title(str('Point cloud with r='+str(r)+'and N='+str(N)))
        plt.show()
    return X,Y

def animate_r(rmin, rmax, N, x0=None,y0=None,steps = None):
    if steps == None:
        steps = 1000.
    if x0==None:
        x0 = np.random.rand()
    if y0==None:
        y0 = np.random.rand()    
    fig , ax = plt.subplots()
    ax.plot(x0,y0,'ro',ms=4)
    points,= ax.plot([], [], 'bo',ms=1., alpha=0.5, )
    title = ax.text(0.5,.9, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                transform=ax.transAxes, ha="center")
    
    def init():
        ax.axis([-0.1,1.1,-0.1,1.1])
        string = 'Point Cloud with (x₀,y₀)=({:.3f},{:3f})'.format(x0,y0)+', {:.2f}≤ r≤{:.2f}'.format(rmin,rmax)
        ax.title.set_text(string)
        points.set_data([], [])
        return points,
    
    def animate(frame):
        X ,Y = GeneratePoints(N,frame,x0=x0,y0=y0,plot=False)
        X = np.array(X[1:])
        Y = np.array(Y[1:])
        title.set_text(u"r={:.5f}".format(frame))
        # update pieces of the animation
        points.set_data([X],[Y])
        return points,title,

    ani = FuncAnimation(fig, animate, frames = np.linspace(rmin,rmax,steps),
                                  interval=1, blit=True, init_func=init,repeat=True)
    plt.show()

def animate_X(r, N, x0=None,y0=None):
    if x0==None:
        x0 = np.random.rand()
    if y0==None:
        y0 = np.random.rand()    
    fig , ax = plt.subplots()
    ax.plot(x0,y0,'ro',ms=6)
    points,= ax.plot([], [], 'ro', ms=4)
    X,Y = GeneratePoints(N,r,x0,y0,plot=False)
    Xdata = []
    Ydata =[]
    
    def init():
        ax.axis([-0.1,1.1,-0.1,1.1])
        string = 'Animated Point Cloud with N={:.0f}'.format(N)
        ax.title.set_text(string)
        points.set_data([], [])
        return points,
    
    def animate(frame):
        Xdata.append(X[int(frame)])
        Ydata.append(Y[int(frame)])
        # update pieces of the animation
        points.set_data([Xdata],[Ydata])
        return points,

    ani = FuncAnimation(fig, animate, frames = np.array([i for i in range(N)]),
                                  interval=1, blit=True, init_func=init,repeat=True)
    plt.show()
    

def GenerateDataset():
    rVals = [2.5,3.5, 4.0, 4.1, 4.3]
    N=500

    X = []
    Y = []
    for r in rVals:
        points = GeneratePoints(N=N, r=r)
        X.append(points[0])
        Y.append(points[1])
        
    data = [list(zip(X[i],Y[i])) for i in range(len(rVals))]
    ind2r = dict()
    rMap = dict()
    labelMap = dict()
    for i in range(len(rVals)):
        ind2r[i]=rVals[i]
    for i in range(len(data)):
        rMap[rVals[i]] = []
        for pair in data[i]:
            labelMap[pair]=ind2r[i]
            rMap[rVals[i]].append(pair)

    Data = []
    for l in data:
        for pair in l:
            Data.append(list([[pair[0],pair[1]],labelMap[pair]]))
    Data = np.array(Data,dtype=object).reshape((len(Data),2))
    X = Data[:,0]
    Y = Data[:,1]
    df = pd.DataFrame(data=[X,Y]).transpose()
    df.columns=['X','r']
    df.head()
    df.to_csv('DynamicalSystem2D.csv',index=False)
    print('Dataset was saved to ',''.join(str(os.getcwd()+'\\DynamicalSystem2D.csv').split()))
    return df
