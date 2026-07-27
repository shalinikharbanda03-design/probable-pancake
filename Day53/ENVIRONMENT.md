# Environment & Configuration Guide
## Environment Variables
Create a `.env` file in the root directory (or set in Streamlit secrets):

```env
ANTHROPIC_API_KEY=your_claude_api_key_here
LOG_LEVEL=INFO
```
### Supported Models
* Primary Model:
* claude-3-5-sonnet-20241022
* Fast/Fallback Model:
* claude-3-haiku-20240307

### Dependencies
* Streamlit (UI Framework)
* Pandas (CSV / Zero-DB Handling)
* Anthropic Python SDK (AI Engine)
