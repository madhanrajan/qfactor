
from .transfer_matrix import *
                         
def magic(E,n,k,wl,params,theta,layers):
    wv_val = [0]*int(params["number_of_layers"]) 
    L = [0]*int(params["number_of_layers"])



    epsil_real = []
    epsil_imag = []
    q=[0]*int(params["number_of_layers"]) 
    
    Exy_real, Exy_im, Ez_real, Ez_im = E

    n_ = np.array(n)
    k_ = np.array(k)


    for i in range(len(layers)):
        material, thickness = layers[i]
        if material== "metamaterial":
            epsil_real = np.array(Exy_real)# + np.array(Ez_real)
            epsil_imag = np.array(Exy_im)# + np.array(Ez_im)
            
            
        else:
            epsil_real = (n_**2)-(k_**2)
            epsil_imag = (2*n_*k_)
            
        L[i]=float(thickness)      

    
    
    big_M = []
    
    for i in range(len(wl)):
        w = wl[i]
        little_M = np.array([[1,0],[0,1]])

        for j in range(int(params["number_of_layers"])):
            material, thickness = layers[j] 


            #setting the epsil values for each layer  
            epsil = complex(epsil_real[j],epsil_imag[j])                                       
        
            # little_m = np.array([[1,0],[0,1]])
            # wv_val[j]=(2*np.pi/wl[i])*epsil-(2*np.pi)/wl[i]*np.sin(30/np.pi*180)                                                 #need to change the initial wv_val for non-normal incidence. We need phi probably
            # q[j] = wv_val[j]/epsil
            
            # M11 = np.cos(wv_val[j]*L[j]) #matrix elements of layers
            # M12 = complex(0, (1/(q[j]*(np.sin(wv_val[j]*L[j])))))
            # M21 = complex(0,(q[j]*np.sin(wv_val[j]*L[j])))
            # M22 = np.cos(wv_val[j]*L[j])
            # little_m = np.matmul([[M11,M12],[M21,M22]],little_m)
            M = M_N(float(thickness), epsil,w,theta)
            little_M = np.matmul(M,little_M)
             ### <- use thise instead of the one on top
            
        big_M.append(little_M)

    
    
    r_list = []
    big_M = np.array(big_M)
    t_list = []

    for w in range(len(wl)):
        wavelen = wl[w]
        eps_super = 1
        eps_sub = 1
        r_list.append(get_reflection(big_M[w],theta,wavelen, eps_super, eps_sub))
        t_list.append(get_transmission(big_M[w], theta, wavelen,eps_super,eps_sub))
    
    t_mag = [ np.sqrt(np.conjugate(x)*x) for x in t_list ]
    r_mag = [ np.sqrt(np.conjugate(x)*x) for x in r_list ]

    t_real = [x.real for x in t_list]
    t_imag = [x.imag for x in t_list]

    r_real = [x.real for x in r_list]
    r_imag = [x.imag for x in r_list]

    

    return t_real, t_imag, r_real, r_imag

