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