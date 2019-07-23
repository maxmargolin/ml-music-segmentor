"""
build model
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import dl
import compare
import extractor
import hard_coded_times

video_starts = hard_coded_times.get_data_with_just_start()
Xs = []
Ys = []
filename1 = "og"
filename2 = "lyrical"

# nameless= {"peak":[],"diff":[]}
claim = [33]
ha = [["XNtTEibFvlQ", 33],
        ["rJYcmq__nDM", 33],
        ["xb06CqeSgCQ", 33],
        ["cVoiniG5q5k", 33],
        ["eP4eqhWc7sI", 33],
        ["M97vR2V4vTs", 33],
        ["Ys7-6_t7OEQ", 34],
        ["i41qWJ6QjPI", 34]]
for video_start in ha:
    try:
        video_id = video_start[0]
        real_start = video_start[1]
        dl.do_downloads(filename1, filename2, video_id=video_id)
        corr_array, peak = compare.get_correlation_features()
        duration1, duration2 = compare.get_lengths()
        # print("duration1, duration2", duration1, duration2)

        ser = extractor.get_nearby_up_down(filename1 + ".mp3", claim[0])
        combined = np.append([peak, duration1 - duration2,claim[0]], ser)
        Xs.extend([combined])
        # nameless["duration1"].append(duration1)
        # nameless["duration2"].append(duration2)
        # nameless["peak"].append(peak)
        # nameless["diff"].append(duration1-duration2)
        Ys.append(True)
    except Exception as ex:
        print(ex)

print(Xs, Ys)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
