# Student Dropout Predictor - Model Performance

This file contains the details of the model training phase for the Student Dropout Predictor, including the comparison of different algorithms and the final evaluation metrics of the selected best model. `model.pkl` has been successfully created.

## 📊 Algorithm Accuracy Comparison

During the model selection phase, several classification algorithms were evaluated based on their accuracy:

- **Logistic Regression**: 61.67%
- **Support Vector Machine (SVM)**: 83.33%
- **Decision Tree**: 95.00%
- **Random Forest**: 95.00%

## 🏆 Best Model: Random Forest

Based on the evaluation, **Random Forest** was selected as the best performing model. The model has been saved as `model.pkl` for use in the application.

### Overall Performance Metrics
- **Accuracy**: 0.9667 (96.67%)
- **RMSE (Root Mean Square Error)**: 0.1826
- **R2 Score**: 0.8460

### Confusion Matrix
```
[[39  2]
 [ 0 19]]
```

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **0** (No Dropout) | 1.00 | 0.95 | 0.97 | 41 |
| **1** (Dropout) | 0.90 | 1.00 | 0.95 | 19 |
| | | | | |
| **Accuracy** | | | **0.97** | **60** |
| **Macro Avg** | 0.95 | 0.98 | 0.96 | 60 |
| **Weighted Avg** | 0.97 | 0.97 | 0.97 | 60 |

---

## 📖 Glossary of Terminologies

If you are new to machine learning evaluation metrics, here are the definitions of the terms used above:

- **Accuracy**: The ratio of correctly predicted observations to the total observations. It answers the question: *Overall, how often is the classifier correct?*
- **RMSE (Root Mean Squared Error)**: A measure of the differences between values predicted by a model and the values observed. Lower values indicate a better fit to the data. While often used for regression, it can also provide insight in some probabilistic classification tasks. 
- **R2 Score (R-Squared)**: A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. Closer to 1.0 indicates a better fit.
- **Confusion Matrix**: A table used to describe the performance of a classification model. The rows represent the actual classes, while columns represent predicted classes.
  - *True Positives (19)*: Model correctly predicted a dropout (Class 1).
  - *True Negatives (39)*: Model correctly predicted no dropout (Class 0).
  - *False Positives (2)*: Model incorrectly predicted a dropout (actual was no dropout).
  - *False Negatives (0)*: Model incorrectly predicted no dropout (actual was dropout).
- **Precision**: The ratio of correctly predicted positive observations to the total predicted positive observations. *Of all the students we predicted would drop out, how many actually did?*
- **Recall (Sensitivity)**: The ratio of correctly predicted positive observations to all actual positive observations. *Of all the students that actually dropped out, how many did we predict correctly?*
- **F1-Score**: The harmonic mean of Precision and Recall. It's a single metric that balances both precision and recall, especially useful when dealing with uneven class distribution.
- **Support**: The number of actual occurrences of each class in the test dataset. In this case, 41 instances of Class 0 and 19 instances of Class 1.
- **Macro Avg**: The simple average of precision, recall, and F1-score across all classes. It treats all classes equally, regardless of their sample size.
- **Weighted Avg**: The average of precision, recall, and F1-score across all classes, weighted by the number of true instances for each class (support). This is useful when the dataset is imbalanced.
