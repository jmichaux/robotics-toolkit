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

def rot_rpy_mat(roll, pitch=None, yaw=None):
    """
    Return 3D rotation matrix specified by roll, pitch, yaw, euler angles.

    Each angle represents a rotation about the FIXED world frame. Roll, pitch,
    and yaw angles are also known as the XYZ (or sometimes ZYX) Euler angles.
    Roll is a rotation about the fixed X axis, pitch is a rotation about the
    fixed Y axis, and yaw is a rotation about the fixed Z axis. Since these
    rotations are about the fixed world axes, we pre-multiply as indicated
    below:

        R = Rot(z, yaw) * Rot(y, pitch) * Rot(x, roll)

    Args
        roll (float): rotation about X axis
        pitch (float): rotation about Y axis
        yaw (float): rotation about Z axis

    Return
        euler_rpy_mat: 3D rotation matrix
    """
    Rx = rotx_mat(roll)
    if pitch is None:
        Ry = roty_mat(0)
    else:
        Ry = roty_mat(pitch)
    if yaw is None:
        Rz = rotz_mat(0)
    else:
        Rz = rotz_mat(yaw)
    return Rz.dot(Ry.dot(Rx))

def rot_rpy(vec, roll, pitch=None, yaw=None):
    """
    Return a vector after applying roll, pitch,
    and yaw transformation
    """
    return np.dot(rot_rpy_mat(roll, pitch, yaw), vec)
