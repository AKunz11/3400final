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

   evolve_both_stars = .true.

!   pgbinary_flag = .true.

/ ! end of binary_job namelist

&binary_controls
         
   initial_period_in_days = 500d0

   fr = 0.01
   fr_limit = 1d-3

   limit_retention_by_mdot_edd = .false.
         
/ ! end of binary_controls namelist
```
### Inlist1
```
&star_job

      show_log_description_at_start = .false.
      load_saved_model = .true.
      load_model_filename = '7M_after_core_he_burn.mod'
      
      set_initial_age = .true.
      initial_age = 0 ! in years

      set_initial_model_number = .true.
      initial_model_number = 0

      pgstar_flag = .true.


/ ! end of star_job namelist

&eos

/ ! end of eos namelist

&kap

      Zbase = 0.02

/ ! end of kap namelist


&controls

      ! check for retries as part of test_suite
      ! you can/should delete this for use outside of test_suite
         max_number_retries = 80
         retry_limit = 100
         use_gold2_tolerances = .true.

      extra_terminal_output_file = 'log1' 
      log_directory = 'LOGS1'


      profile_interval = 50
      history_interval = 10
      terminal_interval = 1
      write_header_frequency = 10
      
      varcontrol_target = 1d-3
      

/ ! end of controls namelist


&pgstar
   read_extra_pgstar_inlist(1) = .true.
   extra_pgstar_inlist_name(1)= 'inlist_pgstar'

/ ! end of pgstar namelist

```
### Inlist 2
```
&star_job

      show_log_description_at_start = .false.
      load_saved_model = .true.
      load_model_filename = 'wd_0.8Msun.mod'
      
      set_initial_age = .true.
      initial_age = 0 ! in years

      set_initial_model_number = .true.
      initial_model_number = 0

      pgstar_flag = .true.


/ ! end of star_job namelist

&eos

/ ! end of eos namelist


&kap

      Zbase = 0.02

/ ! end of kap namelist


&controls

      ! check for retries as part of test_suite
      ! you can/should delete this for use outside of test_suite
         retry_limit = 100
         max_number_retries = 80
         use_gold2_tolerances = .true.

      extra_terminal_output_file = 'log2' 
      log_directory = 'LOGS2'


      profile_interval = 50
      history_interval = 10
      terminal_interval = 1
      write_header_frequency = 10
      
      varcontrol_target = 1d-3
      

/ ! end of controls namelist


&pgstar
   read_extra_pgstar_inlist(1) = .true.
   extra_pgstar_inlist_name(1)= 'inlist_pgstar'

/ ! end of pgstar namelist

```
## Run it!
```
./mk
./rn
```
