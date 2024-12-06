MESA Problems:
===================================================================================================================
Note that the inlists for the system are in the github <br>

- When running the binary system with the loaded models, it stops before mass transfer due to a retry limit for "eos evaluated at too low a density".

- Also see a lot of retry for "logT < hydro_mtx_min_allowed_logT", similar for logRho

- These are limiting the model to only 20,000 (or fewer) years after the stars are put in the binary, which is just before mass transfer seems to want to begin.

- Even when I try and run the mesa summer school example where the white dwarf model was found, I get a new error despite not changing anything: (make: *** No rule to make target '../src/run_star_extras.f90', needed by 'run_star_extras.o'.  Stop.) I interpreted this as there not being a file name "run_star_extras.f90" in the src directory but there definitely is, and I cannot even find "run_star_extras.o" if it exists.
