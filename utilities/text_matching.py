import pickle
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')

# Load pre-trained Word2Vec model
model_file_path = "pretrained_model/pretrain_word2vec-google-news-300"
with open(model_file_path, 'rb') as f:
    word2vec_model = pickle.load(f)


def preprocess_text(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    return tokens


def calculate_similarity(jd_text, resume_text, word2vec_model):
    # Preprocess the text
    jd_tokens = preprocess_text(jd_text)
    resume_tokens = preprocess_text(resume_text)

    # Filter tokens to include only those present in the Word2Vec model
    jd_tokens = [
        token for token in jd_tokens if token in word2vec_model.key_to_index]
    resume_tokens = [
        token for token in resume_tokens if token in word2vec_model.key_to_index]

    # Calculate the average word embeddings for job description and resume
    jd_embedding = sum(word2vec_model.get_vector(token)
                       for token in jd_tokens) / len(jd_tokens)
    resume_embedding = sum(word2vec_model.get_vector(token)
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
