from yapper import PiperSpeaker, PiperVoiceUS
from TTS.api import TTS

import random
import torch


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
    def __init__(self, text, software='coqui', speaker='random'):
        self.text = text
        self.software = software
        
        if speaker == 'random' and software == 'coqui':
            speakers = ['Claribel Dervla', 'Damian Black', 'Baldur Sanjin', 'Barbora MacLean', 'Alexandra Hisakawa', 'Adde Michal' ]
            self.speaker = random.choice(speakers)
        elif speaker == 'random' and software == 'piper':
            speakers = [PiperVoiceUS.LIBRITTS_R, PiperVoiceUS.NORMAN, PiperVoiceUS.RYAN, PiperVoiceUS.AMY, PiperVoiceUS.BRYCE]
            self.speaker = random.choice(speakers)
        else:
            self.speaker = speaker

    
    
    def piper_to_speech(self, title:str):
        """
        Converts the provided text to speech and saves it as a .wav file with the given title.
        Args:
            title (str): The title to be used for the output .wav file.
        Raises:
            ValueError: If the speaker is not set and cannot be randomly chosen.
        """
            
        tts = PiperSpeaker(voice=self.speaker)
        tts.text_to_wave(f'{self.text}', f'audio_files/{title}.wav')
        print('done converting!')
    
    def coqui_to_speech(self, title:str):
        """
        Converts text to speech using the Coqui TTS model and saves the audio to a file.

        Args:
            title (str): The title of the audio file to be saved (without extension).

        Returns:
            None

        Raises:
            RuntimeError: If the TTS model fails to generate speech.

        Notes:
            - The function uses a GPU if available, otherwise it falls back to the CPU.
            - The TTS model used is 'tts_models/multilingual/multi-dataset/xtts_v2'.
            - The language for the TTS is set to English ("en").
        """
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2').to(device)
        tts.tts_to_file(
        text = self.text,
        speaker=self.speaker,
        language="en",
        file_path=f'/audio_files/{title}.wav'
        )
        print('done converting!')
        
        @staticmethod
        def recommended_speakers():
            """
            Returns a list of recommended speakers for the Piper/Coqui TTS.

            Returns:
                list: A list of recommended speakers for the Piper/Coqui TTS.

            Example:
                recommended_speakers()
            """
            list_of_speakers = """
            Piper TTS:
            - LIBRITTS_R
            - NORMAN
            - RYAN
            - AMY
            - BRYCE
            
            NOTE: The speaker names must be passed in beginning with: PiperVoiceUS.speaker_name
            
            Coqui TTS:
            - Claribel Dervla
            - Damian Black
            - Baldur Sanjin
            - Barbora MacLean
            - Alexandra Hisakawa
            - Adde Michal
            
            If you would like to use one of these speakers, pass the speaker name when creating a new instance of the TextToSpeech class.
            
            """
            print(list_of_speakers)