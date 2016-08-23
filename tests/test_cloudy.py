import os

import numpy as np
from cloudy.cloudy import Cloudy

dire = 'sample_data'
grd1 = os.path.join(dire, 'sample.grd')
grd2 = os.path.join(dire, 'sample_2.grd')
ems1 = os.path.join(dire, 'sample.ems')
ems2 = os.path.join(dire, 'sample_2.ems')
test_1 = Cloudy(grd1, ems1)
test_2 = Cloudy(grd2, ems2)
test_3 = Cloudy(grd2, ems2, ['hden', 'Temperature'])


def test_read_grd():
    arr1 = np.arange(8000., 40100., 1000)
    assert test_1.grd.dtype == 'float64'
    assert np.array_equal(test_1.grd[0], arr1)
    temps = np.arange(100, 4050, 50)
    arr2 = [
        np.concatenate(
            [np.repeat(3.5, len(temps)), np.repeat(4.0, len(temps))]),
        np.tile(
            temps, 2)
    ]
    assert test_2.grd.dtype == 'float64'
    assert np.array_equal(test_2.grd, arr2)


def test_df():
    test_labels_1 = [
        'H  1  6563A', 'N  2  6584A', 'O  1  6300A', 'S  2  6720A',
        'depth']
    assert test_1.labels == test_labels_1
    test_labels_2 = ['H2   2.121m', 'depth']
    assert test_2.labels == test_labels_2
    test_labels_3 = ['H2   2.121m', 'Temperature', 'depth', 'hden']
    assert test_3.labels == test_labels_3

    assert test_1.df['H  1  6563A'][0] == -18.9131
    assert test_1.df['H  1  6563A'][16] == -16.8257
    assert test_1.df['H  1  6563A'][32] == -17.2029
