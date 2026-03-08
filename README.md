# Google Forms Auto Responder

A Python script that automatically submits randomized responses to a Google Form.

The script generates realistic survey answers and sends them directly to the form's `formResponse` endpoint, allowing you to simulate multiple participants.
(still under development so expect bugs and :p)

## Features

- Sends multiple Google Form submissions automatically
- Randomized answers for realistic survey data
- Handles ranking questions
- Automatically retrieves the required `fbzx` form token
- Random delay between submissions to simulate human interaction
- Simple command line interface

## How It Works

Google Forms accept POST requests at a `formResponse` endpoint.

This script:
1. Fetches the form page
2. Extracts the hidden `fbzx` token required for submissions
3. Generates randomized responses
4. Sends them as POST requests
5. Repeats the process for the number of responses you specify

## Requirements

Python 3.x

Install dependencies:

```bash
pip install requests beautifulsoup4
