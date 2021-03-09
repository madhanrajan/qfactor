import numpy as np

def kz_N(eps_N,wl,theta): 
    return (2*(np.pi/wl)**2*eps_N-kx_sub(wl,theta)**2)**0.5

def q_N(eps_N,wl,theta):
    return kz_N(eps_N,wl,theta)/eps_N  

def m11_N(d_N, eps_N,wl,theta):
    return np.cos(kz_N(eps_N,wl,theta)*d_N)

def m12_N(d_N,eps_N,wl,theta):
    return -1j/q_N*(eps_N,wl,theta)*np.sin(kz_N(eps_N,wl,theta)*d_N)

def m21_N(d_N, eps_N,wl,theta):
    return -1.0j*q_N(eps_N,wl,theta)*np.sin(kz_N(eps_N,wl,theta)*d_N)

def m22_N(d_N, eps_N,wl,theta):
    return np.cos(kz_N(eps_N,wl,theta)*d_N)


def M_N(d_N, eps_N,wl,theta):
    return np.array([[m11_N(d_N,eps_N,wl,theta),m12_N(d_N,eps_N,wl,theta],[m21_N(d_N,eps_N,wl,theta),m22_N(d_N,eps_N,wl,theta)]])


def kz_sub(eps_sub,wl,theta):
    return ((2.*np.pi/wl)^2*eps_sub-kx_sub(wl,theta).^2).^(1/2)

def q_sub(eps_sub,wl, theta):
    return kz_sub*(eps_sub,wl,theta)/eps_sub

def kz_super(eps_super,wl,theta):
    return ((2*np.pi/wl)**2*eps_super-kx_sub(wl,theta)**2)**0.5

def q_super(eps_super,wl,theta):
    return kz_super(eps_super,wl,theta)/eps_super
    

def eps_p(omega,theta):
    return 