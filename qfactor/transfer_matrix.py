import numpy as np
from .models import Element

def kz_N(eps_N,wl,theta): 
    return (2*(np.pi/wl)**2*eps_N-kx_sub(wl,theta)**2)**0.5 

#kx sub is 2pi/lamba0 * sin ( incident angle)
def kx_sub(wl, theta):
    return 2*np.pi/wl * np.sin(theta)

def q_N(eps_N,wl,theta):
    return kz_N(eps_N,wl,theta)/eps_N  

def m11_N(d_N, eps_N,wl,theta):
    return np.cos(kz_N(eps_N,wl,theta)*d_N)

def m12_N(d_N,eps_N,wl,theta):
    return -1j/q_N(eps_N,wl,theta)*np.sin(kz_N(eps_N,wl,theta)*d_N)

def m21_N(d_N, eps_N,wl,theta):
    return -1.0j*q_N(eps_N,wl,theta)*np.sin(kz_N(eps_N,wl,theta)*d_N)

def m22_N(d_N, eps_N,wl,theta):
    return np.cos(kz_N(eps_N,wl,theta)*d_N)


def M_N(d_N, eps_N,wl,theta):
    return np.array([[m11_N(d_N,eps_N,wl,theta),m12_N(d_N,eps_N,wl,theta)],[m21_N(d_N,eps_N,wl,theta),m22_N(d_N,eps_N,wl,theta)]])


def kz_sub(eps_sub,wl,theta):
    return ((2.*np.pi/wl)**2*eps_sub-kx_sub(wl,theta)**2)**(1/2)

def q_sub(eps_sub,wl, theta):
    return kz_sub(eps_sub,wl,theta)/eps_sub

def kz_super(eps_super,wl,theta):
    return ((2*np.pi/wl)**2*eps_super-kx_sub(wl,theta)**2)**0.5

def q_super(eps_super,wl,theta):
    return kz_super(eps_super,wl,theta)/eps_super
    
# sub = first layer   to find the eps = (n^2+k^2)^1/2
def eps_p(omega,theta, E, eps_sub):
    Exy_real, Exy_im, Ez_real, Ez_im = E
    epsilon_effx = complex(Exy_real,Exy_im)
    epsilon_effz = complex(Ez_real,Ez_im)
    return epsilon_effx + (eps_sub*sind(theta)**2)*(1-epsilon_effx/epsilon_effz)

def calculate_M(layers, theta, params, E, interpolate):

    
    # big M = []

    # for w in wl:
    #     small_M = np.array([[1,1],[1,1]])
    #     for i in range(len(layers)):
    #         material, thickness = layers[i]
            
    

        

       


    #     epsp = eps_p(2*np.pi/wl*3.0*10**8, theta,E,eps_sub)
    #     m_n = M_N(thickness, epsp,wl,theta)
    #     M = np.matmul(m_n,M)

    print("reflection")
    # for w in wl:
    #     print(get_reflection(E, M,theta,wl, eps_super, eps_sub))
        
    
def get_reflection(M,theta,wl, eps_super, eps_sub):
    m11 = M[0,0]
    m12 = M[0,1]
    m21 = M[1,0]
    m22 = M[1,1]

    r = ((m11 + m12*q_super(eps_super,wl,theta))*q_sub(eps_sub,wl,theta) - (m21+m22*q_super(eps_super,wl,theta)))/((m11+m12*q_super(eps_super,wl,theta))*q_sub(eps_sub,wl,theta) + (m21*m22*q_super(eps_super,wl,theta)))
    return r

def get_transmission(M, theta, wl,eps_super,eps_sub):   
    m11 = M[0,0]
    m12 = M[0,1]
    m21 = M[1,0]
    m22 = M[1,1]

    t=2*q_sub(eps_sub,wl,theta)/((m11 + m12* q_super(eps_super,wl,theta))*q_sub(eps_sub,wl,theta) + (m21 + m22*q_super(eps_super,wl,theta)))


    return t 
   

def sind(theta):
    return np.sin(theta/np.pi*180)

