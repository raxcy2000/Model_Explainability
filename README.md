# Model Explainability

## Interpret output of a model with SHAP and LIME


### Introduction
This is a project to try out the use of SHAP (SHapley Additive exPlanations) to explain the output of machine learning models.

More details on SHAP can be found in the [github repo](https://github.com/slundberg/shap#citations) and in the [documentation](https://shap.readthedocs.io/en/latest/index.html)

### Installation
- Create a new environment using conda. I used python 3.9 for this project

`conda create --name modelexplainenv python=3.9 -y`

- Activate the `modelexplainenv` created by using 
`conda activate modelexplainenv`

- Install all necessary packacges needed using
`pip install jupyter shap pandas numpy scikit-learn matplotlib seaborn` 

conda documentation says all the programs that you want in an environment should be installed at the same time. Installing 1 program at a time can lead to dependency conflicts.

### Data
