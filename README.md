# Alidor - Master

## Overview

This project demonstrates the capabilities required for a 'Master' level task. It implements an audio transcription and analysis application with production-ready features.

## Technologies Used

- **Backend:** Python Flask deployed on AWS Elastic Beanstalk
- **Frontend:** React Framework deployed on S3 Bucket for Static Site Hosting

## Features or Work Explanation

- Supports all audio file formats currently accepted by the Deepgram API.
- Uploads user-provided audio files to S3 and utilizes the public URL for Deepgram transcription.
- Implements file overwriting to store only the most recent audio file in the S3 bucket (e.g., newest.mp3). File in S3 can be directly accessed at [https://alindor-audio-bucket.s3.amazonaws.com/newest.`{enter_file_format_here}`](https://alindor-audio-bucket.s3.amazonaws.com/newest.`{enter_file_format_here}`)
- Enforces file size restrictions (maximum `2 GB`) on uploads. However, due to Elastic Beanstalk timeout settings, uploads for testing purposes are recommended to be less than `1 MB`. During development, audio files from [https://eslyes.com/easydialogs/ec/](https://eslyes.com/easydialogs/ec/) are utlized.
- Handles OpenAI token restrictions (`4097` tokens in total) by utilizing openai piptoken to count tokens and accordingly split prompts exceeding the limit.
- Implements comprehensive error handling on both the backend and frontend.

## Running the Application

### Web Interface:

The web interface can be accessed at: [http://alindor-frontend.s3-website-us-east-1.amazonaws.com/](http://alindor-frontend.s3-website-us-east-1.amazonaws.com/)

The interface accepts an audio file as input, sends an API request to the backend, which then utilizes Deepgram and OpenAI APIs for analysis.

### Backend:

The backend can be directly accessed at: [http://alindor-env.eba-j2su4ewx.us-east-1.elasticbeanstalk.com/upload](http://alindor-env.eba-j2su4ewx.us-east-1.elasticbeanstalk.com/upload)

## Challenges Faced

- **Project Structure:** Dividing the project into well-defined backend and frontend sections.
- **Technology Stack:** Selecting React for the frontend and Python Flask for the backend, requiring in-depth understanding of both frameworks.
- **API Integration:** Understanding the functionalities and limitations of Deepgram and OpenAI APIs.
- **File Size Restrictions by Deepgram API:** Implementing backend logic to handle Deepgram's `2 GB` file size limit.
- **OpenAI Token Restrictions:** Total Tokens allowed for `gpt-3.5-turbo` model are 4097. Thus openai piptoken is employed to manage token limitations and split prompts exceeding the threshold.

_Note: Deepgram and OpenAI API keys are deliberately hardcoded in the code as instructed._
