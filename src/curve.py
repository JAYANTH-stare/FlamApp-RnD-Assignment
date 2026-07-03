import numpy as np


def generate_curve(theta_deg, M, X, num_points=1500):
    """
    Generate the parametric curve.

    Parameters
    ----------
    theta_deg : float
        Angle in degrees.

    M : float
        Exponential coefficient.

    X : float
        Horizontal shift.

    num_points : int
        Number of sampled points.

    Returns
    -------
    x, y
    """

    theta = np.deg2rad(theta_deg)

    t = np.linspace(6, 60, num_points)

    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y