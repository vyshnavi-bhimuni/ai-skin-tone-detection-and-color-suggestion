# AI-Based Skin Tone Detection and Color Suggestion

## Overview

This project is a Python-based application that detects a user's skin tone using OpenCV and recommends suitable clothing colors based on dataset-driven color analysis. The application captures live video through a webcam, analyzes the skin tone using RGB values, and displays personalized color recommendations in real time.

---

## Features

- Real-time webcam-based skin tone detection
- RGB color analysis
- Dataset-driven skin tone classification
- Personalized clothing color recommendations
- Live display of suggested colors
- Simple and user-friendly interface

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Pandas

---

## Dataset Files

- **skin_tone_dataset.csv** – Stores predefined skin tone RGB values.
- **color_rgb_map.csv** – Maps color names to RGB values.
- **suitable_colors.csv** – Stores suitable clothing colors for each skin tone.

---

## Project Structure

```text
color.py
skin_tone_dataset.csv
color_rgb_map.csv
suitable_colors.csv
README.md
```

---

## How to Run

1. Clone or download this repository.

2. Install the required libraries:

```bash
pip install opencv-python pandas numpy
```

3. Ensure all CSV files are in the same folder as `color.py`.

4. Run the program:

```bash
python color.py
```

5. Allow webcam access.

6. Place your face or hand inside the rectangle displayed on the screen.

7. The application detects your skin tone and displays suitable clothing color recommendations.

8. Press **Q** to exit the application.

---

## Applications

- Personal styling assistance
- Clothing color recommendation
- Fashion technology
- Computer vision applications

---

## Future Enhancements

- Improved skin tone classification
- Support for multiple face detection
- Mobile application integration
- More personalized recommendations

---

## Author
VYSHNAVI BHIMUNI
