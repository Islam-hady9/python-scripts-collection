import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration, sample_rate=44100, filename=r"Output\out.wav"):
    """
    Records audio for a specified duration and saves it to a WAV file.

    Parameters:
        duration (int): The duration of the recording in seconds.
        sample_rate (int): The sample rate of the recording (default is 44100).
        filename (str): The name of the output file (default is "out.wav").
    """
    print("Recording...\n")

    # Record the audio with the specified duration and sample rate
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()  # Wait until the recording is finished

    # Save the recording as a WAV file
    write(filename, sample_rate, recording)

    print(f"Finished...\nRecording saved as {filename}")


if __name__ == "__main__":
    try:
        # Get the recording duration from the user
        duration = int(input("Enter the time duration in seconds: "))
        record_audio(duration)
    except ValueError:
        print("Invalid input! Please enter a valid number.")