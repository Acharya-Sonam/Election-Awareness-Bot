# Election AI Assistant

An attractive, interactive AI assistant built with Streamlit to help users understand the election process, timelines, and check their eligibility.

## Features
- **Interactive Election Timeline:** Visual steps outlining the process from registration to election day.
- **Eligibility Checker:** A quick tool to determine if you are eligible to vote.
- **AI Chatbot:** An interactive assistant ready to answer your most frequently asked questions.
- **Premium Design:** Custom CSS injected to provide a clean, modern, white "glassmorphism" aesthetic.

## Folder Structure
- `app.py`: Main Streamlit application
- `modules/`: Logic for timeline (`process.py`), eligibility (`eligibility.py`), and chat (`chatbot.py`)
- `data/`: JSON databases for election info and FAQs
- `utils/`: Helper functions including premium CSS styling

## How to Run Locally

1. Clone the repository.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
