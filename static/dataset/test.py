#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:50:31 2021

@author: erik
"""
import pandas as pd

df = pd.read_csv("./anxiety.csv")
df = df[ df["Phase"] == "1" ]

depression = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_depression = depression[depression["Group"] == "National Estimate" ]
national_depression.to_csv("national_depression.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_depression = depression[depression["Group"] == "National Estimate" ]
national_depression.to_csv("national_anxiety.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Depression Disorder"]
national_depression = depression[depression["Group"] == "By Age" ]
national_depression = national_depression[national_depression["Time Period"] == 1]
national_depression.to_csv("national_depression_by_age_1.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_depression = depression[depression["Group"] == "By Age" ]
national_depression = national_depression[national_depression["Time Period"] == 1]
national_depression.to_csv("national_anxiety_by_age_!.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Depression Disorder"]
national_depression = depression[depression["Group"] == "By Age" ]
national_depression = national_depression[national_depression["Time Period"] == 12]
national_depression.to_csv("national_depression_by_age_12.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_depression = depression[depression["Group"] == "By Age" ]
national_depression = national_depression[national_depression["Time Period"] == 12]
national_depression.to_csv("national_anxiety_by_age_12.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Depression Disorder"]
national_depression = depression[depression["Group"] == "By State" ]
national_depression = national_depression[national_depression["Time Period"] == 12]
national_depression.to_csv("national_anxiety_by_state_12.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_depression = depression[depression["Group"] == "By State" ]
national_depression = national_depression[national_depression["Time Period"] == 12]
national_depression.to_csv("national_anxiety_by_state_12.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Depression Disorder"]
national_depression = depression[depression["Group"] == "By State" ]
national_depression = national_depression[national_depression["Time Period"] == 1]
national_depression.to_csv("national_anxiety_by_state_1.csv", index=False)

depression = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_depression = depression[depression["Group"] == "By State" ]
national_depression = national_depression[national_depression["Time Period"] == 1]
national_depression.to_csv("national_anxiety_by_state_1.csv", index=False)