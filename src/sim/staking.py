# This file contains the different staking strategies for the simulation.

from __future__ import annotations

# Returns the minimum of the two values, but not less than 0.0

def stake_flat(bankroll: float, amount: float) -> float:
    """Flat staking: bet a fixed dollar amount each bet."""
    return max(0.0, min(amount, bankroll))

# Returns a stake thats a fraction of current bankroll

def stake_fraction(bankroll: float, fraction: float) -> float:
    """Fixed fraction staking: bet fraction * bankroll each bet."""
    stake = fraction * bankroll
    return max(0.0, min(stake, bankroll))

# Returns the stakethat maximises the expected log growth of bankroll.

def stake_kelly_fractional(
    bankroll: float,
    p: float,
    d: float,
    kelly_fraction: float,
    cap_fraction: float = 0.05,
) -> float:
    """
    Fractional Kelly staking (with optional cap).

    Parameters
    ----------
    bankroll : current bankroll
    p : win probability (true p in MVP; later can replace with p_hat)
    d : decimal odds
    kelly_fraction : e.g. 0.25 for quarter Kelly
    cap_fraction : max fraction of bankroll to bet (risk control)
    """
    b = d - 1.0
    if b <= 0:
        return 0.0

    # Full Kelly fraction of bankroll
    f_star = (p * b - (1.0 - p)) / b

    # Don't bet if negative EV
    f_star = max(0.0, f_star)

    # Fractional Kelly and cap
    f = min(kelly_fraction * f_star, cap_fraction)

    stake = f * bankroll
    return max(0.0, min(stake, bankroll))