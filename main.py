import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

# 1. load the dataset
housing = pd.read_csv('housing.csv')

print(housing)
# 2.Creating a Stratified test set
housing['income_cat'] = pd.cut(housing['median_income'], 
                               bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                               labels=[1, 2, 3, 4, 5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_set, test_set in split.split(housing, housing['income_cat']):
    strat_train_set =  housing.loc[train_set].drop('income_cat', axis=1)
    strat_test_set = housing.loc[test_set].drop('income_cat', axis=1)

# we will work on the copy of training data   

housing = strat_train_set.copy()

# 3. seprate features and labels

housing_labels = housing['median_house_value'].copy()
housing = housing.drop('median_house_value', axis=1)

test_labels = strat_test_set['median_house_value'].copy()
test_features = strat_test_set.drop('median_house_value', axis=1)


# 4. seprate numerical and categorical columns 

num_attributes = housing.drop('ocean_proximity', axis=1).columns.tolist()
cat_attributes = ['ocean_proximity']

# 5. lets make the pipeline 

# for numerical columns
num_pipeline = Pipeline([
    ('impute', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# for categorical columns
cat_pipeline = Pipeline([
    ('encode', OneHotEncoder(handle_unknown='ignore'))
])

# Constructing the full pipeline

full_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_attributes),
    ('cat', cat_pipeline, cat_attributes)
])

# 6. Transform the data

housing_prepared = full_pipeline.fit_transform(housing)
test_prepared = full_pipeline.transform(test_features)
# print(housing_prepared)

# 7. Training the model

# RandomForest model
Random_forest_reg = RandomForestRegressor(n_estimators=10, n_jobs=1)
Random_forest_reg.fit(housing_prepared, housing_labels)
Random_forest_preds = Random_forest_reg.predict(test_features)
test_pred = r2_score(test_labels, Random_forest_preds)
print(f'R2: {test_pred:.4f}')
# Random_forest_rmse = root_mean_squared_error(housing_labels, Random_forest_preds)
# print(f'The root mean squared error for RandomForest is {Random_forest_rmse}')
score = cross_val_score(Random_forest_reg, housing_prepared, housing_labels, scoring='r2', cv=5)
print(f'mean R2:{score.mean():.4f} ')