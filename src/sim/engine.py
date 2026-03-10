from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class SimConfig:
    """Simulation settings for a repeated-betting bankroll process."""
    p: float = 0.55              # true win probability
    d: float = 1.91              # decimal odds
    bankroll0: float = 1000.0
    n_bets: int = 1000
    ruin_threshold: float = 200.0  # "practical ruin" threshold

# Simulate 1 path of the bankroll process

def simulate_path(
    rng: np.random.Generator,
    cfg: SimConfig,
    stake_fn,
) -> dict:
    """
    Simulate ONE bankroll path over cfg.n_bets bets.

    stake_fn(bankroll) -> stake amount

    Returns dict with ruin flag, time-to-ruin, ending bankroll, and max drawdown.
    """
    bankroll = cfg.bankroll0

    peak = bankroll
    max_drawdown = 0.0

    ruined = False
    t_ruin = None

    for t in range(1, cfg.n_bets + 1):
        # Check ruin at start of each bet
        if bankroll <= cfg.ruin_threshold:
            ruined = True
            t_ruin = t - 1
            break

        stake = float(stake_fn(bankroll))

        # If stake is 0, bankroll doesn't change (still counts as a "bet step")
        if stake > 0:
            win = rng.random() < cfg.p
            if win:
                bankroll += stake * (cfg.d - 1.0)
            else:
                bankroll -= stake

        # Track drawdown
        peak = max(peak, bankroll)
        drawdown = (peak - bankroll) / peak if peak > 0 else 0.0
        max_drawdown = max(max_drawdown, drawdown)

    # If we never broke early but ended below threshold
    if (not ruined) and bankroll <= cfg.ruin_threshold:
        ruined = True
        t_ruin = cfg.n_bets

    return {
        "ruined": int(ruined),
        "t_ruin": t_ruin,
        "ending_bankroll": bankroll,
        "max_drawdown": max_drawdown,
    }

# Function that takes a SimConfig and a stake_fn_factory
# Runs many independent paths and returns list of path results (dicts) 

def run_monte_carlo(
    cfg: SimConfig,
    stake_fn_factory,
    n_paths: int = 10000,
    seed: int = 42,
) -> list[dict]:
    """
    Run many independent bankroll paths.

    stake_fn_factory(cfg) should return stake_fn(bankroll)->stake.
    """
    rng = np.random.default_rng(seed)

    results: list[dict] = []
    for _ in range(n_paths):
        stake_fn = stake_fn_factory(cfg)
        results.append(simulate_path(rng, cfg, stake_fn))

    return results