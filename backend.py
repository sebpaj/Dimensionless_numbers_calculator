class Calculations(object):

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

    def calculate_rayleigh(self,g,b,T1,T2,x,ni,alpha):

        return g*b*(T1-T2)*pow(x,3)/(ni*alpha)

    def calculate_peclet(self,l,u,alpha):

        return l*u/alpha

    def calculate_grashof(self,g,beta,Ts,Tinf,l,ni):

        return g*beta*(Ts-Tinf)*pow(l,3)/(pow(ni,2))

    def calculate_fourier(self,alpha,t,l):

        return alpha*t/(pow(l,2))

    def calculate_biot(self,h,l,k):

        return h*l/k

    def calculate_stokes(self,t,u,l):

        return t*u/l