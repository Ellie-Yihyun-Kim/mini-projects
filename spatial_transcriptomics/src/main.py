
# --- Import Libraries ---
import matplotlib.pyplot as plt
import pandas as pd


# --- Generate Synthetic Data ---
# Create example cell coordinates and gene expression values.
# The first three cells represent a hypothetical cancer group,
# and the remaining three represent a hypothetical normal group.
# These labels are illustrative, not experimentally validated.

data = {
    "x": [1, 2, 3, 8, 9, 10],
    "y": [1, 2, 1, 8, 9, 8],
    "gene_expression": [100, 95, 110, 10, 5, 15]
}

# Convert the dictionary into a pandas DataFrame.
df = pd.DataFrame(data)


# --- Visualize Spatial Gene Expression ---
# Plot cell locations and color each point by expression level.
plt.figure(figsize=(6, 5))

plt.scatter(
    df["x"],
    df["y"],
    c=df["gene_expression"],
    cmap="viridis"
)

# Add a colorbar to show expression intensity.
plt.colorbar(label="Gene Expression Level")

# Add labels and a title.
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Spatial Cell Map (Synthetic Data)")

# Save and display the figure.
plt.savefig(
    "../outputs/spatial_cell_map.png",
    dpi=200,
    bbox_inches="tight"
)
plt.show()