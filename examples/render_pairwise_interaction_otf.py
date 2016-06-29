#!/usr/bin/env python

from kmos.types import *
from itertools import product
import numpy as np

pt = Project()
pt.set_meta(author='Juan M. Lorenzi',
            email='jmlorenzi@gmail.com',
            model_name='dummy_pairwise_interaction_otf',
            model_dimension=2)

layer = pt.add_layer(name='simplecubic_2d')
layer.add_site(name='a')
pt.add_species(name='empty', color='#ffffff')
pt.add_species(name='O', color='#ff0000',
               representation="Atoms('O')",)
pt.add_species(name='CO', color='#000000',
               representation="Atoms('CO',[[0,0,0],[0,0,1.2]])",
               tags='carbon')
pt.add_parameter(name='E_CO', value=-1, adjustable=True, min=-2, max=0)
pt.add_parameter(name='E_CO_nn', value=.2, adjustable=True, min=-1, max=1)
pt.add_parameter(name='p_COgas', value=.2, adjustable=True, scale='log', min=1e-13, max=1e3)
pt.add_parameter(name='T', value=600, adjustable=True, min=300, max=1500)
pt.add_parameter(name='A', value='(3*angstrom)**2')

center = pt.lattice.generate_coord('a')

A = 1.  # lattice const.


pt.lattice.cell = np.diag([A, A, 10])

# Adsorption process
pt.add_process(name='CO_adsorption',
               conditions=[Condition(species='empty', coord=center)],
               actions=[Action(species='CO', coord=center)],
               rate_constant='p_COgas*A*bar/sqrt(2*m_CO*umass/beta)')

pt.add_process(name='O_adsorption',
               conditions=[Condition(species='empty', coord=center)],
               actions=[Action(species='O', coord=center)],
               rate_constant='p_COgas*A*bar/sqrt(2*m_O*umass/beta)')

pt.add_process(name='O_desorption',
               conditions=[Condition(species='O', coord=center)],
               actions=[Action(species='empty', coord=center)],
               rate_constant='p_COgas*A*bar/sqrt(2*m_O*umass/beta)')

# fetch a lot of coordinates
coords = pt.lattice.generate_coord_set(size=[2, 2, 2],
                                       layer_name='simplecubic_2d')

# fetch all nearest neighbor coordinates
nn_coords = [nn_coord for i, nn_coord in enumerate(coords)
             if 0 < (np.linalg.norm(nn_coord.pos - center.pos)) <= A]

# which will be bystanders to the CO desorption process
bystander_list = [Bystander(coord=coord,
                            allowed_species=['CO',],
                            flag='1nn') for coord in nn_coords]

# and conditions and actions are simply
conditions = [Condition(species='CO',coord=center)]
actions = [Action(species='empty',cood=center)]

# define the rate at ZCL
rate_constant = 'p_COgas*A*bar/sqrt(2*m_CO*umass/beta)*exp(beta*(E_CO-mu_COgas)*eV)'
# and the otf rate expression
otf_rate = 'base_rate*exp(beta*nr_CO_1nn*E_CO_nn*eV)'

proc = Process(name='CO_desorption',
                conditions=conditions,
                actions=actions,
                bystander_list = bystander_list,
                rate_constant=rate_constant,
                otf_rate=otf_rate)
pt.add_process(proc)

pt.filename = 'pairwise_interaction_otf.xml'
pt.save()
