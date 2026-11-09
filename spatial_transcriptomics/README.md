# Spatial Transcriptomics Visualization (Toy Example)

## Goal

Build a basic understanding of spatial transcriptomics by visualizing cell coordinates and gene expression levels.

## What I Did

- Created a small synthetic dataset containing six cells with spatial coordinates (x, y) and gene expression values.
- Used pandas to organize the data into a DataFrame.
- Used matplotlib to visualize cell locations, with colors representing gene expression levels.
- Added a colorbar to interpret expression intensity.
- Saved the resulting figure for reproducibility.

## Results

The visualization shows two spatially separated groups of cells with different gene expression levels.

In this hypothetical example, the first three cells represent a cancer group with higher expression, while the remaining three represent a normal group with lower expression.

These patterns were intentionally created for visualization practice and do not represent biological findings.

## Project Structure

- `src/main.py`: Generates synthetic data and creates the visualization.
- `outputs/spatial_cell_map.png`: Saved visualization.

## Limitations

- This project uses synthetic data rather than real spatial transcriptomics data.
- No statistical testing or biological interpretation was performed.
- Real spatial transcriptomics workflows require additional steps, such as quality control, normalization, and spatial analysis.

## Next Steps

Explore real spatial transcriptomics datasets and learn basic preprocessing and visualization using tools such as Scanpy or Squidpy.