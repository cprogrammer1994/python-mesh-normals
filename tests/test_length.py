import numpy as np
import pytest

import mesh_normals


def test_length():
    mesh = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [2.0, 0.0, 0.0],
        [2.0, 1.0, 0.0],
    ], 'f4')

    index = np.array([
        [1, 0, 2],
        [1, 2, 3],
        [3, 2, 4],
        [3, 4, 5],
    ], 'i4')

    normals_data = mesh_normals.build_normals(mesh, index, 12)
    normals = np.frombuffer(normals_data, 'f4').reshape(-1, 3)

    np.testing.assert_almost_equal(normals.shape, (len(mesh), 3))


def test_length_strided():
    mesh = np.array([
        [0.0, 0.0, 0.0, -1.0, -1.0],
        [0.0, 1.0, 0.0, -1.0, -1.0],
        [1.0, 0.0, 1.0, -1.0, -1.0],
        [1.0, 1.0, 1.0, -1.0, -1.0],
        [2.0, 0.0, 0.0, -1.0, -1.0],
        [2.0, 1.0, 0.0, -1.0, -1.0],
    ], 'f4')

    index = np.array([
        [1, 0, 2],
        [1, 2, 3],
        [3, 2, 4],
        [3, 4, 5],
    ], 'i4')

    normals_data = mesh_normals.build_normals(mesh, index, 20)
    normals = np.frombuffer(normals_data, 'f4').reshape(-1, 3)

    np.testing.assert_almost_equal(normals.shape, (len(mesh), 3))


if __name__ == '__main__':
    pytest.main([__file__])
