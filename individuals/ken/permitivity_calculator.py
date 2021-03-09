import matplotlib
import math 
#calculating the filling fraction


filling_fraction = (math.pi*float((params["radius"]))**2)/(float(params["distance"])**2) 
print("filling_fraction")
p=filling_fraction
the refractive indicies
real = []
ams[""float(]imaginary = []
params[""}])float()Ez_real = []
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
    Ezr= (filling_fraction*dielectric_material_realic_material_real) + ((1-filling_fraction)*real[i])
    Ez_real.append(Ezr)
    oneplusp = (1+filling_fraction)
    oneminusp = (1-filling_fraction)
    Ezim = (filling_fraction*dielectric_material_imaginary) + oneminusp*imaginary[i]
    Ez_im.append(Ezim)
    

    Exy= d_perm*((oneplusp*k) + oneminusp*d_perm) / (oneplusp*d_perm + oneminusp*k)
        
    Exy_real.append(Exy.real) 
    Exy_im.append(Exy.imag) 


   


   


   
