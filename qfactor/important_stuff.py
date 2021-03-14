import numpy as np
from .models import Element
import math
from .transfer_matrix_2 import magic

# {"essentials":[{"name":"initial_wavelength","value":"400"},{"name":"final_wavelength","value":"900"},{"name":"initial_polarisation","value":"0"},{"name":"final_polarisation","value":"40"},{"name":"polarisation","value":"TE"},{"name":"radius","value":"20"},{"name":"height","value":"200"},{"name":"distance","value":"60"},{"name":"number_of_layers","value":"3"}],"layers":[{"name":"material","value":"gold"},{"name":"thickness","value":""},{"name":"material","value":"gold"},{"name":"thickness","value":""},{"name":"material","value":"gold"},{"name":"thickness","value":""}]}
# Refer above to retrieve 


def process_data(jsondata):

    params, layers = process_json(jsondata)
    radius = float(params["radius"])
    distance = float(params["distance"])


    #calculating the filling fraction
    filling_fraction = (math.pi*float((params["radius"]))**2)/(float(params["distance"])**2) 
    
    (n, k, wl) = interpolate(Element.objects.get(name=params["nanorod_material"]),wl_init=params["initial_wavelength"],wl_fin=params["final_wavelength"])

    E = get_permitivity(n,k,radius, distance=distance,d_perm_real=float(params["dielectric_material_real"]),d_perm_im=float(params["dielectric_material_complex"]))

    Exy_real, Exy_im, Ez_real, Ez_im = E


    t_real, t_imag, r_real, r_imag = magic(E,n,k,wl,params,int(params["incident_angle"]),layers)

    print(t_real)


    return {'Data received from backend':  jsondata , 'x_data': wl, 'exy_real':Exy_real,'exy_im':Exy_im,'ez_real': Ez_real,'ez_im': Ez_im,"t_real": t_real,"t_imag": t_imag,"r_real":r_real,"r_imag":r_imag}

def get_permitivity(x,y,radius,distance,d_perm_real = 1,d_perm_im = 0):

    filling_fraction = (math.pi*float(radius)**2)/(float(distance)**2) 
    p=filling_fraction
    
    d_perm = complex(d_perm_real,d_perm_im)
    #calculating the refractive indicies
    real = []
    imaginary = []
    Ez_real = []
    Ez_im = []
    Exy_real = []
    Exy_im = []
    perm = []
    #creating the real and imaginary parts of the permitivity of the metal from the refractive index of the metal
    for i in range(len(x)):

        r_=(x[i]**2)-(y[i]**2)
        im_=(2*x[i]*y[i])
        real.append(r_)
        imaginary.append(im_)

    #calculating the permitivity of the nanorods
    for i in range (len(x)):
        k=complex(real[i],imaginary[i])
        perm.append(k)
        Ezr= (filling_fraction*real[i]) + ((1-filling_fraction)*d_perm_real)
        Ez_real.append(Ezr)
        oneplusp = (1+filling_fraction)
        oneminusp = (1-filling_fraction)
        Ezim = (filling_fraction*d_perm_im) + oneminusp*imaginary[i]
        Ez_im.append(Ezim)
        

        Exy= d_perm*(oneplusp*k + oneminusp*d_perm) / (oneplusp*d_perm + oneminusp*k)
            
        Exy_real.append(Exy.real) 
        Exy_im.append(Exy.imag) 

    return Exy_real, Exy_im, Ez_real, Ez_im



def process_json(data):
    i_list_1 = []
    i_list_2 = []
    for i in data["essentials"]:
        i_list_1.append(i["name"])
        i_list_2.append(i["value"])
    
    i_dict = dict(zip(i_list_1,i_list_2))

    j_list_1 = []
    j_list_2 = []

    for j in data["layers"]:
        if j["name"] == "material":
            j_list_1.append(j["value"])
        elif j["name"] == "thickness":
            j_list_2.append(j["value"])
    
    j = [j_list_1,j_list_2]

    j_list = np.array(j).T.tolist()

    

        
        

    return i_dict, j_list



def xl_calculation(params):
    #int data
    #radius
    #distance
    #matlab
    return 0

def interpolate(element,wl_init=400,wl_fin=900):
    data = []
    
    with open(element.file.path,"r") as Au:
        next(Au)
        for line in Au:
            row = line.split()
            row = [float(x) for x in row]
            data.append(row)
            #print(row)
    # print (data) # will show arrays of [[wl,n,k],every row ]

    wavelength = list(map(lambda x: x[0], data)) #list of wavelength i.e column 1
    n = list(map(lambda x: x[1], data)) #list of n i.e column 2
    k = list(map(lambda x: x[2], data)) #list of k i.e column 3
    #Now are each arrays

    #gives value of n for a given wavelength (input_wl) through interpolation (see below)
    #np.interp(input_wl,wl_array,n_array)

    x = []
    y = []
    z = []

    step = int((int(wl_fin) - int(wl_init)) / 50)

    for wl in range(int(wl_init),int(wl_fin),step):
        n_ = np.interp(wl,wavelength,n)
        k_ = np.interp(wl,wavelength,k)
        z_ = wl

        x.append(n_)
        y.append(k_)
        z.append(z_)

        # print (x_,y_,z_)
    return (x,y,z)

