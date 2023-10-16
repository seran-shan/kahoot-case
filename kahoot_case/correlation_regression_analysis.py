import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_with_expenditure(merged_data):
    """
    Plot scatter plots to visually present the relationship between rankings and educational expenditure.

    Parameters:
    - merged_data: Merged DataFrame containing consolidated data.
    """
    plt.figure(figsize=(15,5))
    sns.scatterplot(x="Public institutions", y="world_rank_cwur", data=merged_data, label="CWUR")
    sns.scatterplot(x="Public institutions", y="world_rank_shanghai", data=merged_data, label="Shanghai")
    sns.scatterplot(x="Public institutions", y="world_rank_times", data=merged_data, label="Times")
    plt.gca().invert_yaxis()
    plt.legend()
    plt.show()


def plot_correlation_heatmap(merged_data):
    """
    Plot heatmap showcasing the correlation between the university rankings from CWUR, Shanghai, and Times.

    Parameters:
    - merged_data: Merged DataFrame containing consolidated data.
    """
    # Plotting heatmap...
    correlation_data = merged_data[["world_rank_cwur", "world_rank_shanghai", "world_rank_times", "Public institutions", "Private institutions"]].corr()
    plt.figure(figsize=(10,7))
    sns.heatmap(correlation_data, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.show()
