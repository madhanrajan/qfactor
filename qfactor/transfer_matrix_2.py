
from .transfer_matrix import *


def magic(E, wl, interpolate, params, theta, layers):
    L = [0]*int(params["number_of_layers"])

    epsil_real_list = []
    epsil_imag_list = []

    Exy_real, Exy_im, Ez_real, Ez_im = E

    eps_p_list_real = []
    eps_p_list_im = []

    for i in range(len(Exy_real)):
        eps_p_list_real.append(
            eps_p(Exy_real[i], Exy_im[i], Ez_real[i], Ez_im[i], theta, 1).real)
        eps_p_list_im.append(
            eps_p(Exy_real[i], Exy_im[i], Ez_real[i], Ez_im[i], theta, 1).imag)

    for i in range(len(layers)):
        material, thickness = layers[i]

        if material == "Metamaterial":

            epsil_real = np.array(eps_p_list_real)
            epsil_imag = np.array(eps_p_list_im)

        else:
            (n, k, wl) = interpolate(Element.objects.get(
                name=material), wl_init=params["initial_wavelength"], wl_fin=params["final_wavelength"])
            n_ = np.array(n)
            k_ = np.array(k)
            epsil_real = (n_**2)-(k_**2)
            epsil_imag = (2*n_*k_)
        epsil_real_list.append(epsil_real)
        epsil_imag_list.append(epsil_imag)

        L[i] = float(thickness)

    big_M = []

    for i in range(len(wl)):
        w = wl[i]
        little_M = np.array([[1, 0], [0, 1]])

        for j in range(int(params["number_of_layers"])):
            material, thickness = layers[j]

            # setting the epsil values for each layer
            epsil = complex(epsil_real_list[j][i], epsil_imag_list[j][i])

            # little_m = np.array([[1,0],[0,1]])
            # wv_val[j]=(2*np.pi/wl[i])*epsil-(2*np.pi)/wl[i]*np.sin(30/np.pi*180)                                                 #need to change the initial wv_val for non-normal incidence. We need phi probably
            # q[j] = wv_val[j]/epsil

            # M11 = np.cos(wv_val[j]*L[j]) #matrix elements of layers
            # M12 = complex(0, (1/(q[j]*(np.sin(wv_val[j]*L[j])))))
            # M21 = complex(0,(q[j]*np.sin(wv_val[j]*L[j])))
            # M22 = np.cos(wv_val[j]*L[j])
            # little_m = np.matmul([[M11,M12],[M21,M22]],little_m)
            M = M_N(float(thickness), epsil, w, theta)
            little_M = np.matmul(M, little_M)
            # <- use thise instead of the one on top

        big_M.append(little_M)

    r_list = []
    big_M = np.array(big_M)
    t_list = []

    for w in range(len(wl)):
        wavelen = wl[w]
        eps_super = 1
        eps_sub = 1
        r_list.append(get_reflection(
            big_M[w], theta, wavelen, eps_super, eps_sub))
        t_list.append(get_transmission(
            big_M[w], theta, wavelen, eps_super, eps_sub))

    t_mag = [np.conjugate(x)*x for x in t_list]
    r_mag = [np.conjugate(x)*x for x in r_list]

    t_real = [x.real for x in t_mag]
    # t_imag = [x.imag for x in t_mag]

    r_real = [x.real for x in r_mag]
    # r_imag = [x.imag for x in r_mag]

    # r_real = 1 - np.array(r_real)
    # r_imag = 1 - np.array(r_imag)

    return t_real, [], r_real, []
