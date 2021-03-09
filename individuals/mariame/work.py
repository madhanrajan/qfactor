print ('hello')
import numpy as np

data = []
Au = open ("/Users/mariamekarzazi/Desktop/Au.txt","r")
for line in Au:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    row = line.split()
    row = [float(x) for x in row]
    data.append(row)
        #print(row)
print (data) # will show arrays of [[wl,n,k],every row ]

wavelength = list(map(lambda x: x[0], data)) #list of wavelength i.e column 1
n = list(map(lambda x: x[1], data)) #list of n i.e column 2
k = list(map(lambda x: x[2], data)) #list of k i.e column 3
#Now are each arrays

#gives value of n for a given wavelength (input_wl) through interpolation (see below)
#np.interp(input_wl,wl_array,n_array)

for wl in range(210,550,10):
    print (np.interp(wl,wavelength,n),np.interp(wl,wavelength,k),wl)
