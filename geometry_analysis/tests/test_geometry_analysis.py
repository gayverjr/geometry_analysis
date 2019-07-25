"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys
import numpy as np

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

def test_calculate_distance():
    '''Test calculate distance function.'''

    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])

    expected_distance = np.sqrt(2)
    actual_dist=geometry_analysis.calculate_distance(r1,r2)
    assert actual_dist == expected_distance

"""
def test_calculate_angle():
    '''Test the calculate_angle func'''

    A=np.array([1,0,0])
    B=np.array([0,0,0])
    C=np.array([0,1,0])
    AB = B - A
    BC = B - C
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB)*np.linalg.norm(BC)))
    correct_angle = np.pi/2
    assert theta == correct_angle
"""

@pytest.mark.parametrize("p1,p2,p3,expected_angle",
    [(np.array([1,0,0]),np.array([0,0,0]),np.array([0,1,0]),np.pi/2),
    (np.array([0,0,-1]),np.array([1,0,0]),np.array([0,1,0]),np.pi/3)])

def test_calculate_angle(p1,p2,p3,expected_angle):
    calculated_angle = geometry_analysis.calculate_angle(p1,p2,p3)
    assert np.isclose(expected_angle,calculated_angle)

@pytest.fixture
def water_molecule():
    name="water"
    symbol = ["H","O","H"]
    coords = np.array([[2,0,0],[0,0,0],[-2,0,0]])
    water = geometry_analysis.Molecule(name,symbol,coords)
    return water

def test_molecule_set_coordinates(water_molecule):
    num_bonds=len(water_molecule.bonds)
    assert num_bonds == 2
    new_coords = np.array([[25,0,0],[0,0,0],[-2,0,0] ])
    water_molecule.coordinates=new_coords
    new_bonds= water_molecule.bonds
    assert len(new_bonds) == 1 
    assert np.array_equal(new_coords,water_molecule.coordinates)

def test_create_failure():
    name = 25
    symbols = ["H","O","H"]
    coords= np.zeros([3,3])
    with pytest.raises(TypeError):
        water = geometry_analysis.Molecule(name,symbols,coords)
