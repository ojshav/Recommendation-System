## Description

- Approach 1: Machine Learning-Based Recommendation System

## **Data collection [¶](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#2.1-Data-collection-)**

- The first step in building a recommendation engine is data collection.
- There are two forms of data collection techniques employed in recommender systems.
- These are **explicit** and **implicit** forms of data collection.
- **Explicit data** is information that is provided intentionally, i.e. input from the users such as movie ratings.
- **Implicit data** is information that is not provided intentionally but gathered from available data streams like search history, clicks, order history, etc.

### **Examples of explicit data collection include the following**

- Asking a user to rate an item on a sliding scale.
- Asking a user to search.
- Asking a user to rank a collection of items from favorite to least favorite.
- Presenting two items to a user and asking him/her to choose the better one of them.
- Asking a user to create a list of items that he/she likes.

### **Examples of implicit data collection include the following**

- Observing the items that a user views in an online store.
- Analyzing item/user viewing times.
- Keeping a record of the items that a user purchases online.
- Obtaining a list of items that a user has listened to or watched on his/her computer.
- Analyzing the user's social network and discovering similar likes and dislikes.

## **Data storage [¶](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#2.2-Data-storage-)**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- The second step in building a recommendation engine is data storage.
- The amount of data storage dictates how good the recommendations of the model are.
- For example, in a movie recommendation system, the more ratings users give to movies, the better the recommendations get for other users.
- The type of data plays an important role in deciding the type of storage that has to be used.
- This type of storage could include a standard SQL database, a NoSQL database or some kind of object storage.

# 

