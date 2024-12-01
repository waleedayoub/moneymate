# Money Mate - Your Friendly LLM Financial Management Agent

## Project Description
- The goal of Money Mate is to help look over your historical personal financial transactions and allow you to get advice via natural language
- This is a RAG (retrieval augmented generation) application and the primary dataset it will use to augment its responses will be extracted from (Monarch)[https://www.monarchmoney.com/]
### What is Monarch Money?
Monarch Money is a financial management app that allows users to track all their accounts, transactions, and investments in one place. It provides tools for budgeting, goal tracking, investment monitoring, and net worth tracking. The platform syncs with over 11,200 financial institutions and offers AI-powered transaction categorization, customizable dashboards, and financial planning features. It is a paid service with a 7-day free trial and options for monthly or annual subscriptions​
  - ![alt text](image.png)

- This app will function by allowing you to either upload an extract from Monarch Money (or alternatively, any csv file that fits the same or similar schema)
  - See [Step 1a - Data upload](#step-1a---data-upload) in the section below for instructions on how to do this
- The preferred but slightly more complicated way to inject your own data is to login via the Monarch Money API
  - Details on that API can be found here: https://github.com/hammem/monarchmoney and is covered in detail in [Step 1b - Using the API](#step-1b---using-the-api) below
- Once your data is uploaded, you can then proceed to interrogate your own financial patterns in the past
  - Depending on the breadth and history of data you've provided, you can ask questions like: What is my net worth? What are the categories I spend the most in? If I wanted to save an additional $500 per month, can you recommend 3 things I can do?

TODO things for the future
- Integrate with the [Wealthsimple Trade API](https://github.com/ahmedsakr/wstrade-api/tree/main/docs) and assist with investment advice, not just financial spending advice
- Integrate with other financial management apps

## Architecture

## Deployment Instructions
### Technologies used
### Things you need to have installed
### How to deploy
#### Step 1a - Data upload
#### Step 1b - Using the API
