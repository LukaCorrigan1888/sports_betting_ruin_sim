# Sports Betting Bankroll Simulation  
### Monte Carlo Analysis of Ruin Probability Under Different Staking Strategies

## Overview

This project simulates repeated sports betting using Monte Carlo methods to evaluate how different staking strategies impact:

- Probability of ruin  
- Time to ruin  
- Ending bankroll distribution  
- Maximum drawdown  

The objective is to analyse how bankroll allocation rules affect long-run survival and growth under repeated independent bets.

---

## Problem Setup

We assume repeated bets with:

- True win probability p  
- Decimal odds d  
- Initial bankroll B₀  

Each bet results in:

- Win: bankroll increases by stake × (d − 1)  
- Loss: bankroll decreases by stake  

A bankroll path is simulated over N bets.

**Ruin** is defined as the bankroll falling below a specified threshold (default: 20% of starting bankroll).

---

## Staking Strategies Compared

### 1. Flat Staking  
Bet a fixed dollar amount per bet.

### 2. Fixed Fraction  
Bet a fixed percentage of current bankroll (e.g., 1% or 2%).

### 3. Fractional Kelly  
Bet a fraction of the Kelly optimal stake:

f* = (p(d − 1) − (1 − p)) / (d − 1)

Kelly maximises long-run logarithmic growth but increases volatility. Fractional Kelly (e.g., 0.25 or 0.5) reduces risk.

---

## Methodology

For each staking strategy:

- Simulate 10,000–20,000 independent bankroll paths  
- Each path consists of 1,000 sequential bets  
- Record:
  - Ruin indicator  
  - Time to ruin  
  - Ending bankroll  
  - Maximum drawdown  

Monte Carlo estimates are summarised and compared across strategies.

---

## Key Risk Metrics

- **Ruin Probability** – proportion of paths that fall below the ruin threshold  
- **Median Ending Bankroll** – typical long-run outcome  
- **5th Percentile Ending Bankroll** – downside risk measure  
- **Maximum Drawdown** – largest peak-to-trough loss  

---

## Example Insight

Even with positive expected value:

- Aggressive staking increases drawdowns  
- Overbetting reduces long-run growth  
- Fractional Kelly often improves growth while moderating ruin risk  

This demonstrates that staking choice materially affects survival probability — not just expected return.

---

## Project Structure

src/  
&nbsp;&nbsp;&nbsp;&nbsp;sim/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;engine.py      # Monte Carlo simulation engine  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;staking.py     # Staking rules  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metrics.py     # Summary statistics  

notebooks/  
&nbsp;&nbsp;&nbsp;&nbsp;01_ruin_analysis.ipynb  

pyproject.toml  
README.md  

---

## How to Run

Install dependencies:

    uv sync

---

## Motivation

This project demonstrates:

- Monte Carlo simulation  
- Risk modelling and ruin analysis  
- Kelly Criterion implementation  
- Bankroll growth dynamics  
- Clean Python project structure (src layout, modular design)  

It connects probability theory with practical risk management in repeated investment/betting environments.