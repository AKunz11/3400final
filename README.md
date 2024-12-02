# 3400final
The main hub where all of the files/code will sit for the final project

## Authors:
Alex Kunz, Morgan Lynch, Abhiyan Barailee


## Question:
In a binary system of a white dwarf (mostly C&O) and a red giant (carbon depletion core), where they are at a fixed distance that allows direct mass transfer, how does the binary interaction differ with different initial masses of the red giant? How does the binary interaction between the red giant and the white dwarf impact their evolution? 

## Hypothesis:
With our current knowledge of mass transfer in a binary system of a red giant and white dwarf, we expect a white dwarf to constantly accrete mass from the red giant until it reaches the Chandrasekhar’s limit of 1.4 solar mass, at which it’ll undergo explosive nucleosynthesis, resulting in a Type Ia supernova. The shockwave of the Type Ia supernova will blow off more mass from the red giant, resulting in a huge mass loss for the red giant overall. As a result, the  luminosity and radius of the red giant will decrease. Due to the loss of mass and reduction in radius, the remain mass of the red giant would be more gravitationally bound, thus we expect the  core to contracts and as a result, the temperature, density, and pressure should all go up. Depending on how much mass is lost, the red giant phase could either accelerate and the star will go supernova, or it will reach equilibrium again where it starts nucleosynthesis again in its core, slowing down the red giant phase since the lower mass start to have a longer lifespan. Additionally, the third possible outcome we expect is that it can shed its outer layer and become a white dwarf. Furthermore, we chose the metallicity to be mostly carbon and oxygen for the white dwarf and carbon-depleted core for the red giant, so the mass accreted by the white dwarf isn’t just hydrogen and helium. Otherwise, the mass would just accrete on the envelope (surface) of the star and continue until the temperature on the surface reaches hot enough to fuse hydrogen and helium, which will result in nova on the white dwarf, and the white dwarf would just remain as its original mass. Lastly, we expect the mass accretion rate to be larger in magnitude, the mass transfer to start earlier, and the red giant’s lifespan to be shorter when we increase the initial mass of the red giant. 

## Methods:
We will be using the MESA repository to simulate these events

## Helpful links:
https://cococubed.com/mesa_market/inlists.html (list of inlist examples)
https://billwolf.space/projects/massive_binaries_2021/#part1 (MESA summer school binary help)
## Variables list
The binary terminal output contains the following information

  - 'step' is the number of steps since the start of the run,
  - 'lg_dt' is log10 timestep in years,
  - 'age_yr' is the simulated years since the start run,
  - 'M1+M2' is the total mass of the system (Msun),
  - 'M1' is the mass of the primary (Msun)
  - 'M2' is the mass of the secondary (Msun)
  - 'separ' is the semi-major axis of the orbit (Rsun),
  -  'R1' is the radius of the primary (Rsun)
  -   R2' is the radius of the secondary (Rsun)
  - 'orb' is the orbital period (days),
  - 'P1' is the rotation period of star 1 (days, zero if not modeling rotation),
  - 'P2' is the rotation period of star 2 (days, zero if not modeling rotation),
  - 'e' orbital eccentricity,
  - 'dot_e' time derivative of e (1/yr),
  - 'Eorb' orbital energy G*M1*M2/2*separation (ergs),
  - 'M2/M1' mass ratio,
  - 'vorb1' orbital velocity of star 1 (km/s),
  - 'vorb2' orbital velocity of star 2 (km/s),
  - 'pm_i' index of star evolved as point mass, zero if both stars are modeled,
  - 'RL1' Roche lobe radius of star 1 (Rsun),
  - 'Rl2' Roche lobe radius of star 2 (Rsun),
  - 'donor_i' index of star taken as donor,
  - 'RL_gap1' (R1-Rl1)/Rl1,
  - 'RL_gap2' (R2-Rl2)/Rl2,
  - 'dot_Mmt', mass transfer rate (Msun/yr),
  - 'dot_M1', time derivative for the mass of star 1 (Msun/yr),
  - 'dot_M2', time derivative for the mass of star 2 (Msun/yr),
  - 'eff', mass transfer efficiency, computed as -dot_M2/dot_M1 (zero if dot_M1=0),
  - 'dot_Medd', Eddington accretion rate (Msun/yr),
  - 'L_acc', accretion luminosity when accreting to a point mass (ergs/s),
  - 'Jorb', orbital angular momentum (g*cm^2/s)
  - 'spin1', spin angular momentum of star 1 (g*cm^2/s),
  - 'spin2', spin angular momentum of star 2 (g*cm^2/s),
  - 'dot_J', time derivative of Jorb (g*cm^2/s^2),
  - 'dot_Jgr', time derivative of Jorb due to gravitational waves (g*cm^2/s^2),
  - 'dot_Jml', time derivative of Jorb due to mass loss (g*cm^2/s^2),
  - 'dot_Jmb', time derivative of Jorb due to magnetic braking (g*cm^2/s^2),
  - 'dot_Jls', time derivative of Jorb due to spin-orbit coupling (g*cm^2/s^2),
  - 'rlo_iters', number of iterations for implicit calculation of mass transfer,

 All this and more can be saved in binary_history.data during the run.
## Test Notes
- Both_stars1 used a period of 755 days (the period calculated using Roche Lobe radius)
- Both_stars2 used a period of 655 days

## Setup
- Copy MESA models into directory: `cp -r /opt/mesa/mesa-r23.05.1/binary/test_suite/evolve_both_stars ~/`
