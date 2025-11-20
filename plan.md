Create an e-commerce recommendation project using machine learning and deep learning.

1.Tech Stack

Use TensorFlow and Keras for deep learning.

i've already the dataset of Retail Rocket dataset containing: events.csv
first analyse the events.csv file and then create the recommendation system based on that dataset.

You may select datasets that best fit each of the two model types below.

2.Datasets (Two Required)

Use two separate real-world datasets:

A.User Activity Dataset

Contains user-specific behavioral events (ratings, purchases, searches, clicks, views, etc.).

Used for personalized recommendation modeling.

B.Trending Dataset

Contains trending product categories, popular items, or aggregated high-level patterns.

Can be derived from another public dataset or a subset of the first dataset based on global statistics.

Used for trending-based recommendation modeling.

3.Machine Learning Models

Build two separate recommendation pipelines:

A.Personalized Recommendation Model

Predict product recommendations tailored to a specific user based on their historical activity.

B.Trending Recommendation Model

Recommend globally popular or trending items.

4.Algorithms

For each of the two models, train:

At least 3 traditional machine learning algorithms

Examples:

K-Nearest Neighbors (KNN)

Random Forest

Support Vector Machine

Gradient Boosting/XGBoost

At least 1 deep learning model

A neural network built with TensorFlow & Keras (e.g., dense NN, embedding-based NN, or shallow recommendation network)

5.Evaluation

Use an 80/20 train-test split on each dataset.

Compare model performance using appropriate metrics such as:

Accuracy

Precision/Recall

F1-score

RMSE/MAE (if using rating prediction)

Provide visualizations comparing ML vs. DL performance.

6.Final Output

Generate two recommendation outputs for a given test user:

Personalized recommendation(based on user activity)

Trending recommendation(based on trending dataset)

make a jupyter notebook