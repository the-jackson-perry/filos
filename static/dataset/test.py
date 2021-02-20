#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:50:31 2021

@author: erik
"""
import pandas as pd

df = pd.read_csv("./anxiety.csv")
df = df[ df["Phase"] == "1" ]
df = df.rename(columns= {'Low CI':"Low_CI", "High CI": "High_CI", "Time_Period Label": "Time", "Time Period": "Time_Period"})

Depressive = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "National Estimate" ]
national_Depressive.to_csv("national_depression.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "National Estimate" ]
national_Depressive.to_csv("national_anxiety.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By Age" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 1]
national_Depressive.to_csv("national_depression_by_age_1.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By Age" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 1]
national_Depressive.to_csv("national_anxiety_by_age_!.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By Age" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 12]
national_Depressive.to_csv("national_depression_by_age_12.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By Age" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 12]
national_Depressive.to_csv("national_anxiety_by_age_12.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By State" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 12]
national_Depressive.to_csv("national_depression_by_state_12.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By State" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 12]
national_Depressive.to_csv("national_anxiety_by_state_12.csv", index=False)

Depressive = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
print(Depressive)
national_Depressive = Depressive[Depressive["Group"] == "By State" ]
print(national_Depressive)
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 1]
print(national_Depressive)
national_Depressive.to_csv("national_depression_by_state_1.csv", index=False)


Depressive = df[df["Indicator"] == "Symptoms of Anxiety Disorder"]
national_Depressive = Depressive[Depressive["Group"] == "By State" ]
national_Depressive = national_Depressive[national_Depressive["Time_Period"] == 1]
national_Depressive.to_csv("national_anxiety_by_state_1.csv", index=False)