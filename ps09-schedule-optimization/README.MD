# 🧩 Problem Set 9: Schedule Optimization

## Introduction

In Problem Set 9, you will be tasked with implementing optimization algorithms for course scheduling at an institute of higher education. The goal is to help students select a list of subjects that maximizes their learning value while staying within the constraints of their available study hours. We'll explore two different approaches: a greedy algorithm and a brute force algorithm.

## Problem 1: Building A Subject Dictionary

To start, you need to create a data structure to represent the subjects. The subjects will be read from a file named `subjects.txt`, where each line contains information about a subject in the format "name,value,work". You will implement the `loadSubjects` function, which reads the file and returns a dictionary mapping subject names to tuples of (value, work), where value and work are integers representing the learning value and required study hours for each subject, respectively.

## Problem 2: Subject Selection By Greedy Optimization

In this part, you will implement a greedy algorithm called `greedyAdvisor`. The algorithm will use a comparator function to pick the "best" subjects based on different criteria (value, work, or value/work ratio). The function will take a dictionary of subjects, a maximum work limit, and a comparator function as inputs. It will return a dictionary of selected subjects that maximizes the learning value without exceeding the work limit.

## Problem 3: Subject Selection By Brute Force

Next, you will implement a brute force algorithm named `bruteForceAdvisor`. The goal is to find the globally optimal selection of subjects using a brute force approach. The function will take a dictionary of subjects and a maximum work limit as inputs and return a dictionary of subjects representing the best possible selection.

## Problem 4: Efficiency Analysis

In this part, you will analyze the algorithmic complexity of both `greedyAdvisor` and `bruteForceAdvisor`. You'll also estimate the time it would take for `bruteForceAdvisor` to find optimal solutions for various numbers of subjects. The analysis will be documented in the `ps9_writeup.pdf` file.

By completing this problem set, you will have developed two different algorithms to help students optimize their course schedules based on their learning objectives and available study hours. Enjoy the problem-solving process and happy coding!

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).