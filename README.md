# Instagram AI Agent

An autonomous AI agent designed to plan and generate Instagram content (Reels, Carousels, Posts) for brands. It leverages **LangGraph** for orchestration, **Google Gemini** for content creation, and **Pinecone** for long-term brand memory.

## 🚀 Features

*   **Autonomous Planning**: Generates detailed content plans including captions, hashtags, and visual descriptions.
*   **Brand Memory**: Uses **Pinecone** to store and retrieve brand-specific context, ensuring consistency over time.
*   **Multi-Modal Generation**:
    *   **Text**: Powered by Google Gemini (Gemini 2.5 Flash).
    *   **Visuals**: Includes a Colab notebook for generating images and video clips using Stable Diffusion (LCM-LoRA).
*   **Robust Architecture**: Built with LangChain and LangGraph for reliable state management.
*   **Fallback Modes**:
    *   Runs with a **Mock LLM** if no API keys are provided.
    *   Runs with **NoOp Memory** if Pinecone is not configured.

## 🛠️ Prerequisites

*   Python 3.10+
*   [Ollama](https://ollama.com/) (Optional, for local embeddings if using Pinecone)
    *   Model: `nomic-embed-text` (`ollama pull nomic-embed-text`)

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/instagram-ai.git
    cd instagram-ai
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

Create a `.env` file in the root directory. You can copy the variables below.

**Note**: The application works out-of-the-box without keys in a "Mock Mode". To enable real AI capabilities, set the following:

```env
# LLM Provider (Google Gemini)
GOOGLE_API_KEY=your_google_api_key_here
# OR
GEMINI_API_KEY=your_gemini_api_key_here

# Long-term Memory (Pinecone) - Optional
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name

# Embeddings (Ollama) - Optional (Used with Pinecone)
OLLAMA_BASE_URL=http://localhost:11434
```

## 🏃 Usage

The workflow is divided into two phases: **Planning** (Local) and **Generation** (Cloud/Colab).

### Phase 1: Content Planning

Run the main application to generate the content plan. This step uses the LLM to create hooks, bodies, CTAs, and visual prompts.

```bash
python -m app.main
```

**Output**: This will generate a `content_job.json` file in the root directory containing the structured content plan.

### Phase 2: Media Generation

Use the provided Google Colab notebook to generate the actual images and videos based on the plan.

1.  Open `colab/instagram_content_generator.ipynb` in [Google Colab](https://colab.research.google.com/).
2.  Upload the `content_job.json` generated in Phase 1 to the Colab session.
3.  Run all cells in the notebook.
4.  The notebook will:
    *   Install necessary libraries (Diffusers, MoviePy, etc.).
    *   Load the Stable Diffusion model.
    *   Generate images for carousels and scenes for reels.
    *   Stitch together video clips for Reels.
    *   Save the output to your Google Drive under `instagram_ai/{JOB_ID}`.

## 📂 Project Structure

```
.
├── app/
│   ├── graph.py            # LangGraph definition
│   ├── llm.py              # LLM factory (Gemini + Fallback)
│   ├── main.py             # Entry point
│   ├── state.py            # Graph state definition
│   ├── memory/             # Pinecone memory implementation
│   ├── nodes/              # Graph nodes (Brand, Planner, Creator, Export)
│   └── ...
├── colab/
│   └── instagram_content_generator.ipynb  # Media generation notebook
├── content_job.json        # Output artifact (Plan)
├── requirements.txt        # Python dependencies
└── README.md
```
