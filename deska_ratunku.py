from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
#import sympy


'''
todo
sprawdzić czym są w mag i
wyznaczanie punkt po punkcie kolejnych współrzędnych i zapisywanie ich do tablicy - tatarowy "mały dt"
pobudzenie prostokątem o skończonym czasie trwania
pobudzenie trójkątem
pobudzenie sygnałem harmonicznym
wyświetlanie wejścia i wyjścia jako przebieg czasowy
coś nowego jeszcze coś dopisuję




-- char. f. bodego


'''


class Układ:
   def __init__(self, lista_IN):
       #lista_IN = wektor_wejścia #[R, L, R2, C, U]
      
       self.R = lista_IN[0]
       self.L = lista_IN[1]
       self.R2 = lista_IN[2]
       self.C = lista_IN[3]
       self.U = lista_IN[4]
       self.biegun = None
       #self.P = None
       #self.Q = None
       self.Y_string=''
       self.transmitancja =' Y/U = -R/(R+R2+sRCR2)'


      
      
       #zerowe warunki początkowe


   def biegun(self):
       self.biegun = -(self.R+self.R2)/(self.R*self.R2*self.C)
       return self.biegun


   def bode(self):
       self.sys = signal.TransferFunction([self.R], [self.R*self.R2*self.C, self.R+self.R2])
       w, mag, phase = signal.bode(self.sys)
       plt.figure()
       plt.semilogx(w, mag)    # Bode magnitude plot
       plt.figure()
       plt.semilogx(w, phase)  # Bode phase plot
       plt.show()

   #def odp_harmoniczna(self, A, w):
       #IN = [A,w]

       #Y = A*R^2*sin(t*w) + A*R*R2*sin(t*w) - A*C*R^2*R2*w*cos(t*w))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2) + (A*C*R^2*R2*w*exp(-(t*(R + R2))/(C*R*R2)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
       #odp_harm (exp(-(t*(R + R2))/(C*R*R2))*(A*R^2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*R*R2*exp((t*(R + R2))/(C*R*R2))*sin(t*w) + A*C*R^2*R2*w - A*C*R^2*R2*w*exp((t*(R + R2))/(C*R*R2))*cos(t*w)))/(C^2*R^2*R2^2*w^2 + R^2 + 2*R*R2 + R2^2)
       #mnożenie w dzieninie s to to samo co splot w dziedzinie t - numpy.convolution
       #R = self.R
       #R2 = self.R2
       #C = self.C



    def sygnal_prostokatny(self, A, w, time):
        A=1
        w=1
        t = np.linspace(0,t,t*10, endpoint=True) #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
        #plt.plot(t, signal.square(w*t))
        #plt.figure()
        IN = signal.square(w*t)
        #plt.plot(t,IN)
        #plt.show()
        return IN

    def sygnal_trojkatny(self, A, w, time):
        A=1
        w=1
        t = np.linspace(0,t,t*10, endpoint=True)
    #plt.figure()
        IN = signal.sawtooth(w*t, 0,5) #0,5 daje trójkątny, 1 dawało by piłokształtny
        return IN

    def sygnal_harmoniczny(self, A, w, time):
        A=1
        w=1
        t = np.linspace(0,t,t*10, endpoint=True)
        plt.figure()
        IN = np.sin(t)



RLC = [10,1,15,20,1] #R, L, R2, C, U


uklad = Układ(RLC)


uklad.bode()


print("kompilacja udana")

###################################################


#sys = signal.TransferFunction([1], [1, 2]) 
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html

#https://realpython.com/python-matplotlib-guide/
#https://matplotlib.org/stable/gallery/widgets/buttons.html#sphx-glr-gallery-widgets-buttons-py
#https://www.youtube.com/watch?v=u5VCZBUNOcA
#https://matplotlib.org/stable/gallery/widgets/buttons.html buttony
#https://matplotlib.org/stable/gallery/widgets/textbox.html textbox
#https://matplotlib.org/stable/gallery/widgets/radio_buttons.html radio buttons
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html sygnał prostokątny






