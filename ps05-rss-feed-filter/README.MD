# 🧩 Problem Set 5: RSS Feed Filter

## Introduction

In problem set 5, you will build a program to monitor news feeds over the Internet. Your program will filter the news, alerting the user when it notices a news story that matches that user’s interests (for example, the user may be interested in a notification whenever a story related to the Red Sox is posted).

This problem set involves creating a filtering system for news stories. We will define different types of triggers that can match specific words or phrases in the subject, title, or summary of a news story. These triggers will be combined to create more complex filtering rules.

The goal is to implement a filtering system that reads a trigger configuration from a `triggers.txt` file and then uses these triggers to filter out relevant news stories. The user can define the triggers they are interested in, and the program will display only the news stories that match the specified triggers.

The problem set is divided into several parts:

## Part I: Data Structure Design

In Part I, we will define a data structure to represent a news story. We will create a class called `NewsStory` that will store information about each news item, including a globally unique identifier (GUID), title, subject, summary, and link to more content. The `NewsStory` class will have methods to retrieve these pieces of information.

## Part II: Triggers

In Part II, we will implement different types of triggers. Triggers are conditions that will be evaluated against a news story, and if the condition is met, the trigger will fire an alert. We will start with word triggers, such as `TitleTrigger`, `SubjectTrigger`, and `SummaryTrigger`, which will fire if a specific word is present in the title, subject, or summary of a news story, respectively. We will also implement composite triggers, such as `NotTrigger`, `AndTrigger`, and `OrTrigger`, which will combine multiple triggers to create more complex alert rules.

## Part III: Filtering

In Part III, we will create a function called `filter_stories` that takes a list of news stories and a list of triggers as input. It will return only the news stories for which at least one trigger fires an alert. This function will be used to filter the news stories based on the user-defined triggers.

## Part IV: User-Specified Triggers

In Part IV, we will allow the user to specify the triggers they are interested in by reading the trigger configuration from a `triggers.txt` file. The `readTriggerConfig` function will parse the file and create the corresponding triggers. The `main_thread` function will then use these triggers to filter the news stories.

By completing all the parts of this problem set, you will have built a news filtering system that allows users to receive notifications for news stories that match their interests, as specified in the `triggers.txt` file. Enjoy the challenge, and happy coding!

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).
