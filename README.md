# Heart Deseases Prediction
## Project related with [Kaggle Community Prediction Competition](https://www.kaggle.com/competitions/yap15-heart-diseases-predictions/leaderboard)

**The main idea of this project** is prediction of the heart deseases risk based on patient lifestyle information. The presented data included general information about patients (*age*, *height*, *weight*, *gender* and others) and medical indicators (*cholesterol level*, *glucose level*, *diastolic and systolic pressure values*). Before analysis and applying machine learning, preprocessing was carried out.

**Compared ML algorithms**: *Random Forest*, *Gradient Boosting*. \
**The evaluation metric** is *ROC AUC score*.

The best result was shown by the *Gradient Boosting Model (GBM)* after selecting the optimal parameters. \
This model was ranked first in [the kaggle competition](https://www.kaggle.com/competitions/yap15-heart-diseases-predictions/leaderboard).

The best AUC-ROC score on the **train** set: **0.80313** \
The best AUC-ROC score on the **test** set: **0.80415**

In addition, the streamlit application based this model was created. It allows you to predict the risk of heart deseases when choosing your or patient's parameters in real time. 

### Files in the directory:
- `app.py` - streamlit application file
-  `hd_notebook.ipynb` - notebook with data preprocessing, analysis and selecting ML model
-  `gbm_model.pcl` - compressed gbm model
