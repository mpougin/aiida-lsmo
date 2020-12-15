# -*- coding: utf-8 -*-
"""Test oxidation state prediction."""
import os
import pytest
from aiida.orm import CifData
from aiida_lsmo.calcfunctions.oxidation_state import compute_oxidation_states

from . import DATA_DIR

CIF_FILES = ['Fe-MOF-74.cif', 'Mg_MOF_74.cif', 'Cu-I-II-HKUST-1.cif']
OXIDATION_STATES = {
    'Fe-MOF-74.cif': [2, 2, 2, 2, 2, 2],
    'Mg_MOF_74.cif': [2, 2, 2, 2, 2, 2],
    'Cu-I-II-HKUST-1.cif': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
}


@pytest.mark.parametrize('cif_filename', CIF_FILES)
def test_oxidation_state(cif_filename):
    """Check that oxidation states are as expected."""
    with open(os.path.join(DATA_DIR, cif_filename), 'rb') as handle:
        cif = CifData(file=handle)

    results_dict = compute_oxidation_states(cif).get_dict()
    assert results_dict['prediction'] == OXIDATION_STATES[cif_filename]