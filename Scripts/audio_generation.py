from yapper import PiperSpeaker, PiperVoiceUS
import torch
from TTS.api import TTS



class TextToSpeech:
    """
    A class to convert text to speech using different TTS software.
    Attributes:
    -----------
    text : str
        The text to be converted to speech.
    software : str, optional
        The TTS software to use (default is 'coqui').
    Methods:
    --------
    piper_to_speech(title):
        Converts text to speech using Piper TTS and saves it as a .wav file.
    coqui_to_speech(title):
        Converts text to speech using Coqui TTS and saves it as a .mp3 file.
    """
    def __init__(self, text, software='coqui'):
        self.text = text
        self.software = software

    def piper_to_speech(self, title):
        tts = PiperSpeaker(voice=PiperVoiceUS.LIBRITTS_R)
        tts.text_to_wave(f'{self.text}', f'{title}.wav')
        print('done converting!')
    
    def coqui_to_speech(self, title):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2').to(device)
        tts.tts_to_file(
        text = self.text,
        speaker="Claribel Dervla",
        language="en",
        file_path=f'{title}.mp3'
        )
        print('done converting!')