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

---

## 📝 Step-by-Step Guide

Follow these steps to set up the agent and generate your first Instagram content.

### Step 1: Install Dependencies

First, get the code and install the required Python packages.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/instagram-ai.git
    cd instagram-ai
    ```

2.  **Install Python requirements**:
    Make sure you have Python 3.10+ installed.
    ```bash
    pip install -r requirements.txt
    ```

3.  **(Optional) Install Ollama**:
    If you plan to use Pinecone for memory, you need Ollama for local embeddings.
    *   Download from [ollama.com](https://ollama.com/).
    *   Pull the embedding model:
        ```bash
        ollama pull nomic-embed-text
        ```

### Step 2: Configure Environment

You need to set up your API keys. If you skip this, the app will run in "Mock Mode" (generating fake text without calling real APIs).

1.  **Create a `.env` file** in the root directory:
    ```bash
    touch .env
    ```

2.  **Add your API keys** to the `.env` file:
    ```env
    # Required for real text generation (Google Gemini)
    GOOGLE_API_KEY=your_google_api_key_here

    # Optional: Required for long-term memory (Pinecone)
    PINECONE_API_KEY=your_pinecone_api_key
    PINECONE_INDEX_NAME=your_index_name
    OLLAMA_BASE_URL=http://localhost:11434
    ```

### Step 3: Generate the Content Plan

Now, run the agent to brainstorm and plan the content.

1.  **Run the main script**:
    ```bash
    python -m app.main
    ```

2.  **Check the output**:
    *   The script will run the LangGraph workflow.
    *   Look for a new file named `content_job.json` in the root folder.
    *   This file contains the **Scripts**, **Captions**, **Hashtags**, and **Image Prompts**.

### Step 4: Generate Images & Videos (Google Colab)

Since image generation requires a GPU, we use Google Colab.

1.  **Open the Notebook**:
    *   Go to [Google Colab](https://colab.research.google.com/).
    *   Upload the `colab/instagram_content_generator.ipynb` file from this repository.

2.  **Upload the Plan**:
    *   In the Colab sidebar (Files icon on the left), upload the `content_job.json` file you generated in Step 3.

3.  **Run the Generator**:
    *   In Colab, go to **Runtime** > **Run all** (or press `Ctrl+F9`).
    *   The notebook will:
        1.  Install 3D/Image libraries.
        2.  Load the Stable Diffusion model.
        3.  Generate images for every scene in your plan.
        4.  Stitch images into a video (for Reels).

4.  **Download Results**:
    *   Once finished, check the `instagram_ai/{JOB_ID}` folder in the Colab file browser (or your Google Drive if mounted).
    *   Download your final **MP4 (Reels)** or **PNGs (Carousels)**.

---

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
