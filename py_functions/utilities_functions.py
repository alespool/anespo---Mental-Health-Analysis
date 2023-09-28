import scipy.stats as stats
from typing import Dict, List
import pandas as pd
from scipy import stats
import researchpy
import matplotlib.pyplot as plt
import seaborn as sns


def shapiro_wilk_and_bartlett_tests(
    df: pd.DataFrame, target_column: str, group_column: str
) -> Dict[str, Dict[str, float]]:
    """
    Perform Shapiro-Wilk test for normality and Bartlett's test for homoscedasticity tests on a DataFrame after removing all nas for selected columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        target_column (str): The column containing the target variable.
        group_column (str): The column containing the group variable.

    Returns:
        dict: A dictionary containing the results of the Shapiro-Wilk test and Bartlett's test.

    Examples:
        >>> normality_and_homoscedasticity_tests(df, 'target', 'group')
    """

    valid_data = df[df[target_column].notna() & df[group_column].notna()]

    # Check for normality using Shapiro-Wilk test for each group
    shapiro_results = {}
    groups = valid_data[group_column].unique()

    # Create a single figure with subplots for the Q-Q plots
    fig, axes = plt.subplots(1, len(groups), figsize=(15, 4))

    for i, group in enumerate(groups):
        data = valid_data[valid_data[group_column] == group][target_column]
        shapiro_stat, shapiro_p = stats.shapiro(data)
        shapiro_results[group] = {
            "Shapiro Statistic": shapiro_stat,
            "p-value": shapiro_p,
        }

        # Create a Q-Q plot in the corresponding subplot
        stats.probplot(data, plot=axes[i])
        axes[i].set_title(
            f"Q-Q Plot for {group} Group in {group_column}\n" f" p-value: {shapiro_p}"
        )
        axes[i].set_xlabel("Theoretical Quantiles")
        axes[i].set_ylabel("Ordered Values")

    # Adjust spacing between subplots
    plt.tight_layout()

    # Perform Bartlett's test on the filtered data for homoscedasticity
    bartlett_results = {}
    group_data = [
        valid_data[valid_data[group_column] == group][target_column] for group in groups
    ]
    bartlett_stat, bartlett_p = stats.bartlett(*group_data)
    bartlett_results[group_column] = {  # Changed to use group_column as the key
        "Bartlett Statistic": bartlett_stat,
        "p-value": bartlett_p,
    }

    # Print the test results
    print("Shapiro-Wilk Test Results:")
    for group, result in shapiro_results.items():
        print(
            f"Group: {group}, Shapiro Statistic: {result['Shapiro Statistic']}, p-value: {result['p-value']}"
        )

    print("\nBartlett Test Results:")
    for group, result in bartlett_results.items():
        print(
            f"Group: {group}, Bartlett Statistic: {result['Bartlett Statistic']}, p-value: {result['p-value']}"
        )

    return shapiro_results, bartlett_results


def print_contingency_table(contingency_table: Dict[str, List[float]]) -> None:
    """Prints the percentages of each column in the contingency table.

    Parameters:
        contingency_table (Dict[str, List[float]]): The contingency table obtained by chi-squared test.

    Returns:
        None
    """

    for column in contingency_table:
        print()
        print(contingency_table[column] / sum(contingency_table[column]))
        print()


def chi_squared_plot(
    data: pd.DataFrame, x_column: str, y_column: str, hue: str, color_palette: str
) -> pd.DataFrame:
    """
    Generates a chi-squared plot to visualize the relationship between two categorical variables in a given dataset.

    Parameters:
        - data: A pandas DataFrame containing the dataset.
        - x_column: The name of the column representing the independent variable.
        - y_column: The name of the column representing the dependent variable.
        - hue: The name of the column representing the categorical variable.
        - color_palette: The color palette to use for the plot

    Returns:
        A pandas DataFrame representing the contingency table.

    Examples:
    >>> chi_squared_plot(df, 'mhd', 'sex')
    """
    # Perform chi-squared test and generate contingency table
    crosstab, test_results, expected = researchpy.crosstab(
        data[x_column],
        data[y_column],
        test="chi-square",
        expected_freqs=True,
        prop="cell",
    )

    # Print chi-squared test results
    print(test_results)
    print()

    # Print the contingency table
    contingency_table = pd.crosstab(data[x_column], data[y_column])
    contingency_table = contingency_table.sort_values(by=x_column, ascending=True)

    print(f"Tables for {x_column} and {y_column}:\n")
    print(contingency_table)

    plt.figure(figsize=(8, 6))
    ax = sns.countplot(data=data, y=x_column, hue=hue, palette=color_palette)
    ax.set_title(
        f"Chi-Squared Test for '{x_column}'\n(p-value: {test_results['results'][1]:.4f})"
    )
    ax.set_ylabel(x_column.title())
    ax.set_xlabel("Count")

    plt.show()

    return contingency_table
