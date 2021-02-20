#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:50:31 2021

@author: erik
"""
import pandas as pd

df = pd.read_csv("./anxiety.csv")
depression = df[df["Indicator"] == "Symptoms of Depressive Disorder"]
national_depression = depression[depression["Group"] == "National Estimate"]

print(national_depression.head())