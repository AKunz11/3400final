# How to get your binary directory!! :D
## Step 1
Copy that thing over: <br>
`cp -r /opt/mesa/mesa-r23.05.1/binary/work ~/your_path`
## Step 2
Configure your inlists!! <br>
### Inlist_project
```
&binary_job

   inlist_names(1) = 'inlist1' 
   inlist_names(2) = 'inlist2'
   
   evolve_both_stars = .true.                 ! Enable binary evolution    

/ ! end of binary_job namelist

&binary_controls
         
   roche_lobe_overflow_scheme = 'implicit'   ! Handle RLOF (mass transfer)
   initial_period_in_days = 2d0
   initial_eccentricity = 0.0                ! Initial orbital eccentricity

   !transfer efficiency controls
   limit_retention_by_mdot_edd = .true.

   max_tries_to_achieve = 20
         
/ ! end of binary_controls namelist 
```
### Inlist1
```
! inlist_test_rlo



&star_job

      load_saved_model = .true.
      saved_model_name = 'HeStar_0.4Msun.mod' ! OR whatver star 1 model is named, this is an example
      
      set_initial_age = .true.
      initial_age = 0 ! in years

      set_initial_model_number = .true.
      initial_model_number = 0

      pgstar_flag = .true.

/ ! end of star_job namelist

&eos
  ! eos options
  ! see eos/defaults/eos.defaults

/ ! end of eos namelist


&kap
  ! kap options
  ! see kap/defaults/kap.defaults
  use_Type2_opacities = .true.
  Zbase = 0.02

/ ! end of kap namelist


&controls

      extra_terminal_output_file = 'log1' 
      log_directory = 'LOGS1'

      profile_interval = 50
      history_interval = 10
      terminal_interval = 1
      write_header_frequency = 10
      
      max_age = 1d10
      relax_initial_tau_factor = 1.0            ! Optional: Relax the starting model

/ ! end of controls namelist


&pgstar


      History_Panels1_win_flag = .true.
      History_Panels1_win_width = 5
      History_Panels1_win_aspect_ratio = 1.0 ! aspect_ratio = height/width
      
      History_Panels1_title = 'Orbital evolution'
      History_Panels1_num_panels = 2
      
      History_Panels1_yaxis_name(1) = 'period_days'
      History_Panels1_other_yaxis_name(1) = 'lg_mstar_dot_1' 
      History_Panels1_yaxis_name(2) = 'Jdot' 
      History_Panels1_other_yaxis_name(2) = 'binary_separation' 


      History_Track1_win_flag = .true.
      History_Track1_title = 'P vs t'
      History_Track1_xname = 'age'
      History_Track1_yname = 'period_days'
      History_Track1_xaxis_label = 't (years)'
      History_Track1_yaxis_label = 'P (days)'
      History_Track1_log_xaxis = .false. ! show log10 of abs value
      History_Track1_log_yaxis = .true. ! show log10 of abs value
      History_Track1_reverse_xaxis = .false.
      
/ ! end of pgstar namelist
```
### Inlist 2
```

! inlist_test_rlo



&star_job

      load_saved_model = .true.
      saved_model_name = 'HeStar_0.4Msun.mod' ! OR whatver star 2 model is named, this is an example
      
      set_initial_age = .true.
      initial_age = 0 ! in years

      set_initial_model_number = .true.
      initial_model_number = 0

      pgstar_flag = .true.


/ ! end of star_job namelist

&eos
  ! eos options
  ! see eos/defaults/eos.defaults

/ ! end of eos namelist


&kap
  ! kap options
  ! see kap/defaults/kap.defaults
  use_Type2_opacities = .true.
  Zbase = 0.02

/ ! end of kap namelist

&controls

      extra_terminal_output_file = 'log2' 
      log_directory = 'LOGS2'

      profile_interval = 50
      history_interval = 10
      terminal_interval = 1
      write_header_frequency = 10
      
      max_age = 1d10
      relax_initial_tau_factor = 1.0            ! Optional: Relax the starting model

/ ! end of controls namelist


&pgstar
         


/ ! end of pgstar namelist
```
## Run it!
```
./mk
./rn
```
