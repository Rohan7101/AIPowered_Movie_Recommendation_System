# AI Movie Recommendation System

A Python-based AI Movie Recommendation System using **LangChain, FAISS, Hugging Face Sentence Transformers, and Nemotron LLM** to recommend movies based on natural-language user preferences.

## 1. Project Overview

The AI Movie Recommendation System helps users discover movies based on their interests.

Users enter their movie preferences in natural language, such as "I want a scary horror movie." The system searches a movie dataset, identifies relevant movies, and uses a Large Language Model (LLM) to generate personalized recommendations with explanations.

The application runs through a simple Python terminal interface.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Pandas | Loading and processing the movie dataset |
| Sentence Transformers | Generating text embeddings |
| Hugging Face | Providing access to the pre-trained embedding model |
| LangChain | Integrating embeddings, FAISS and the LLM |
| FAISS | Vector storage and similarity search |
| OpenRouter API | Providing access to the Nemotron model |
| Nemotron LLM | Generating movie recommendations and explanations |
| Pytest | Automated testing |

**Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`

**LLM:** `nvidia/nemotron-3-ultra-550b-a55b:free`

## 3. Key Features

- Natural-language movie preference input
- Dataset containing 100 movies across 8 genres
- Semantic similarity search using FAISS
- LangChain-based movie retrieval
- Similarity and genre-based filtering
- Up to five retrieved movie candidates
- AI-generated recommendations with explanations
- Simple Python terminal interface
- Automated testing using Pytest

## 4. How the System Works

1. **Dataset Loading:** Pandas loads movie information from `movies.csv`.
2. **Embedding Generation:** Sentence Transformers converts movie information into numerical vectors.
3. **Vector Store:** FAISS indexes the movie embeddings for similarity searching.
4. **User Input:** The user enters a movie preference in natural language.
5. **Movie Retrieval:** LangChain's FAISS integration retrieves similar movies.
6. **Filtering:** The system applies similarity and genre-based filtering to select candidates.
7. **LLM Processing:** LangChain sends the retrieved movie details to Nemotron through OpenRouter.
8. **Final Output:** Nemotron generates personalized recommendations with explanations.

### Application Workflow

```text
User Movie Preference
         |
         v
Sentence Transformers
         |
         v
LangChain + FAISS
         |
         v
Similarity & Genre Filtering
         |
         v
Nemotron LLM via OpenRouter
         |
         v
Movie Recommendations
```

## 5. Project Structure

```text
AI_Movie_Recommendation_System/
|
|-- data/
|   |-- movies.csv
|
|-- src/
|   |-- __init__.py
|   |-- dataset.py
|   |-- langchain_retriever.py
|   |-- recommender.py
|
|-- tests/
|   |-- test_recommender.py
|
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .env
```

### Main Files

- `dataset.py` — Loads and prepares movie data from the CSV file.
- `langchain_retriever.py` — Creates movie embeddings, builds the FAISS vector store, retrieves similar movies and applies filtering.
- `recommender.py` — Handles user interaction and generates AI recommendations using the Nemotron LLM.
- `test_recommender.py` — Tests movie retrieval functionality.

**Configuration:**

The `.env` file stores the OpenRouter API key. It must remain private and must not be committed to Git.

The `.venv` directory contains the Python virtual environment and should also be excluded from Git.

## 6. Installation and Setup

### Step 1: Create a Virtual Environment

```bash
python3 -m venv .venv
```

### Step 2: Activate the Virtual Environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the API Key

Create a `.env` file in the project root directory.

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenRouter API key.

**Security:** Never share or commit your actual API key.

## 7. Running the Application

From the project root directory, execute:

```bash
python -m src.recommender
```

Enter your movie preference when prompted.

The application retrieves relevant movies and generates recommendations using Nemotron.

An internet connection and a valid OpenRouter API key are required for LLM-generated recommendations.

## 8. Example Input and Output

### Example 1: Space Exploration

**Input:**

```text
I want a movie about space exploration
```

**Example recommendations:**

- Interstellar (2014)
- 2001: A Space Odyssey (1968)
- Avatar (2009)

### Example 2: Romance

**Input:**

```text
I like romantic love stories
```

**Example recommendations:**

- The Notebook (2004)
- Pride & Prejudice (2005)
- A Walk to Remember (2002)
- Me Before You (2016)
- La La Land (2016)

### Example 3: Horror

**Input:**

```text
I want a scary horror movie
```

**Example recommendations:**

- Sinister (2012)
- Hereditary (2018)
- IT (2017)
- A Quiet Place (2018)

The system also provides explanations for recommended movies.

*Note: These are illustrative examples. Actual recommendations may vary depending on the dataset, user query, retrieval results and LLM response.*

## 9. Automated Testing

The project uses Pytest to test movie retrieval functionality.

Run the tests using:

```bash
python -m pytest tests/test_recommender.py -v
```

The test suite covers:

1. Horror movie retrieval.
2. Romance movie retrieval.
3. Space exploration movie retrieval.

These tests validate retrieval behavior without making OpenRouter API calls.

## 10. Limitations

- The dataset contains 100 movies.
- Genre filtering uses simple keyword matching.
- Recommendations depend on embedding similarity and dataset quality.
- The LLM may occasionally generate inaccurate explanations.
- An internet connection and valid API key are required for LLM-generated recommendations.

## 11. Conclusion

The AI Movie Recommendation System demonstrates how **LangChain, Hugging Face Sentence Transformers, FAISS and Nemotron LLM** can be combined to build an intelligent movie recommendation application.

The system uses semantic search to retrieve relevant movies and an LLM to generate personalized recommendations with explanations.

This project demonstrates practical applications of embeddings, vector databases, information retrieval and Large Language Models through a simple Python terminal interface.
