import os
import threading
from fastapi import APIRouter, File, UploadFile

from helpers.audio.audio_playback_helper import AudioPlaybackHelper
from middleware.auth import require_auth
import tempfile

router = APIRouter()


@router.post("/play-audio")
async def play_audio(token: str = require_auth(), file: UploadFile = File(...)):
    """
    Endpoint to play a sound file.
    Expects an audio file upload.
    """

    # Store in temporary file using tempfile module
    content = await file.read()

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content)
        temp_file_path = temp_file.name

        def play_file():
            try:
                AudioPlaybackHelper.play_audio(temp_file_path)
            finally:
                os.remove(temp_file_path)

        threading.Thread(target=play_file, daemon=False).start()

    return {"status": "playback_started"}
