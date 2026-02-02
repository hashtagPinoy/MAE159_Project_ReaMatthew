import matplotlib
import numpy as np
import scipy

def calculate_drag(CL: float, AR: float, CD0: float = 0.15) -> dict[str, float]:
    
    """
    Calculate aircraft drag coefficient.

    Parameters
        ----------
        CL : float
        Lift coefficient, dimensionless
        AR : float
        Wing aspect ratio, dimensionless
        CD0 : float, optional
        Zero-lift drag, dimensionless (default: 0.015)
        Returns
        -------
    dict
        Results dictionary with CD, e, CD_induced, CD0, L_over_D
    """
    if CL < 0:
        raise ValueError(f"CL must be non-negative, got {CL}")

    oswald_eff = 1 / (1.035 + 0.38 * CD0 * np.pi * AR)
    CD_induced = CL**2 / (np.pi * oswald_eff * AR)
    CD = CD0 + CD_induced
    LD_ratio = CL/CD
    
    return {
        "CD": CD,
        "e": oswald_eff,
        "CD_induced": CD_induced,
        "CD0": CD0,
        "LD_ratio": LD_ratio
        }


