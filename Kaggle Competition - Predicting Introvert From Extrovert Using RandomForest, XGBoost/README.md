# 🧠 Personality Prediction: Introvert vs Extrovert (Kaggle Playground S5E7)

This project predicts whether a person is an **Introvert** or **Extrovert** based on behavioral data such as time spent alone, stage fear, social interactions, and more. Built as part of the [Kaggle Playground Series - Season 5, Episode 7](https://www.kaggle.com/competitions/playground-series-s5e7/overview) competition.

---

## 📊 Problem Statement

The objective is to build a classifier that identifies personality type based on various social and personal behavioral traits.

---

## 📁 Dataset Overview

The dataset includes:

- `train.csv`: Labeled training data
- `test.csv`: Unlabeled test data (used for submission)
- `sample_submission.csv`: Format for Kaggle submission

### 🧾 Features
- `Time_spent_Alone`
- `Stage_fear`
- `Going_outside`
- `Drained_after_socializing`
- `Friends_circle_size`
- `Social_event_attendance`
- `Post_frequency`
- `Personality` (Target: Extrovert / Introvert)

---

## 🛠️ Approach

### 🔍 1. EDA & Preprocessing
- Identified missing values and imbalanced target
- Filled missing numerical features with **mean**, categorical with **mode**
- Used `LabelEncoder` for binary categorical features

### 🤖 2. Modeling
- Started with **RandomForestClassifier**
- Improved with **XGBoostClassifier** and used `scale_pos_weight` to address class imbalance
- Used `LabelEncoder` for target variable
- Tuned hyperparameters manually

### 🧪 3. Evaluation
- Evaluated using `classification_report` (Precision, Recall, F1)
- Validated using a **train-test split** (75% train, 25% test)

---

## 📈 Results

| Metric          | Validation Set |
|-----------------|----------------|
| Accuracy        | 62%            |
| Precision       | Extrovert: 74%, Introvert: 26% |
| Recall          | Extrovert: 75%, Introvert: 26% |
| Public Score on Kaggle | **0.972469** |

[Link to submission notebook](https://www.kaggle.com/code/ashutoshkaremore/predict-the-introverts-from-the-extroverts-v001?scriptVersionId=250444541)
