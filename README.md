# Django Video Creation App

## Overview

This Django application is designed to create video files from audio and a collection of images using the `moviepy` library. It provides a user-friendly interface to upload audio files, select a set of images, and generate a video with dynamic transitions.

## Features

- **Audio Upload:** Users can upload audio files in various formats (e.g., MP3, WAV).
  
- **Image Selection:** Users can select multiple images to be used in the video creation process.

- **Video Configuration:** Users can configure video settings such as duration, frame rate, and transition effects.

- **Preview:** Before generating the final video, users can preview the video with selected audio and images.

- **Download:** Once satisfied with the preview, users can download the generated video.

## Requirements

- Python 3.10.0
- Django 5.0.1
- moviepy library (`pip install moviepy`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/atifraza158/Audio-Opus-ToVideo.git
   cd Audio-Opus-toVideo
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Visit the application in your web browser.

2. Upload an audio file.

3. Select images to be used in the video.

4. Configure video settings.

5. Preview the video.

6. Download the final video.

## Contributing

Feel free to contribute to the development of this project by submitting issues or pull requests.


---
