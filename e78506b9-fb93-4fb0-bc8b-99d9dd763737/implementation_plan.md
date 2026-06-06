# YouTube Viral Shorts Tracker

This project aims to build a web application that automatically collects and displays YouTube Shorts with high view counts in real-time (or near real-time).

## User Review Required

Before we start building, please review the proposed architecture and tech stack. Building this requires a YouTube Data API Key. 

## Open Questions

> [!IMPORTANT]
> 1. **Do you have a Google Cloud account to get a YouTube Data API key?** We will need this to fetch the data legally and reliably.
> 2. **Do you have a preferred tech stack?** (e.g., React, Next.js, Python, Node.js). If not, I will recommend Next.js as it can handle both frontend and backend tasks easily.
> 3. **Where do you want to store the data?** (e.g., Supabase, Firebase, or just fetch directly without saving initially).

## Proposed Architecture

### 1. Data Source (YouTube Data API v3)
- Use the YouTube Data API to search for videos.
- Filter by `#shorts` or video duration (< 60 seconds).
- Sort the results by `viewCount`.

### 2. Backend (Data Fetching & Storage)
- A scheduled task (cron job) that runs periodically (e.g., every hour) to fetch the latest trending shorts.
- Store the video ID, title, view count, and thumbnail in a database.

### 3. Frontend (User Interface)
- A web interface to display the collected Shorts.
- Features: Grid layout of thumbnails, view counts, click to watch, and filtering by category or date.

### 4. Recommended Tech Stack
- **Framework**: Next.js (React) - handles both frontend UI and backend API routes.
- **Database**: Supabase (PostgreSQL) - easy to set up and great for structured data.
- **Styling**: Tailwind CSS (or Vanilla CSS based on preference) for a modern, sleek look.

## Verification Plan
1. Successfully make a test call to the YouTube API to fetch Shorts.
2. Build the basic UI to display mock data.
3. Connect the real API data to the UI.
4. Set up the database and scheduled fetching.
