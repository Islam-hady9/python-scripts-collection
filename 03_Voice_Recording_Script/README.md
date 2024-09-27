# Voice Recording Script

This Python script allows you to record audio for a specified duration and save it as a WAV file.

## How It Works

The script records audio using your computer's microphone for a user-specified number of seconds and saves the recording in WAV format. By default, the sample rate is set to 44,100 Hz (CD quality), and the output is saved in the `Output` directory as `out.wav`.

### How the script operates:
1. The user is prompted to enter the recording duration in seconds.
2. The script records audio using the `sounddevice` library.
3. The recording is saved as a `.wav` file using the `scipy.io.wavfile` module.
4. The saved file can be found in the specified location (default: `Output\out.wav`).

## Example Use Case

You can use this script to:
- Record voice memos or interviews
- Capture sound for testing audio equipment
- Save quick audio notes directly from the command line

### Example:
To record a 5-second audio clip, simply run the script and provide the duration:

```bash
$ python voice_recording_script.py
Enter the time duration in seconds: 5
Recording...

Finished...
Recording saved as Output\out.wav
```

## Requirements

To run the script, you need the following libraries installed:

- `sounddevice`
- `scipy`

To install these dependencies, you can use the provided `requirements.txt` file. Run the following command:

```bash
pip install -r requirements.txt
```
