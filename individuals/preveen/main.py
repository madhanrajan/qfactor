#Defining E  and H of incident light as superposition of left and right
#travelling wave with ewave number ki and wavelength lam0
phi = [, , , ,] #list of angles used for incident light with array
Er =    
El = 
E = Er +El


#square root of epsilon/mu is the 1/Zc where Zc is the wave impedance of media
#Zc is also the ratio of the magnitude of E and H. Zc = E/H
#relation between E and H is given by H = (1/ikZc)(dE/dz) from maxwell equation
eps0 = 
mu0 =
Z0 = (math.sqrt(mu0/eps0))
H = (Z0 ** -1) *((Er - El)
                          
#Setting up initial conditions of incident light at surface
#of stacked dielectrics (z = 0). Outputs Matrix with initial E and H                          
z = 0
Wave = np.array([E,H])
print(Wave)


                         
#Transfer Matrix of layers
wv_val = [0]*int(params["number_of_layers"])  #list of wavenumber of layers
L = [0]*int(params["number_of_layers"]) #array of thickness of each layer
mu = [1]*int(params["number_of_layers"]) #list of magnetic permeabilities of ordered layers
epsil = [1]*int(params["number_of_layers"])#list of electric permittivities of layers
New_wave= []

for i,j in layers:
    
    L[i]=j
    
for material, thickness in layers:
    (n, k, wl) = interpolate(Element.objects.get(name=material),wl_init=params["initial_wavelength"],wl_fin=params["final_wavelength"])
    Exy_real, Exy_im, Ez_real, Ez_im = get_permitivity(n,k,radius, distance)
    for i in range(len(wl)):
        wl[i]
        n[i] #real part of the refractive index
        k[i] #complex part of the refactive index
        wv_val[0]=2*math.pi()/wl[i]
        refractive_index= complex(n[i],k[i])
        for i in range int(params["number_of_layers"]):
            wv[i+1] = refractive_index * wv[i]           # wavevector of media
            Zc = math.sqrt(mu[i]/eps[i])  #impedance of the particular media
            M11 = math.cos(wv[i+1]*L[i]) #matrix elements of layers
            M12 = complex(0, Zc * (math.sin(wv[i+1]*L[i]))
            M21 = complex(0,(Zc ** -1) *(math.sin(wv[i+1]*L[i]))
            M22 = math.cos(wv[i+1]*L[i])
            M = np.array([[M11,M12],[M21,M22]])
            New_Wave = np.dot(M,Wave) #matrix multiplication representing transformation of E and H in media
            New_wave.append(Wave)


New_wl,print(Wave)                       
Ei = (Er*(math.exp(*j*ki*z))) + (El*(math.exp(-j*ki*z)))



Hi = Zc *((Er*(math.exp(*j*ki*z))) - (El*(math.exp(-j*ki*z))))    