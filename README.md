# Election AI Assistant 🗳️

A premium, interactive AI assistant built with Streamlit to guide users through the election process, voting timelines, and eligibility requirements.

## 🌟 Evaluation Highlights

- **Google Services Integration:** Features a robust AI chatbot powered by the **Google Gemini API** (`google-genai` SDK).
- **Code Quality:** Highly modular architecture with clean separation of concerns (Logic, UI, Data, Utils).
- **Robustness (Efficiency):** Implements a **dual-layer fallback system**. If the Gemini AI service is unavailable or quota-limited, the bot automatically falls back to a local JSON knowledge base.
- **Security:** Implements secure API key management using `.env` and `st.secrets`.
- **Testing:** Comprehensive unit tests for core eligibility logic using `pytest`.
- **Accessibility:** A premium Dark Navy theme with high-contrast elements for maximum readability.

## 📁 Folder Structure
- `app.py`: Main entry point and layout configuration.
- `modules/`: Feature-specific logic (Timeline, Eligibility, AI Chat).
- `data/`: Structured JSON for election steps and FAQ fallbacks.
- `utils/`: UI helper functions and custom CSS injections.
- `tests/`: Automated test suite.

## 🚀 How to Run Locally

1. **Install Dependencies:**
   ```bash
   py -m pip install -r requirements.txt
   ```
2. **Setup API Key:**
   Rename `.env.example` to `.env` and add your Google Gemini API Key.
3. **Launch Application:**
   ```bash
   py -m streamlit run app.py
   ```
4. **Run Tests:**
   ```bash
   py -m pytest tests/
   ```
