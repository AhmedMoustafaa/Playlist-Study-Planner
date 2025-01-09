from pytube import Playlist
from bs4 import BeautifulSoup
import requests
import isodate
import time
from tqdm import tqdm

"""
Used to calculate the number of hours needed to study a particular playlist.
pytube is only used to get video URLs and not to fetch the duration.
Durations are fetched via web scraping.
"""


def get_playlist_info(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"  # Fixes some pytube issues
    except Exception as e:
        print(f"Error loading playlist: {e}")
        return None

    try:
        playlist_name = playlist.title
        playlist_author = playlist.owner
    except Exception as e:
        print(f"Error fetching playlist metadata: {e}")
        playlist_name = "Unknown Playlist"
        playlist_author = "Unknown Author"

    try:
        video_ids = [video.video_id for video in playlist.videos]
        video_durations = get_video_durations(video_ids)
    except Exception as e:
        print(f"Error fetching video IDs or durations: {e}")
        return None

    try:
        total_seconds = sum(isodate.parse_duration(d).total_seconds() for d in video_durations)
        video_count = len(video_durations)
        average_length = total_seconds / video_count if video_count > 0 else 0
    except Exception as e:
        print(f"Error calculating total duration or average length: {e}")
        total_seconds, video_count, average_length = 0, 0, 0

    speeds = [1.25, 1.5, 1.75, 2.0]
    speed_durations = {
        f"at_{speed}x": format_time(total_seconds / speed) for speed in speeds
    }

    return {
        "playlist_name": playlist_name,
        "playlist_author": playlist_author,
        "video_count": video_count,
        "average_video_length": format_time(average_length),
        "total_length": format_time(total_seconds),
        **speed_durations
    }


def get_video_durations(video_ids):
    base_url = 'https://www.youtube.com/watch?v='
    durations = []

    for video_id in tqdm(video_ids, desc="Fetching video durations"):
        url = base_url + video_id
        try:
            response = requests.get(url, timeout=10)  # Add timeout to handle slow responses
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            duration_element = soup.find('meta', itemprop="duration")
            if not duration_element:
                raise ValueError("Duration metadata not found.")

            duration_str = duration_element['content']
            durations.append(duration_str)
        except requests.exceptions.RequestException as req_err:
            print(f"Network error for video ID {video_id}: {req_err}")
        except Exception as e:
            print(f"Error fetching duration for video ID {video_id}: {e}")
        finally:
            time.sleep(1)  # To avoid rate-limiting or being blocked by YouTube

    return durations


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    playlist_url = input("Playlist URL: ")
    playlist_info = get_playlist_info(playlist_url)

    if playlist_info:
        print("\n****** YouTube Study Planner ******")
        print(f"Playlist Name: {playlist_info['playlist_name']}")
        print(f"Playlist Author: {playlist_info['playlist_author']}")
        print(f"Playlist: {playlist_info['video_count']} videos")
        print(f"Average video length: {playlist_info['average_video_length']}")
        print(f"Total length: {playlist_info['total_length']}")
        print(f"At 1.25x: {playlist_info['at_1.25x']}")
        print(f"At 1.50x: {playlist_info['at_1.5x']}")
        print(f"At 1.75x: {playlist_info['at_1.75x']}")
        print(f"At 2.00x: {playlist_info['at_2.0x']}")
    else:
        print("Failed to fetch playlist information.")
