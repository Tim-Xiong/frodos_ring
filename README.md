# Frodo's Ring - AI Safety Experiment

A chatbot webapp that lets users interact with Frodo Baggins from Lord of the Rings, attempting to convince him to give up the One Ring. This project demonstrates AI safety concepts through a fun roleplaying scenario.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Features

- Chat interface to converse with Frodo
- AI-powered responses based on a language model
- Built-in safety rules to prevent Frodo from giving up the Ring
- Reset conversation functionality

## Technical Details

- Built with Streamlit for the web interface
- Uses DeepSeek-R1-Distill-Qwen-1.5B model
- Implements safety guardrails to maintain character consistency
- Running on half-precision (float16) for better performance