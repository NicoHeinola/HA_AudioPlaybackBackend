import os
from fastapi import APIRouter, File, UploadFile

from helpers.audio.audio_playback_helper import AudioPlaybackHelper
from middleware.auth import require_auth

router = APIRouter()


@router.post("/play-audio")
async def play_audio(token: str = require_auth(), file: UploadFile = File(...)):
    """
    Endpoint to play a sound file.
    Expects an audio file upload.
    """

    # Store in temporary file
    temp_file_path: str = os.path.join("/tmp", "temp_audio_file")
    with open(temp_file_path, "wb") as temp_file:
        content = await file.read()
        temp_file.write(content)

    try:
        AudioPlaybackHelper.play_audio(temp_file_path)
    finally:
        os.remove(temp_file_path)

    return {"status": "playback_started"}
