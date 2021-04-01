import numpy as np
from .models import Element


def kx_sub(wave, theta):

    return 2.0*(np.pi/wave)*sind(theta)


def kz_N(eps_N, wave, theta):

    return np.sqrt(np.square(2*np.pi/wave)*eps_N - np.square(kx_sub(wave, theta)))

# kx sub is 2pi/lamba0 * sin ( incident angle)


def q_N(eps_N, wave, theta):
    return 1.0*kz_N(eps_N, wave, theta)/eps_N


def m11_N(d_N, eps_N, wave, theta):
    print("epsn")
    print(eps_N)
    print("wave")
    print(wave)
    print("m11")
    print("dn")
    print(d_N)

    return 1.0*np.cos(kz_N(eps_N, wave, theta)*d_N)


def m12_N(d_N, eps_N, wave, theta):

    return complex(0, -1.0)/q_N(eps_N, wave, theta)*np.sin(kz_N(eps_N, wave, theta)*d_N)


def m21_N(d_N, eps_N, wave, theta):

    return complex(0, -1.0)*q_N(eps_N, wave, theta)*np.sin(kz_N(eps_N, wave, theta)*d_N)


def m22_N(d_N, eps_N, wave, theta):

    return 1.0*np.cos(kz_N(eps_N, wave, theta)*d_N)


def M_N(d_N, eps_N, wave, theta):
    return np.array([[m11_N(d_N, eps_N, wave, theta), m12_N(d_N, eps_N, wave, theta)], [m21_N(d_N, eps_N, wave, theta), m22_N(d_N, eps_N, wave, theta)]])


def kz_sub(eps_sub, wave, theta):
    return (((2.0*np.pi/wave)**2)*eps_sub-kx_sub(wave, theta)**2)**(0.5)


def q_sub(eps_sub, wave, theta):

    return 1.0*kz_sub(eps_sub, wave, theta)/eps_sub


def kz_super(eps_super, wave, theta):
    return ((2.0*np.pi/wave)**2*eps_super-kx_sub(wave, theta)**2)**0.5


def q_super(eps_super, wave, theta):

    return 1.0*kz_super(eps_super, wave, theta)/eps_super

# sub = first layer   to find the eps = (n^2+k^2)^1/2


def eps_p(Exy_r, Exy_im, Ez_r, Ez_im, theta, eps_sub):

    epsilon_effx = complex(Exy_r, Exy_im)
    epsilon_effz = complex(Ez_r, Ez_im)
    return epsilon_effx + (eps_sub*sind(theta)**2)*(1-epsilon_effx/epsilon_effz)


def get_reflection(M, theta, wave, eps_super, eps_sub):
    m11 = M[0, 0]
    m12 = M[0, 1]
    m21 = M[1, 0]
    m22 = M[1, 1]

    numerator = ((m11+(m12 * q_super(eps_super, wave, theta))) *
                 q_sub(eps_sub, wave, theta))-(m21+(m22*q_super(eps_super, wave, theta)))
    denominator = ((m11+(m12*q_super(eps_super, wave, theta)))*q_sub(eps_sub,
                                                                     wave, theta))+(m21+(m22*q_super(eps_super, wave, theta)))

    # r = ((m11 + m12*q_super(eps_super, wave,theta))*q_sub(eps_sub,wave,theta) - (m21+m22*q_super(eps_super,wave,theta))) / (m11 + m12)

    return numerator/denominator


def get_transmission(M, theta, wave, eps_super, eps_sub):
    m11 = M[0, 0]
    m12 = M[0, 1]
    m21 = M[1, 0]
    m22 = M[1, 1]

    t = 2.0*q_sub(eps_sub, wave, theta)/((m11 + m12 * q_super(eps_super, wave, theta))
                                         * q_sub(eps_sub, wave, theta) + (m21 + m22*q_super(eps_super, wave, theta)))

    return t


def sind(theta):

    return 1.0*np.sin(theta*np.pi/180)
