import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import os

nltk.download('punkt')

# Path to save the model locally
MODEL_PATH = "word2vec-google-news-300/word2vec-google-news-300.gz"

# Check if the model exists locally
if not os.path.exists(MODEL_PATH):
    # If the model doesn't exist, download it
    word2vec_model = api.load('word2vec-google-news-300')
    # Save the model locally
    word2vec_model.save(MODEL_PATH)
else:
    # Load the model from the local path
    word2vec_model = gensim.models.KeyedVectors.load(MODEL_PATH)


def preprocess_text(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    return tokens


def calculate_similarity(jd_text, resume_text, word2vec_model):
    # Preprocess the text
    jd_tokens = preprocess_text(jd_text)
    resume_tokens = preprocess_text(resume_text)

    # Filter tokens to include only those present in the Word2Vec model
    jd_tokens = [token for token in jd_tokens if token in word2vec_model.vocab]
    resume_tokens = [
        token for token in resume_tokens if token in word2vec_model.vocab]

    # Calculate the average word embeddings for job description and resume
    jd_embedding = sum(word2vec_model[token]
                       for token in jd_tokens) / len(jd_tokens)
    resume_embedding = sum(word2vec_model[token]
                           for token in resume_tokens) / len(resume_tokens)

    # Compute cosine similarity
    similarity = cosine_similarity([jd_embedding], [resume_embedding])[0][0]

    # Convert similarity to percentage
    similarity_percentage = similarity * 100
    return similarity_percentage


if __name__ == "__main__":
    # Sample job description and resume text
    jd_text = "Your job description text goes here..."
    resume_text = "Your resume text goes here..."

    # Calculate similarity percentage
    similarity_percentage = calculate_similarity(
        jd_text, resume_text, word2vec_model)
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")
