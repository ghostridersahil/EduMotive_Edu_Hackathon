from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular_events.pkl', 'rb'))
Date=(list(popular_df['Date'].values))
for i in range(len(Date)):
    print(Date[i])