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

## Setup
- Copy MESA models into directory: `cp -r /opt/mesa/mesa-r23.05.1/star/test_suite/12M_pre_ms_to_core_collapse ~/`
