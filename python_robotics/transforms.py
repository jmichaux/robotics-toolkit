import numpy as np

def rot_inv(R):
    """
    Inverse rotation matrix
    """
    return R.T

def rot2d(vec, theta):
    """
    Return vector rotation

    Args
        vec (ndarray): Vector of len 2
        theta (float):  angle in radians

    Returns
        rotated vector (ndarray)
    """
    return np.dot(rot2d_mat(theta), vec)

def rot2d_mat(theta):
    """
    Return 2D rotation matrix

    Args
        theta (float): angle in radians

    Returns
        R: 2D rotation matrix
    """
    R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
    ])
    return R

def rotx(vec, theta):
    """
    Return vector rotation about X axis

    Args
        vec (ndarray): Vector of len 3
        theta (float):  angle in radians

    Returns
        rotated vector (ndarray)
    """
    return np.dot(rotx_mat(theta), vec)

def rotx_mat(theta):
    """
    Return 3D rotation matrix about X axis

    Args
        theta (float): angle in radians

    Returns
        Rx: 3D rotation matrix about X axis
    """
    Rx = np.array([
    [1, 0, 0],
    [0, np.cos(theta), -np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
    ])
    return Rx

def roty(vec, theta):
    """
    Return vector rotation about Y axis

    Args
        vec (ndarray): Vector of len 3
        theta (float):  angle in radians

    Returns
        rotated vector (ndarray)
    """
    return np.dot(roty_mat(theta), vec)

def roty_mat(theta):
    """
    Return 3D rotation matrix about Y axis

    Args
        theta (float): angle in radians

    Returns
        Rx: 3D rotation matrix about X axis
    """
    Ry = np.array([
    [np.cos(theta), 0, np.sin(theta)],
    [0, 1, 0],
    [-np.sin(theta), 0, np.cos(theta)]
    ])
    return Ry

def rotz(vec, theta):
    """
    Return vector rotation about Z axis

    Args
        vec (ndarray): Vector of len 3
        theta (float):  angle in radians

    Returns
        rotated vector (ndarray)
    """
    return np.dot(rotz_mat(theta), vec)

def rotz_mat(theta):
    """
    Return 3D rotation matrix about Z axis

    Args
        theta (float): angle in radians

    Returns
        Rx: 3D rotation matrix about X axis
    """
    Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
    ])
    return Rz

def euler_rpy_mat(angles):
    """
    3D rotation matrix specified by roll, pitch, yaw, euler angles

    Each angle represents a rotation about the fixed world frame.

    XYZ Euler angles (some books refer to these as ZYX)
    R = Rot(z,gamma) * Rot(y, beta) * Rot(x, alpha)
        euler_mat([alpha, beta, gamma], [2, 1, 0])

    Args
        angles (list or ndarray): Vector of len 3

    Return
        euler_rpy_mat: 3D rotation matrix
    """
    return rotz_mat(angles[2]).dot(roty_mat(angles[1]).dot(rotx_mat(angles[0])))
