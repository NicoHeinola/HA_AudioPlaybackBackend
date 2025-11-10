import os
from fastapi import APIRouter, Body, Response

from helpers.audio.audio_playback_helper import AudioPlaybackHelper
from middleware.auth import require_auth

router = APIRouter()


@router.post("/play-audio")
def play_audio(token: str = require_auth(), body: dict = Body(...)):
    """
    Endpoint to play a sound file.
    Expects raw audio data in the request body.
    """

    # Store in temporary file
    temp_file_path: str = os.path.join("/tmp", "temp_audio_file")
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(body.get("audio_data", b""))

    try:
        AudioPlaybackHelper.play_audio(temp_file_path)
    finally:
        os.remove(temp_file_path)

    return {"status": "playback_started"}
