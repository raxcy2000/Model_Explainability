# Model Explainability

## Interpret output of a model with SHAP and LIME


### Introduction
This is a project to try out the use of SHAP (SHapley Additive exPlanations) to explain the output of machine learning models.

More details on SHAP can be found in the [github repo](https://github.com/slundberg/shap#citations) and in the [documentation](https://shap.readthedocs.io/en/latest/index.html)

Good read on the theory of SHAP [here](https://christophm.github.io/interpretable-ml-book/shap.html)

Good read on the theory of LIME [here](https://christophm.github.io/interpretable-ml-book/lime.html#lime)

### Installation
- Create a new environment using conda. I used python 3.9 for this project

`conda create --name modelexplainenv python=3.9 -y`

- Activate the `modelexplainenv` created by using 
`conda activate modelexplainenv`

- Install all necessary packacges needed using
`pip install jupyter shap pandas numpy scikit-learn matplotlib seaborn catboost` 

conda documentation says all the programs that you want in an environment should be installed at the same time. Installing 1 program at a time can lead to dependency conflicts.

### Data



### Citataion
- Lundberg SM, Lee SI. A unified approach to interpreting model predictions. In: Guyon I, Luxburg UV, Bengio S, Wallach H, Fergus R, Vishwanathan S, Garnett R, editors. Advances in neural information processing systems. New York: Curran Associates; 2017. p. 4765–74.

- SHAP - What Is Your Model Telling You? Interpret CatBoost Regression and Classification Outputs by Manuel Amunategui. Avaialable at https://www.youtube.com/watch?v=ZkIxZ5xlMuI&t=15s accessed on 27 April, 2023.