# Fish Detection

This repository contains the source code and resources for a Fish Detection application. The application is designed to process camera inputs, visualize graphs, and handle control switches using a graphical user interface (GUI).

## Project Structure

```
fishDetection/
├── CameraWidget.py      # Handles camera-related functionalities
├── graphWidget.py       # Manages graph visualization
├── main.py              # Entry point of the application
├── switches.py          # Handles switches and controls
├── icon/
│   ├── arrowIcon.png    # Icon for arrow functionality
│   └── cameraIcon.png   # Icon for camera functionality
```

## Features

- **CameraWidget**: Manages the camera input and related settings.
- **GraphWidget**: Displays graphical data visualizations.
- **Switches**: Provides control over various settings or parameters.
- **Main Application**: Integrates all components and serves as the entry point.

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.12.x
- Required Python libraries (install using the `requirements.txt` file if provided)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Djovie/fishDetection.git
   cd fishDetection
   ```

2. Install dependencies:
   ```bash
   pip install PyQt5
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Directory Explanation

### `CameraWidget.py`
Contains functions and classes to handle camera operations, including capturing frames and displaying live feed.

### `graphWidget.py`
Manages the creation and updating of graphs to display data visually.

### `main.py`
The main script to run the application, combining all components into a working GUI.

### `switches.py`
Implements various switch controls used in the GUI.

### `icon/`
Contains graphical assets used in the application:
- `arrowIcon.png`: The image on the drop-down button is used to select a camera.
- `cameraIcon.png`: The image that will appear if the camera is off.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore and modify the code to suit your needs!
