from get_rot_curve import GetRotCurve
from scipy import integrate, special
import numpy as np
import matplotlib.pyplot as plt

G = 4.302e-6 #kpc M_sol^-1 (km/s)^2 #6.67408e-11 # m^3 kg^-1 s^-2

def rho_integrand(x, kappa, Rb, r):

    return np.exp(kappa * (1.0 - (x / Rb)**(1.0/4))) / (x**(3.0/4) * np.sqrt(x**2 - r**2))

def rho(r, sigma_be, kappa, Rb):
    
    return (kappa * sigma_be / (4 * np.pi * Rb**(1.0/4))) * integrate.quad(rho_integrand, r, np.inf, args=(kappa, Rb, r))[0]

def Mb_integrand(r, sigma_be, kappa, Rb):

    return rho(r, sigma_be, kappa, Rb) * r**2

def Mb(R, sigma_be, kappa, Rb):
    #print(R)
    return 4* np.pi * integrate.quad(Mb_integrand, 0.0, R, args=(sigma_be, kappa, Rb))[0]

def Vb(R, sigma_be, kappa, Rb):

    return np.sqrt(G * Mb(R, sigma_be, kappa, Rb) / R)

def Vd(R, Rd, sigma_0):

    y = R / (2 * Rd)
    
    return np.sqrt(4 * np.pi * G * sigma_0 * Rd * y**2 * [special.i0(y) * special.k0(y) - special.i1(y) * special.k1(y)][0])

def Vh(R, Vinf, Rh):

    return Vinf * np.sqrt(1.0 - (Rh / R) * np.arctan(R / Rh))

sigma_be = 2.7e9#3.2e9
kappa = 7.6695
Rb = 0.5#0.5
sigma_0 = 8.6e8#8.44e8
Rd = 3.5#3.5
Vinf = 250#200
Rh = 16#12

#R_data, deltaR_data, V_data, deltaV_data = GetRotCurve()
#R = np.array(list(np.linspace(0.01, 2, 20)) + list(np.linspace(2,20,20)))

#Vbul, Vdisk, Vhalo = [], [], []
#for i in range(len(R)):
#    Vbul.append(Vb(R[i], sigma_be, kappa, Rb))
#    Vdisk.append(Vd(R[i], Rd, sigma_0))
#    Vhalo.append(Vh(R[i], Vinf, Rh))

#Vbul = np.array(Vbul)
#Vdisk = np.array(Vdisk)
#Vhalo = np.array(Vhalo)

#fig, ax = plt.subplots()

#ax.errorbar(R_data, V_data, yerr=deltaV_data, fmt='.', capsize=2)
#ax.plot(R, Vbul, '--', color='r')
#ax.plot(R, Vdisk, '--', color='b')
#ax.plot(R, np.sqrt(Vbul**2 + Vdisk**2), '-', color='orange')
#ax.plot(R, Vhalo, '--', color='g')
#ax.plot(R, np.sqrt(Vbul**2 + Vdisk**2 + Vhalo**2), '-', color='purple')

#ax.set_xlim([0, 20])

#plt.show()





