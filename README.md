# TactIQ Proof of Concept

TactIQ is an AI-powered tactical analysis platform for sports, starting with rugby and football.

## Goals

- Detect players from match video.
- Track player positions over time.
- Identify tactical formations and key events.
- Visualize results in Jupyter notebooks.

## Setup Instructions

1. Create and activate the conda environment:
   ```
   conda env create -f environment.yml
   conda activate tactiq
   ```

2. Run Jupyter notebooks:
   ```
   jupyter notebook notebooks/player_tracking_demo.ipynb
   ```

3. Add your own match videos in `data/` and update paths in notebooks.

## Future Plans

- Expand to web API using FastAPI.
- Build React or Streamlit dashboard.
- Integrate GPS/tracking data.
