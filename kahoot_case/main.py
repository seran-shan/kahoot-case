from data_preprocessing import load_data, preprocess_and_merge
from exploratory_analysis import plot_rankings_distribution, plot_educational_expenditure_distribution
from correlation_regression_analysis import plot_correlation_with_expenditure, plot_correlation_heatmap

def main():
    cwur, shanghai, times, school_and_country, expenditure, attainment = load_data()

    merged_data = preprocess_and_merge(cwur, shanghai, times, school_and_country, expenditure, attainment)

    plot_rankings_distribution(merged_data)
    plot_educational_expenditure_distribution(merged_data)

    plot_correlation_with_expenditure(merged_data)

    plot_correlation_heatmap(merged_data)

if __name__ == "__main__":
    main()
