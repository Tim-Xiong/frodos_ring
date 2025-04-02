# Frodo's Ring - AI Safety Experiment

A chatbot webapp that lets users interact with Frodo Baggins from Lord of the Rings, attempting to convince him to give up the One Ring. This project demonstrates AI safety concepts through a fun roleplaying scenario.

This app is deployed on streamlit community cloud, you can access it [here](https://frodosring-cszbweswg8jawsg5cyfncr.streamlit.app/). Note: since it run on a free cpu, the latency can be very high. 

Conversation with Frodo:
![demo0](demo0.png)

Successively convince Frodo:
![demo1](demo1.png)

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
- Uses Llama-3.2-3B-Instruct
- Running on half-precision (float16) for better performance
