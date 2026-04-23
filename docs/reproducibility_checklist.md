Reproducibility Checklist
Required Input Files
To run this analysis, the following files must be present in the data/ folder:
data/sample_data.csv: The raw experimental dataset containing missing values.

Software Dependencies
Ensure the following are installed via your requirements.txt file:

Python 3.x
Pandas
Matplotlib

Execution Order
To reproduce the results, execute the scripts in the following specific order:
1.python src/clean_data.py: Processes the raw data and handles missing values.
2.python src/visualize_data.py: Reads the cleaned data and generates research plots.

Expected Output Files
After successful execution, the following files should be generated in the results/ and data/ folders:

data/cleaned_data.csv: The dataset after mean imputation.
results/score_plot.png: Visualization of experiment scores.
results/temperature_humidity_plot.png: Visualization of environmental conditions.

Critical Assumptions
The script assumes a docs/ folder exists for methodology notes.
It is assumed that the column names in sample_data.csv have not been altered.