# Mental Health in the Tech Industry Data Analysis

## Overview
This project involves the extraction, cleaning, and exploratory data analysis (EDA) of survey data related to mental health in the tech industry. The data is sourced from the Open Source Mental Illness (OSMI) survey conducted in multiple years (2014, 2016, 2017, 2018, and 2019). The goal of this analysis is to gain insights into the mental health landscape within the tech industry, identify factors influencing mental health, and propose potential areas of improvement for mental health support.

## Table of Contents
- [Data Extraction and Preparation](#data-extraction-and-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Sentiment Analysis](#sentiment-analysis)
- [Recommendations](#recommendations)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Data Extraction and Preparation
- The data is sourced from [OSMI survey data](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry).
- It is organized into three tables: Survey, Question, and Answer.
- Data cleaning is performed to handle missing values and ensure data consistency.

## Exploratory Data Analysis (EDA)
- EDA is conducted to gain insights into mental health trends in the tech industry.
- Factors such as age, gender and race are analyzed.
- Visualizations and statistical tests are used to examine relationships between variables.

## Sentiment Analysis
- Sentiment analysis is performed on responses regarding how to improve mental health support in the workplace.
- Common topics and sentiment trends are identified.
- Positive and negative sentiments are categorized.

## Recommendations
- Based on the analysis, the following recommendations are made:
  - Enhancing training or informal meetings on mental health topics.
  - Providing resources and support for specific groups.
  - Addressing the prevalence of mental health disorders.
  - Improving work-life balance and reducing stigma.

## General Summary
Demographics: We explored the demographic characteristics of survey respondents, including age, gender and race. Notably, females tended to report higher rates of mental health disorders than males, and people of color reported higher rates of mental health disorders than white people.

Mental Health Disorders: A significant portion of respondents reported being diagnosed with mental health disorders. We observed variations in diagnosis rates based on gender and race, but not by age.

Support Measures: We investigated the impact of mental health support measures such as benefits, resources, chats with coworkers and available support. Our findings revealed that the majority of respondents were not aware of these support measures, but - in proportion - more females than males answered 'Yes' to having received mental health benefits and having chats with coworkers.

Sentiment Analysis: An analysis of open-ended responses regarding improvements in mental health support showed an overall positive sentiment marked by a majority of respondents.

In conclusion, this analysis provides insights into the state of mental health in the workplace. The findings suggest that there is room for improvement in how tech companies provide mental health support, benefits and resources, especially to females and people of color. These insights can guide efforts to enhance mental health support and create a more inclusive work environment.

However, a pivotal point that needs to be addressed is the fact that this is all self-reported data, that is heavily skewed towards a single subset of the population, and is thus less valid for making claims than more representative data.

## Potential Improvements
Some aspects that could be improved on this analysis:

- Machine Learning Models: Machine learning models can be used for predictive analysis. The models can try to predict mental health outcomes or identify patterns in mental health support needs.

- Additional Data Sources: Incorporate additional data sources to enrich your analysis. External data, such as economic indicators or job market trends, can provide more context for your findings.

- Natural Language Processing (NLP): Expand the sentiment analysis by applying more advanced NLP techniques, such as topic modeling or sentiment analysis on specific demographics or groups.

- Data Updates: The last year available of data is from 2019. 

For more information, feel free to [email me](mailto:alessionespoli.97@gmail.com).

## Getting Started
To replicate this analysis, follow these steps:

### Dependencies
- Python (3.x)
- Required Python libraries (NumPy, pandas, seaborn, nltk, wordcloud, etc.) are shown in the `requirements.txt` file

### Usage
1. Clone this repository.
2. Install the required dependencies through the `requirements.txt` file
3. Run the provided Python scripts in the order specified.

## License
This project is licensed under the [MIT License](LICENSE).


