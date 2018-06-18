class Calculations:

    def __init__(self):
        pass

    def calculate_reynolds(self,ro,u,l,mi):

        return ro*u*l/mi

    def calculate_mach(self,u,c):

        return u/c

    def calculate_prandtl(self,ni,alpha):

        return ni/alpha

    def calculate_nusselt(self,h,l,k):

        return h*l/k

    def calculate_rayleigh(self,g,b,ni,alpha,T1,T2,x):

        return g*b*(T1-T2)*pow(x,3)/(ni*alpha)

    def calculatePeclet(self,l,u,alpha):

        return l*u/alpha

    def calculateGrashof(self,g,beta,Ts,Tinf,l,ni):

        return g*beta*(Ts-Tinf)*pow(l,3)/(pow(ni,2))

    def calculateFourier(self,alpha,t,l):

        return alpha*t/(pow(l,2))

    def calculateBiot(self,h,l,k):

        return l*h/k

    def calculateStokes(self,t,u,l):

        return t*u/l