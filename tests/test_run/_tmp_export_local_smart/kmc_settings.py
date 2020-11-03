model_name = 'AB_no_diffusion'
simulation_size = 20
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "A":{"value":"1.552e-19", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_bind_CO":{"value":"-1.9", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_bind_O2":{"value":"-2.138", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react":{"value":"0.9", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"600", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "p_COgas":{"value":"1.0", "adjustable":True, "min":"1e-13", "max":"100.0","scale":"log"},
    "p_O2gas":{"value":"1.0", "adjustable":True, "min":"1e-13", "max":"100.0","scale":"log"},
    }

rate_constants = {
    "AB_react_down":("1/(beta*h)*exp(-beta*E_react*eV)", True),
    "AB_react_left":("1/(beta*h)*exp(-beta*E_react*eV)", True),
    "AB_react_right":("1/(beta*h)*exp(-beta*E_react*eV)", True),
    "AB_react_up":("1/(beta*h)*exp(-beta*E_react*eV)", True),
    "A_adsorption":("p_O2gas*bar*A/sqrt(2*pi*m_O2*umass/beta)", True),
    "A_desorption":("p_O2gas*bar*A/sqrt(2*pi*m_O2*umass/beta)*exp(beta*(E_bind_O2)*eV)", True),
    "B_adsorption":("p_COgas*bar*A/sqrt(2*pi*m_CO*umass/beta)", True),
    "B_desorption":("p_COgas*bar*A/sqrt(2*pi*m_CO*umass/beta)*exp(beta*(E_bind_CO)*eV)", True),
    }

site_names = ['default_a']
representations = {
    "A":"""Atoms('O')""",
    "B":"""Atoms('CO', [[0,0,0],[0,0,1.2]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "A":"""""",
    "B":"""""",
    "empty":"""""",
    }

tof_count = {
    "AB_react_down":{'TOF': 1},
    "AB_react_left":{'TOF': 1},
    "AB_react_right":{'TOF': 1},
    "AB_react_up":{'TOF': 1},
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 3)">
    <meta author="Max J. Hoffmann" debug="0" email="mjhoffmann@gmail.com" model_dimension="2" model_name="AB_no_diffusion"/>
    <species_list default_species="empty">
        <species color="" name="A" representation="Atoms('O')" tags=""/>
        <species color="" name="B" representation="Atoms('CO', [[0,0,0],[0,0,1.2]])" tags=""/>
        <species color="" name="empty" representation="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="A" scale="linear" value="1.552e-19"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="E_bind_CO" scale="linear" value="-1.9"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="E_bind_O2" scale="linear" value="-2.138"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="E_react" scale="linear" value="0.9"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="T" scale="linear" value="600"/>
        <parameter adjustable="True" max="100.0" min="1e-13" name="p_COgas" scale="log" value="1.0"/>
        <parameter adjustable="True" max="100.0" min="1e-13" name="p_O2gas" scale="log" value="1.0"/>
    </parameter_list>
    <lattice cell_size="1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0" default_layer="default" representation="" substrate_layer="default">
        <layer color="#ffffff" name="default">
            <site default_species="default_species" pos="0.0 0.0 0.0" tags="" type="a"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="AB_react_down" rate_constant="1/(beta*h)*exp(-beta*E_react*eV)" tof_count="{'TOF': 1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
            <condition coord_layer="default" coord_name="a" coord_offset="0 -1 0" species="B"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 -1 0" species="empty"/>
        </process>
        <process enabled="True" name="AB_react_left" rate_constant="1/(beta*h)*exp(-beta*E_react*eV)" tof_count="{'TOF': 1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
            <condition coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="B"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="AB_react_right" rate_constant="1/(beta*h)*exp(-beta*E_react*eV)" tof_count="{'TOF': 1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
            <condition coord_layer="default" coord_name="a" coord_offset="1 0 0" species="B"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="AB_react_up" rate_constant="1/(beta*h)*exp(-beta*E_react*eV)" tof_count="{'TOF': 1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
            <condition coord_layer="default" coord_name="a" coord_offset="0 1 0" species="B"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 1 0" species="empty"/>
        </process>
        <process enabled="True" name="A_adsorption" rate_constant="p_O2gas*bar*A/sqrt(2*pi*m_O2*umass/beta)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
        </process>
        <process enabled="True" name="A_desorption" rate_constant="p_O2gas*bar*A/sqrt(2*pi*m_O2*umass/beta)*exp(beta*(E_bind_O2)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="A"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="B_adsorption" rate_constant="p_COgas*bar*A/sqrt(2*pi*m_CO*umass/beta)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="B"/>
        </process>
        <process enabled="True" name="B_desorption" rate_constant="p_COgas*bar*A/sqrt(2*pi*m_CO*umass/beta)*exp(beta*(E_bind_CO)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="B"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
