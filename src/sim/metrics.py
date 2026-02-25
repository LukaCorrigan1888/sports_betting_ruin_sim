from __future__ import annotations

import numpy as np
import pandas as pd


def summarize(results: list[dict]):
    """
    Convert path results into a summary table and a full dataframe.
    """
    df = pd.DataFrame(results)

    ruin_prob = float(df["ruined"].mean())

    # time to ruin: only defined for ruined paths
    t_ruin_vals = df["t_ruin"].dropna()
    median_t_ruin = float(t_ruin_vals.median()) if len(t_ruin_vals) else np.nan

    summary = pd.DataFrame([{
        "ruin_prob": ruin_prob,
        "median_time_to_ruin": median_t_ruin,
        "median_ending_bankroll": float(df["ending_bankroll"].median()),
        "p05_ending_bankroll": float(df["ending_bankroll"].quantile(0.05)),
        "median_max_drawdown": float(df["max_drawdown"].median()),
    }])

    return summary, df