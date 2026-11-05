[README.md](https://github.com/user-attachments/files/34409795/README.md)
# Voice Assistant

A Python-based voice assistant project focused on working with spoken input. The repository includes a speech-recognition module and Jupyter notebooks for experimenting with the project workflow and its supporting data.

## Features

- Captures audio from the computer's microphone.
- Uses the `SpeechRecognition` library with Google's speech-recognition service.
- Configures recognition for Persian (`fa-IR`).
- Includes text-to-speech-related dependencies (`gTTS` and `playsound`) for audio output experiments.
- Provides Jupyter notebooks and TSV files used by the project.

> **Note:** The currently visible `functions.py` implements microphone capture and Persian speech recognition. The text-to-speech imports are present, but a complete text-to-speech workflow is not exposed in that file.

## Repository structure

```text
voice-assistant-/
├── functions.py
├── باز کردن.py
├── HowToUse (1).ipynb
├── Untitled1_(1).ipynb
├── dementional (2).ipynb
├── heab (1).ipynb
├── metadata.tsv
└── vectors.tsv
```

- **`functions.py`** — microphone input and Persian speech recognition.
- **`HowToUse (1).ipynb`** — notebook containing usage and experimentation material.
- **Other notebooks** — additional experiments and project development.
- **`metadata.tsv` / `vectors.tsv`** — supporting tabular data files used in the notebook workflow.
- **`باز کردن.py`** — an additional Python script.

## Requirements

- Python 3
- A working microphone
- Internet connection for Google's online speech-recognition service
- The Python packages used by the speech module:

```bash
pip install SpeechRecognition gTTS playsound
```

`SpeechRecognition` needs a microphone input backend. Depending on your operating system and Python version, you may also need to install and configure **PyAudio** separately.

For notebook-based work, install Jupyter:

```bash
pip install notebook
```

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/arianshakoo/voice-assistant-.git
   cd voice-assistant-
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies listed above and configure the microphone backend.

4. Run the speech-recognition script:

   ```bash
   python functions.py
   ```

   When prompted by the program's execution flow, speak into the microphone. The recognizer is configured for Persian (`fa-IR`) and prints the recognized text.

5. To explore the notebooks, start Jupyter:

   ```bash
   jupyter notebook
   ```

   Then open `HowToUse (1).ipynb` and run its cells in order.

## How the speech-recognition module works

The `get_audio()` function in `functions.py`:

1. Creates a `Recognizer` instance.
2. Opens the default microphone as the audio source.
3. Records audio from the microphone.
4. Sends the recorded audio to Google's recognition service with the `fa-IR` language setting.
5. Prints and returns the recognized text. If recognition fails, it prints the exception and returns an empty string.

## Troubleshooting

- **Microphone errors:** Check your operating system's microphone permissions and make sure a microphone is connected and selected.
- **PyAudio installation issues:** Install a compatible microphone backend for your operating system and Python version.
- **Recognition errors:** Check your internet connection and speak clearly in Persian.
- **Notebook errors:** Run the notebook cells in order and install any additional packages reported as missing.

## Limitations

- Speech recognition relies on an online Google service, so an internet connection is required.
- Recognition quality can vary with microphone quality, background noise, and speaking style.
- The repository contains experimental notebooks; their dependencies and execution order may differ from the minimal speech-recognition module.

## Contributing

Suggestions, bug reports, and improvements are welcome. Feel free to open an issue or submit a pull request.

## License

No license file is currently specified in the repository. Unless a license is added, the project should be treated as having all rights reserved.
