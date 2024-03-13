# YouTube Transcript Fetcher

YouTube Transcript Fetcher is a web application that retrieves and displays subtitles from a specified YouTube video URL. The application is structured into a frontend developed with Next.js for the user interface, and a Flask backend that handles the retrieval of subtitles using the `youtube-transcript-api`.

## Features

- **YouTube Subtitle Retrieval**: Input a YouTube video URL to fetch its subtitles.
- **Subtitle Display**: View the fetched subtitles directly on the web interface.
- **Download Option**: Ability to download the retrieved subtitles as a text file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your machine.
- Node.js and npm/yarn are installed for frontend development.
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