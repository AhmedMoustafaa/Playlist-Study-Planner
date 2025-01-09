# YouTube Playlist Study Planner

A Python script to calculate the total and average duration of videos in a YouTube playlist and estimate the time needed to watch the content at different playback speeds. This script uses **web scraping** for video duration data, avoiding the need for YouTube API access.

---

## Features
- Calculates the total and average duration of a YouTube playlist.
- Estimates viewing time at various playback speeds (e.g., 1.25x, 1.5x, 1.75x, 2.0x).
- Uses **web scraping** instead of YouTube API, making it simple and independent of API limits.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Required libraries:
  - `pytube`
  - `beautifulsoup4`
  - `requests`
  - `isodate`
  - `tqdm`

You can install the dependencies with:
```bash
pip install -r requirements.txt
```

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedMoustafaa/Playlist-Study-Planner.git
   cd .\Playlist-Study-Planner
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Enter the YouTube playlist URL when prompted.

4. The script will display:
   - Playlist name and author
   - Number of videos
   - Average video length
   - Total length of the playlist
   - Estimated viewing times at various playback speeds

---

## Example Output
```
Playlist URL: https://www.youtube.com/playlist?list=PL...
Fetching video durations: 100%|██████████████████████████| 20/20 [01:00<00:00, 3.00s/it]

****** YouTube Study Planner ******
Playlist Name: Introduction to Python Programming
Playlist Author: CodeAcademy
Playlist: 20 videos
Average video length: 00:12:30
Total length: 04:10:00
At 1.25x: 03:20:00
At 1.50x: 02:46:40
At 1.75x: 02:23:26
At 2.00x: 02:05:00
```

---

## Limitations
- The script relies on web scraping, which may break if YouTube changes its website structure.
- Fetching video durations may take time for large playlists due to scraping and rate-limiting.

---

## License
- This project is licensed under the Unlicense, placing it in the public domain. See the [LICENSE](LICENSE) file for details.
---

## Contributing
Contributions are welcome! Feel free to:
- Report issues or suggest new features.
- Submit pull requests to improve the script.

---

## Acknowledgments
Special thanks to Kanye West and the developers of:
- [pytube](https://github.com/pytube/pytube)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)