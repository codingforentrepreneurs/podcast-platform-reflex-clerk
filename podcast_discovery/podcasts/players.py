import reflex as rx


def podcast_audio_player(podcast_data:dict, key:str="episodeUrl"):
    episode_url_value = podcast_data.get(key)
    return rx.cond(
        episode_url_value,
        rx.audio(url=episode_url_value, width="150px", height="32px"),
        "No audio found"
    )


def podcast_video_player(podcast_data:dict, key:str="episodeUrl"):
    episode_url_value = podcast_data.get(key)
    return rx.cond(
        episode_url_value,
        rx.video(url=episode_url_value, width="350px", height="150px"),
        "No video found"
    )