## [Platform AI - Recommending Members](https://www.topcoder.com/challenges/340ebf70-3031-49f0-a080-40a0a0fe5296?tab=details)
- Challenge aims to build a core program/system which can recommend a list of members for a particular challenge or task.

## Tech Stack
- [Anaconda Python3](https://www.anaconda.com/distribution/)

## Deployment:
```CMD
cd /path/to/requirements.txt
pip install -r requirements.txt
```

## SOLUTION RUN
```CMD
python cli.py
```

## CLI ARGUMENTS 
--member_dir_path - Member Profile JSON Path
--challenge_dir_path - Challenge Profile JSON Path

- default folder path is the `data` directory inside the submission Just place the required two profile JSON inside this
- currently has a small part of the dataset for testing purpose.

# Solution Approach
1. Take an intersection of skills present in both challenges and member profile
2. Calculate the similarity score between this intersection by taking an average of skill confidence present for those members which have a valid skills in that slice. - This make sure the a member that have a rich profile with multiple skills sets get a better recommendation.
3. Provide a rating threshold using a predefined scale
4. Use this rating to train a SVD recommender model based on collaborative filtering between Member and Challenge Profile
5. Used the trained model of prediction
6. AN SVD(Singular value decomposition) algorithm is used for training that provides a way to factorize a matrix, into singular vectors and singular values. The SVD allows us to discover some of the same kind of information as the eigen decomposition
7. For better understanding on training and testing please refer to Training and Testing Jupyter notebooks.