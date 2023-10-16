import matplotlib.pyplot as plt

def plot_rankings_distribution(merged_data):
    """
    Plots the distribution of university rankings for 2015.
    
    Parameters:
    - merged_data: Merged DataFrame containing consolidated data.
    """
    plt.figure(figsize=(15,5))
    plt.hist(merged_data['world_rank_cwur'].dropna(), bins=100, alpha=0.5, label="CWUR")
    plt.hist(merged_data['world_rank_shanghai'].dropna(), bins=100, alpha=0.5, label="Shanghai")
    plt.hist(merged_data['world_rank_times'].dropna(), bins=100, alpha=0.5, label="Times")
    plt.legend(loc="upper right")
    plt.show()


def plot_educational_expenditure_distribution(merged_data):
    """
    Plots the distribution of educational expenditure as % of GDP for 2011.
    
    Parameters:
    - merged_data: Merged DataFrame containing consolidated data.
    """
    plt.figure(figsize=(15,5))
    plt.hist(merged_data['Public institutions'].dropna(), bins=50, alpha=0.5, label="Public institutions")
    plt.hist(merged_data['Private institutions'].dropna(), bins=50, alpha=0.5, label="Private institutions")
    plt.legend(loc="upper right")
    plt.show()
