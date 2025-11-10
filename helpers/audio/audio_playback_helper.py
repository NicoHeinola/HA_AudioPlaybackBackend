import playsound3


class AudioPlaybackHelper:
    @staticmethod
    def play_audio(
        file_path: str,
    ) -> bool:
        """
        Play an audio file located at file_path.
        Supports common audio formats like WAV, MP3, etc.
        """
        try:
            playsound3.playsound(file_path)
            return True
        except Exception as e:
            print(f"Error playing audio: {e}")
            return False