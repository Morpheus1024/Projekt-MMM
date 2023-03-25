from pylab import *

class Układ:
    def __init__(self, wektor_wejścia):
        self.lista_IN = wektor_wejścia #[R, L, R2, C, U]
        self.R = self.lista_IN[0]
        self.L = self.lista_IN[1]
        self.R2 = self.lista_IN[2]
        self.C = self.lista_IN[3]
        self.U = self.lista_IN[4]
        self.biegun = None
        #self.P = None
        #self.Q = None
        self.Y_string=''
        self.transmitancja =' Y/U = -R/(R+R2+sRCR2)'
        
        #zerowe warunki początkowe

    def biegun(self):
        self.biegun = -(self.R+self.R2)/(self.R*self.R2*self.C)
        return self.biegun

    def moduł(self, w):
        self.P = -(self.R*(self.R + self.R2))/((self.R+self.R2)**2+(w*self.R*self.R2*self.C)**2)
        self.Q = (w*self.R*self.R2*self.C)/((self.R+self.R2)**2+(w*self.R*self.R2*self.C)**2)
        return sqrt(self.P**2+self.Q**2)

    def faza(self, w):
        self.P = -(self.R*(self.R + self.R2))/((self.R+self.R2)**2+(w*self.R*self.R2*self.C)**2)
        self.Q = (w*self.R*self.R2*self.C)/((self.R+self.R2)**2+(w*self.R*self.R2*self.C)**2)
        return arctan(self.Q/self.P)

    #def moduł(self,w):
     # return(self.P+j*self.Q) 


    
#def H(w):
    #wc = 4000*pi
    #return 1.0 / (1.0 + 1j * w / wc)
  

#f = logspace(1,5) # frequencies from 10**1 to 10**5
#plot(f, 20*log10(abs(H(2*pi*f)))); xscale('log')
print('siema') 



############################################################################


RLC = [1,1,1,1,1] #R, L, R2, C, U

uklad = Układ(RLC)

f = logspace(0,10)

plot(f, 20*log10(abs(uklad.moduł(2*pi*f)))); xscale('log')

plot(f, 20*log10(abs(uklad.faza(2*pi*f)))); xscale('log')
#plot(f, 20*log10(abs(uklad.wyjście_Q(2*pi*f)))); xscale('log')
#print('faza')
#plot (f, arg(uklad.wyjście_P(2*pi*f))); xscale('log')
