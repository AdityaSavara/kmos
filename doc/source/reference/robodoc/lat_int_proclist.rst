proclist/do_kmc_step
----------------------------------------

    Performs exactly one kMC step.
    *  first update clock
    *  then configuration sampling step
    *  last execute process

    ``none``

proclist/do_kmc_steps
""""""""""""""""""""""""""""""""""""""""""""""""""
    Performs ``n`` kMC step.
    If one has to run many steps without evaluation
    do_kmc_steps might perform a little better.
    * first update clock
    * then configuration sampling step
    * last execute process

    ``n`` : Number of steps to run

proclist/get_kmc_step
""""""""""""""""""""""""""""""""""""""""""""""""""
    Determines next step without executing it.

    ``none``

proclist/get_occupation
""""""""""""""""""""""""""""""""""""""""""""""""""
    Evaluate current lattice configuration and returns
    the normalized occupation as matrix. Different species
    run along the first axis and different sites run
    along the second.

    ``none``

proclist/init
""""""""""""""""""""""""""""""""""""""""""""""""""
     Allocates the system and initializes all sites in the given
     layer.

    * ``input_system_size`` number of unit cell per axis.
    * ``system_name`` identifier for reload file.
    * ``layer`` initial layer.
    * ``no_banner`` [optional] if True no copyright is issued.

proclist/initialize_state
""""""""""""""""""""""""""""""""""""""""""""""""""
    Initialize all sites and book-keeping array
    for the given layer.

    * ``layer`` integer representing layer
