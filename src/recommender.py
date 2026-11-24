import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_retriever import search_movies

# Load API key
load_dotenv()

# Connect to OpenRouter
llm = ChatOpenAI(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)



def get_recommendations(query):
    movies = search_movies(query)

    if not movies:
        return "No matching movies found."

    movie_details = ""

    for movie in movies:
        movie_details += (
            f"Title: {movie.metadata['title']}\n"
            f"Genre: {movie.metadata['genre']}\n"
            f"Year: {movie.metadata['year']}\n"
            f"Description: {movie.metadata['description']}\n\n"
        )

    prompt = f"""
    You are an AI movie recommendation assistant.

    User preference: {query}

    Available movies:
    {movie_details}

    Recommend only movies that clearly match the user's preference.

    Do not recommend unrelated movies.
    Do not recommend movies outside the available list.

    Explain briefly why each recommended movie matches.
    """

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    queries = [
        "I want a movie about space exploration",
        "I like romantic love stories",
        "I want a scary horror movie"
    ]

    for query in queries:
        print("\nUser Preference:", query)
        print(get_recommendations(query))
        print("-" * 40)
