#!/usr/bin/python

from distutils.core import setup

author = 'Max J. Hoffmann'
author_email = 'mjhoffmann@gmail.com'
description = "kMC modeling on steroids"
license = 'COPYING'
long_description = "A vigorous attempt to make lattice kinetic Monte Carlo modelling more accessible"
name='python-kmos'
packages = [
           'kmos',
           'kmos.pygtkcanvas',
           ]
package_dir = {'kmos':'kmos'}
package_data = {'kmos':['fortran_src/*f90',
                        'kmc_editor.glade',
                        'fortran_src/assert.ppc',
                        'kmc_project_v0.2.dtd']}
platforms = ['linux']
requires = ['kiwi',]
scripts = [
        'tools/kmos-gui',
        'tools/kmos-export-program',
        'tools/kmos-build',
        'tools/kmos-view',
        'tools/kmos-build-standalone',
        ]
url = 'https://github.com/mhoffman/kmos'
version = '0.1'

setup(
      author=author,
      author_email=author_email,
      description=description,
      license=license,
      long_description=long_description,
      name=name,
      packages=packages,
      package_dir=package_dir,
      package_data=package_data,
      platforms=platforms,
      requires=requires,
      scripts=scripts,
      url=url,
      version=version,
      )