## **2.3 Filtering the data**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- The third and final step in building a recommendation engine is filter the data to extract relevant information required to make final recommendations.
- There are two major approaches to filter the data to extract relevant information. These are as follows:-
- 
    1. [**Collaborative Filtering**](https://en.wikipedia.org/wiki/Collaborative_filtering) – based on similar users.
- 
    1. [**Content-Based Filtering**](http://recommender-systems.org/content-based-filtering/) – based on product attributes.
- The difference between the above two approaches are shown in the following diagram-

![image](https://github.com/user-attachments/assets/df194b67-5fd8-4d2c-92d3-b4dc8e5f56cd)


# **Collaborative Filtering Recommender System ¶**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- In the [collaborative filtering](https://en.wikipedia.org/wiki/Collaborative_filtering) recommender system, the behaviour of a group of users is used to make recommendations to other users.
- In this case, the system don’t have any knowledge about the product.
- Collaborative filtering approach build a model from a user’s past behaviour (items previously purchased or selected and/or numerical ratings given to those items) as well as similar decisions made by other users.
- This model is then used to predict items (or ratings for items) that the user may have an interest in.
- It recommends based on the user’s rating in the past.
- These systems try to predict the user’s rating or preferences based on past rating or preferences of other users.
- These filters do not require item metadata to make predictions.
- There are two types of collaborative filtering recommender system. They are:-

### **1. User-based collaborative filtering**

- In this method products are recommended to a user based on the fact that the products have been liked by users similar to the user.

### **2. Item-based collaborative filtering**

- This method identifies and predict similar items based on users’ previous ratings.

# 

### **Collaborative filtering methods are also classified as memory-based and model-based**

- An example of memory-based approach is the user-based algorithm while that of model-based approach is Kernel-Mapping Recommender.
- Collaborative filtering approaches often suffer from three problems -
1. cold start
2. scalability
3. sparsity
- These are discussed below:-

### **1. Cold start**

- Cold start refers to a problem, when for a new user or item there is not enough data to make recommendations.

### **2. Scalability**

- To make recommendations, we need to choose from millions of users and products. So scalability means a large amount of computation power is required to make recommendations.

### **3. Sparsity**

- The number of items sold on e-commerce portals are extremely large. The most active users will only have rated a small subset of overall database. Thus, even the most popular items have very few ratings.
- Most famous example of collaborative filtering is item-to-item collaborative filtering (people who buy x also buy y). This algorithm is popularized by Amazon recommender system.
- Social network companies like Facebook, originally used collaborative filtering to recommend new friends and groups by examining the network of connections between a user and their friends.
- The diagram below demonstrates collaborative filtering recommender systems.

# 

![image](https://github.com/user-attachments/assets/949f2aea-7449-4009-96bc-ca71927eb4ca)


### **image source : https://medium.com/@tomar.ankur287/user-user-collaborative-filtering-recommender-system-51f568489727**

# 

# **4. Content-based Filtering Recommender System**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- Another common approach when designing recommender systems is [Content-based Filtering](http://recommender-systems.org/content-based-filtering/).
- Content-based filtering methods are based on a description of the item and a profile of the user’s preferences.
- These methods are best suited to situations where there is known data on an item (name, location, description, etc.), but not on the user.
- In content based filtering recommender system, the similarity between different products is calculated on the basis of the attributes of the products.
- The system uses the knowledge of each product to recommend a new product.
- Content-based filtering approaches utilize a series of discrete characteristics of an item in order to recommend additional items with similar properties.
- For example, in a content based movie recommender system, the similarities between the movies is calculated on the basis of genres, the actors and the director.
- The general idea behind these recommender systems is that if a person liked a particular item, then he will also like an item similar to it.
- Content-based recommenders treat recommendation as a user-specific classification problem and learn a classifier for the user's likes and dislikes based on product features.
- The diagram below demonstrates content-based filtering recommender systems.

# 

![image](https://github.com/user-attachments/assets/d2d3b2eb-dedc-4499-80c3-fa1307c0e8eb)




# 

# 


# **5. Hybrid Recommender Systems**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- Most recommender systems now use a hybrid approach.
- It means to combine collaborative filtering, content-based filtering and other approaches.
- Hybrid approaches can be implemented in several ways which are as follows:
1. By making content-based and collaborative-based predictions separately and then combining them.
2. By adding content-based capabilities to a collaborative-based approach (and vice versa) or
3. By combining the approaches into one model.
- An example of hybrid recommender systems is Netflix website.
- The website makes recommendations by comparing the watching and searching habits of similar users (collaborative filtering) as well as by offering movies that share characteristics with films that a user has rated highly (content-based filtering).

Some hybridization techniques include:

- **Weighted**: Combining the score of different recommendation components numerically.
- **Switching**: Choosing among recommendation components and applying the selected one.
- **Mixed**: Recommendations from different recommenders are presented together to give the recommendation.
- **Feature Combination**: Features derived from different knowledge sources are combined together and given to a single recommendation algorithm.
- **Feature Augmentation**: Computing a feature or set of features, which is then part of the input to the next technique.
- **Cascade**: Recommenders are given strict priority, with the lower priority ones breaking ties in the scoring of the higher ones.
- **Meta-level**: One recommendation technique is applied and produces some sort of model, which is then the input used by the next technique.

# 

# **6. Introduction to Matrix Factorization**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- **Matrix factorization** is a class of collaborative filtering algorithms used in recommender systems.
- **Matrix factorization** algorithms work by decomposing the user-item interaction matrix into the product of two lower dimensionality rectangular matrices.
- It became widely known during the Netflix prize challenge due to its effectiveness as reported by Simon Funk in 2006.
- The idea behind matrix factorization is to represent users and items in a lower dimensional latent space.
- Matrix factorization can be demonstrated by the following diagram-

# 

![image](https://github.com/user-attachments/assets/b91beb86-cfec-45fc-9647-c2cb551ce5ca)




# 

- Nowadays, different types of matrix factorization approaches are used in practice.
- Most popular used matrix factorization approaches are discussed below.

# 

## **Funk SVD**

- Funk SVD is the original algorithm proposed by Simon Funk.
- He factorized the user-item rating matrix as the product of two lower dimensional matrices – the first one has a row for each user while the second one has a column for each item.
- The row or column associated to a specific user or item is referred to as latent factors.
- Despite its name, in Funk SVD, no singular value decomposition is applied.

## **SVD ++**

- FunkSVD is able to provide very good recommendation quality, its ability to use only explicit numerical ratings as user-items interactions constitutes a limitation.
- Modern day recommender systems should exploit all available interactions both explicit (e.g. numerical ratings) and implicit (e.g. likes, purchases, skipped, bookmarked).
- Keeping this in mind, SVD++ was designed to take into account implicit interactions as well.
- As compared to FunkSVD, SVD++ takes also into account user and item bias.

## **Asymmetric SVD**

- Asymmetric SVD aims at combining the advantages of SVD++ while being a model based algorithm.
- Therefore it is able to consider new users with a few ratings without needing to retrain the whole model.

## **Hybrid Matrix Factorization**

- In recent years many other matrix factorization models have been developed to exploit the ever increasing amount and variety of available interaction data and use cases.
- Hybrid matrix factorization algorithms are capable of merging explicit and implicit interactions or both content and collaborative data.

# 

# **7. Evaluating Recommender Systems**

[Table of Contents](https://www.kaggle.com/code/prashant111/recommender-systems-in-python#0.1)

- Once we develop a recommender system, we want to evaluate them.
- Evaluation is important in assessing the effectiveness of recommender systems.
- To measure the effectiveness of recommender systems, three types of evaluations are available –
1. user studies,
2. online evaluations (A/B tests), and
3. offline evaluations.
- The commonly used metrics are the mean squared error (MSE) and root mean squared error(RMSE).
- The information retrieval metrics such as precision and recall are useful to assess the quality of a recommender system.
- Diversity, novelty and coverage are also considered as important aspects in evaluation.
- User studies are rather small scale judgement technique. A few dozens or hundreds of users are presented recommendations created by different recommendation approaches, and then the users’ judge which recommendations are the best.
- In A/B tests, recommendations are shown to thousands of users of a real product, and the recommender system randomly picks at least two different recommendation approaches to generate recommendations.
- The effectiveness is measured with implicit measures of effectiveness such as conversion rate or click-through rate.
- Offline evaluations are based on historic data. For example, a dataset that contains information about how users previously rated movies.
- The effectiveness of recommendation system is then measured based on how well a recommendation approach can predict the users' ratings in the dataset.

### **Beyond measures of accuracy**

Research on recommender systems is focussed towards finding the most accurate recommendation algorithms. There are a number of factors that are also important. These are discussed below.

- **Diversity** – Users tend to be more satisfied with recommendations when there is a higher intra-list diversity. For example, items from different artists.
- **Recommender persistence** – Sometimes, it is more effective to re-show recommendations than showing new items. There are several reasons for this. Users may ignore items when they are shown for the first time. May be they do not inspect the recommendations initially.
- **Privacy** – Recommender systems usually have to deal with privacy concerns because users have to reveal sensitive information.
- **User demographics** – User demographics may influence how satisfied users are with recommendations.
- **Robustness** – When users can participate in the recommender system, the issue of fraud must be addressed.
- **Serendipity** – Serendipity is a measure of how surprising the recommendations are. For instance, a recommender system that recommends milk to a customer in a grocery store might be perfectly accurate. But it is not a good recommendation because it is an obvious item for the customer to buy.
- **Trust** – A recommender system is of little value for a user if the user does not trust the system. Trust can be built by a recommender system by explaining how it generates recommendations, and why it recommends an item.
- **Labelling** – User satisfaction with recommendations may be influenced by the labelling of the recommendations.

# Dataset:

https://www.kaggle.com/datasets/saurav9786/amazon-product-reviews

 https://jmcauley.ucsd.edu/data/amazon/

**Approach**

**1) Rank Based Product Recommendation**

Objective -

- Recommend products with highest number of ratings.
- Target new customers with most popular products.
- Solve the [Cold Start Problem]

Outputs -

- Recommend top 5 products with 50/100 minimum ratings/interactions.

Approach -

- Calculate average rating for each product.
- Calculate total number of ratings for each product.
- Create a DataFrame using these values and sort it by average.
- Write a function to get 'n' top products with specified minimum number of interactions.

**2) Similarity based Collaborative filtering**

Objective -

- Provide personalized and relevant recommendations to users.

Outputs -

- Recommend top 5 products based on interactions of similar users.

Approach -

- Here, user_id is of object, for our convenience we convert it to value of 0 to 1539(integer type).
- We write a function to find similar users -
    1. Find the similarity score of the desired user with each user in the interaction matrix using cosine_similarity and append to an empty list and sort it.
    2. extract the similar user and similarity scores from the sorted list
    3. remove original user and its similarity score and return the rest.
- We write a function to recommend users -
    1. Call the previous similar users function to get the similar users for the desired user_id.
    2. Find prod_ids with which the original user has interacted -> observed_interactions
    3. For each similar user Find 'n' products with which the similar user has interacted with but not the actual user.
    4. return the specified number of products.

**3) Model based Collaborative filtering**

Objective -

- Provide personalized recommendations to users based on their past behavior and preferences, while also addressing the challenges of sparsity and scalability that can arise in other collaborative filtering techniques.

Outputs -

- Recommend top 5 products for a particular user.

Approach -

- Taking the matrix of product ratings and converting it to a CSR(compressed sparse row) matrix. This is done to save memory and computational time, since only the non-zero values need to be stored.
- Performing singular value decomposition (SVD) on the sparse or csr matrix. SVD is a matrix decomposition technique that can be used to reduce the dimensionality of a matrix. In this case, the SVD is used to reduce the dimensionality of the matrix of product ratings to 50 latent features.
- Calculating the predicted ratings for all users using SVD. The predicted ratings are calculated by multiplying the U matrix, the sigma matrix, and the Vt matrix.
- Storing the predicted ratings in a DataFrame. The DataFrame has the same columns as the original matrix of product ratings. The rows of the DataFrame correspond to the users. The values in the DataFrame are the predicted ratings for each user.
- A funtion is written to recommend products based on the rating predictions made :
    1. It gets the user's ratings from the interactions_matrix.
    2. It gets the user's predicted ratings from the preds_matrix.
    3. It creates a DataFrame with the user's actual and predicted ratings.
    4. It adds a column to the DataFrame with the product names.
    5. It filters the DataFrame to only include products that the user has not rated.
    6. It sorts the DataFrame by the predicted ratings in descending order.
    7. It prints the top num_recommendations products.
- Evaluating the model :
    1. Calculate the average rating for all the movies by dividing the sum of all the ratings by the number of ratings. 2, Calculate the average rating for all the predicted ratings by dividing the sum of all the predicted ratings by the number of ratings.
    2. Create a DataFrame called rmse_df that contains the average actual ratings and the average predicted ratings.
    3. Calculate the RMSE of the SVD model by taking the square root of the mean of the squared errors between the average actual ratings and the average predicted ratings.
1. 

### **Hybrid Recommendation System**

**Objective:**

To recommend top 5 products for a given `user_id` by combining multiple techniques to handle both new and existing users effectively.

---

### **Approach**

### **1. Check User Status: New or Existing**

- Query the interaction matrix or dataset to determine if the user has interacted with any product.
- **New User:** No interactions exist.
- **Existing User:** At least one interaction exists.

### **2. Recommendation Strategy**

- **For New Users (Cold Start):**
Use **Rank-Based Product Recommendation** to recommend the most popular products.
    - Compute the average ratings and total number of ratings for all products.
    - Filter products with at least a specified minimum number of interactions (e.g., 50 or 100).
    - Return the top 5 products based on the highest average rating.
- **For Existing Users:**
Use a combination of **Similarity-Based Collaborative Filtering** and **Model-Based Collaborative Filtering**:
    
    **a. Similarity-Based Filtering:**
    
    - Identify similar users based on interaction data using cosine similarity.
    - Extract the products these similar users have interacted with but the target user hasn't.
    - Rank these products based on frequency or similarity scores.
    
    **b. Model-Based Filtering (SVD):**
    
    - Use the SVD-based predicted ratings to suggest products the user hasn’t interacted with.
    - Rank the products by the predicted rating.
    
    **c. Combine Results:**
    
    - Take the union of product recommendations from the similarity-based and model-based approaches.
    - Rank these products based on predicted ratings or interaction frequency and select the top 5.

```python
def hybrid_recommendation(user_id, interaction_matrix, product_info, min_interactions=50):
    if user_id not in interaction_matrix.index:
        # New user: Use rank-based recommendation
        return rank_based_recommendation(product_info, min_interactions)
    
    # Existing user: Use collaborative approaches
    similarity_recommendations = similarity_based_recommendation(user_id, interaction_matrix)
    svd_recommendations = model_based_recommendation(user_id, interaction_matrix)
    
    # Combine and rank recommendations
    hybrid_recs = pd.concat([similarity_recommendations, svd_recommendations]).drop_duplicates()
    hybrid_recs = hybrid_recs.sort_values(by="predicted_rating", ascending=False)
    
    return hybrid_recs.head(5)

```
