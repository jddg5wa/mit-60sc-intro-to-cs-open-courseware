# 🧩 Problem Set 10: Clustering

## Introduction

In Problem Set 10, you will be using k-means clustering to process and analyze data from the United States Census. The goal is to apply k-means clustering to group data points (representing counties) into clusters based on certain features. We will analyze the clustering results and examine prediction errors to understand how well the algorithm performs.

## Problem 0: Provided Classes and Functions

The problem set provides several classes and functions to help you implement k-means clustering. These include `Point`, `County`, and `Cluster` classes, along with functions like `kmeans()`, `readCountyData()`, `buildCountyPoints()`, and `randomPartition()`. You should familiarize yourself with these provided elements before proceeding with the problems.

## Problem 1: Graphing Removed Error

In this problem, you will graph the total error produced by the `kmeans()` function for different values of k. You will partition the data set into training and holdout sets, then calculate the total error for each set. Finally, you will plot the training and holdout errors against k and also graph the ratio of holdout error to total training error.

## Problem 2: k-means and You

In this problem, you will run k-means three times with k = 50 and examine the cluster that contains your home county (or a county of your choice). You will observe whether your county clusters with the same counties each time and analyze whether it is in an appropriate cluster.

## Problem 3: Graphing Prediction Error

Here, you will set the weight of the Poverty feature to 0 and the weights of other features to 1 in the `County` class. Then, you'll partition the data into training and holdout sets and apply k-means clustering to the training set. For each point in the holdout set, you will calculate the error between the predicted and actual poverty values and graph this error against k.

## Problem 4: Graphing Prediction Error (AGAIN!)

In this final problem, you will explore the effect of changing weight vectors on prediction errors. You'll find a weight vector that reduces error compared to Problem 3 and another weight vector with values between 0 and 1 that further improves the results. For each weight vector, you will graph the prediction error against k and provide explanations for the observed results.

By completing this problem set, you will gain experience with k-means clustering and its application to real-world data. Have fun with the experiments and analysis, and good luck with the coding!




**Please note that these projects are a part of the MIT OpenCourseWare and follow their guidelines for collaboration and time spent on the problems.**

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).