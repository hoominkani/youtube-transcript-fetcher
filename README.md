# YouTube Transcript Fetcher

YouTube Transcript Fetcher is a web application that retrieves and displays subtitles from a specified YouTube video URL. The application is structured into Flask that handles the retrieval of subtitles using the `youtube-transcript-api`.

<img width="503" alt="スクリーンショット 2024-03-13 18 37 27" src="https://github.com/hoominkani/youtube-transcript-fetcher/assets/35726568/ec6cca6c-bf57-4a2c-a836-a09a41247d46">

## Features

- **YouTube Subtitle Retrieval**: Input a YouTube video URL to fetch its subtitles.
- **Subtitle Display**: View the fetched subtitles directly on the web interface.
- **Download Option**: Ability to download the retrieved subtitles as a text file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your machine.
- Python 3 and pip are installed for backend development.

## Installation

To set up YouTube Transcript Fetcher for development, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/hoominkani/youtube-transcript-fetcher.git
   cd youtube-transcript-fetcher
   ```

2. **Build and Run with Docker Compose**

   ```bash
   docker-compose up -d
   ```

The frontend will be accessible at http://localhost:5000.