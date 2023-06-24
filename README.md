# greenScreenRemover

This Python script that utilizes the OpenCV library to perform green screen removal in videos.
Installation

    Clone the repository or download the source code files.
    Ensure that Python and the required dependencies are installed (OpenCV, NumPy).
    Place the video file (in MP4 format) you want to process in the same directory as the script.
    Optionally, provide a background image file (in JPEG or PNG format) for replacing the green screen.

Usage

    Open a terminal or command prompt.

    Navigate to the directory where the script is located.

    Run the script using the following command:

    python green_screen.py

    The script will open a video player window showing the original video and a separate window showing the processed video with the green screen removed.

    To quit the script, press the 'Esc' key or close the video player window.

Configuration

You can customize the green color range by modifying the following lines of code in the script:

python

l_green = np.array([0, 0, 100], dtype=np.uint8)
u_green = np.array([200, 200, 255], dtype=np.uint8)

Adjust the values in the l_green and u_green arrays to define the lower and upper bounds of the green color range.
Dependencies

The Plugin Name relies on the following dependencies:

    Python 3.x
    OpenCV (4.7.0 or higher)
    NumPy

Make sure these dependencies are installed before running the script.
Examples

Here are some examples of how to use the Plugin Name script:

    Basic Usage:

python green_screen.py

This will process the video named "v.mp4" in the same directory, using the default green color range and no background image.

Custom Green Color Range:

python

    l_green = np.array([0, 100, 0], dtype=np.uint8)
    u_green = np.array([100, 255, 100], dtype=np.uint8)

    Modify the l_green and u_green arrays to define a custom green color range.

    Background Image:

    Place a background image file named "bg.jpg" in the same directory as the script. The background image will replace the green screen in the processed video.

Contributions

Contributions to the Plugin Name project are welcome. If you have any bug fixes, improvements, or new features to suggest, please create a pull request on th
