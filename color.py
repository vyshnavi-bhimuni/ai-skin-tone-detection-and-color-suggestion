import cv2
import numpy as np
import pandas as pd
from math import sqrt

skin_tone_data = pd.read_csv("skin_tone_dataset.csv")
suitable_color_data = pd.read_csv("suitable_colors.csv")
color_map = pd.read_csv("color_rgb_map.csv")
def get_nearest_skin_tone(avg_rgb):
    min_dist = float("inf")
    matched_tone = None
    for _, row in skin_tone_data.iterrows():
        dist = sqrt((avg_rgb[0] - row["R"]) ** 2 +
                    (avg_rgb[1] - row["G"]) ** 2 +
                    (avg_rgb[2] - row["B"]) ** 2)
        if dist < min_dist:
            min_dist = dist
            matched_tone = row["SkinTone"]
    return matched_tone


def get_suitable_colors(skin_tone):
    row = suitable_color_data[suitable_color_data["SkinTone"] == skin_tone]
    if not row.empty:
        return row.iloc[0]["SuitableColors"].split(",")
    return ["No match found"]
def get_color_rgb(color_name):
    row = color_map[color_map["ColorName"].str.lower() == color_name.strip().lower()]
    if not row.empty:
        return (int(row.iloc[0]["R"]), int(row.iloc[0]["G"]), int(row.iloc[0]["B"]))
    else:
        return (255, 255, 255)  
cap = cv2.VideoCapture(0)
cv2.namedWindow("Skin Tone Color Suggestion")

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    if not ret:
        break

    
    h, w, _ = frame.shape
    x1, y1, x2, y2 = w // 2 - 75, h // 2 - 75, w // 2 + 75, h // 2 + 75
    roi = frame[y1:y2, x1:x2]

    
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

    
    avg_color = np.average(np.average(roi, axis=0), axis=0)
    avg_rgb = (int(avg_color[2]), int(avg_color[1]), int(avg_color[0]))

    
    skin_tone = get_nearest_skin_tone(avg_rgb)
    suggested_colors = get_suitable_colors(skin_tone)


    cv2.putText(frame, f"Skin Tone: {skin_tone}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(frame, "Suggested Colors:", (10, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    
    start_x = 10
    start_y = 90
    rect_w = 90
    rect_h = 40
    spacing = 15

    for i, color_name in enumerate(suggested_colors[:4]):
        rgb = get_color_rgb(color_name)
        top_left = (start_x + i * (rect_w + spacing), start_y)
        bottom_right = (top_left[0] + rect_w, top_left[1] + rect_h)
        cv2.rectangle(frame, top_left, bottom_right, rgb[::-1], -1)
        cv2.putText(frame, color_name.strip(), (top_left[0] + 5, bottom_right[1] + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


    cv2.imshow("Skin Tone Color Suggestion", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()