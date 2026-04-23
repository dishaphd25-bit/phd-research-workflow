Research Methodology: Thyroid Diagnosis Analysis

Purpose of the Dataset
The dataset (data/sample_data.csv) was created to simulate experimental records for a PhD research project focused on thyroid condition diagnosis. It contains parameters such as experiment_score, temperature, and humidity to evaluate diagnostic objectivity.
Data Cleaning Strategy: Missing Values
During the data preparation phase, missing numeric values were identified in the raw dataset.
Strategy: Mean Imputation.
Reasoning: This strategy was chosen because it is simple and suitable for small experimental datasets during the initial baseline study.
Visualizations Generated
The following plots were generated using the src/visualize_data.py script to interpret the cleaned data:
Score Variation Plot: To observe the distribution of experiment scores.
Environmental Condition Plot: To study the relationship between temperature and humidity during data collection.
Study Limitations
Sample Size: The current analysis uses a small sample of 10 rows for testing the workflow.Imputation Bias: While mean imputation is simple, it may not account for extreme outliers; median imputation is being considered for future iterations to reduce this effect.