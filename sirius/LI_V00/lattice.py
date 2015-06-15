#!/usr/bin/env python3

import math as _math
import numpy as _np
import pyaccel as _pyaccel
import mathphys as _mp
from . import optics_mode_M0 as _optics_mode_M0

_default_optics_mode = _optics_mode_M0
_energy = 0.15e9 #[eV]
_emittance = 170.3329758677203e-09 #[m rad]
_family_segmentation = { }

def create_lattice(**kwargs):

    return []


def sirius_li_family_data(lattice):
    latt_dict=_pyaccel.lattice.finddict(lattice,'fam_name')
    data={}

    for key in latt_dict.keys():
        if key in _family_segmentation.keys():
            data[key] = {'index' : latt_dict[key], 'nr_segs' : _family_segmentation[key] , 'families' : key}

    return data

_the_ring = create_lattice()
_family_data = sirius_li_family_data(_the_ring)
