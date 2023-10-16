from statsmodels.formula.api import ols

def perform_regression_analysis(merged_data):
    """
    Perform regression analysis.
    
    Parameters
    ----------
    merged_data : pandas.DataFrame
        Merged data.
    """
    results = []
    for ranking in ["world_rank_cwur", "world_rank_shanghai", "world_rank_times"]:
        for expenditure in ["Public institutions", "Private institutions"]:
            formula = f"{ranking} ~ {expenditure}"
            model = ols(formula, data=merged_data).fit()
            results.append((ranking, expenditure, model.summary()))
    return results
