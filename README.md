# RealTimeYOLO
# Project Setup Guide

## Prerequisites
- Git installed on your system
- Python and pip installed
- Webcam (built-in or external)

## Installation Steps

1. Clone the repository
```bash
git clone <[repository_url](https://github.com/Yair-fartouh/RealTimeYOLO.git)>
cd <project_directory>
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Connect your webcam to your computer
- Windows: System will automatically install necessary drivers
- Linux: System should recognize the webcam automatically
- macOS: Grant camera permissions when prompted

4. Configure camera settings:
- Open your code and locate:
```python
cap = cv2.VideoCapture(1)
```
- Change the camera index:
  - `0`: Built-in webcam/single camera setup
  - `1`: External webcam (for multiple cameras)

5. Run the application
```bash
python main.py
```

## Troubleshooting

If you encounter issues:
- For camera detection problems, try different index values (0, 1, 2)
- Ensure all dependencies are properly installed
- Check if your system has proper camera permissions
- Make sure no other application is currently using the webcam

## Contact

For additional support, please open an issue in the repository.
