# Spatial Transcriptomics (Toy Example)

## Goal
Build intuition for spatial transcriptomics by visualizing cell coordinates and overlaying a gene expression signal.

## What I did
- Created a small synthetic dataset of spatial coordinates (x, y) and expression values.
- Plotted cells on a 2D map with color representing gene expression intensity.
- Added a colorbar to enable quantitative interpretation.
- Saved the figure to `outputs/` for reproducibility.

## Project structure
- `src/main.py`: generates the synthetic data and plot
- `outputs/spatial_cell_map.png`: saved figure

## Notes / Limitations
- This is toy data (not real spatial transcriptomics).
- Real workflows include QC, normalization, and spatial neighborhood analysis (often using tools like Scanpy/Squidpy).