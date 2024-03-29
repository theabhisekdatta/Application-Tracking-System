import pickle
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
from nltk.stem import PorterStemmer
nltk.download('punkt')


# Load pre-trained Word2Vec model
model_file_path = "utilities/pretrain_word2vec-google-news-300"
with open(model_file_path, 'rb') as f:
    word2vec_model = pickle.load(f)


def preprocess_text(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    # Removing special characters except alphanumeric and space
    cleaned_text = [re.sub(r'[^a-zA-Z0-9\s]', '', token) for token in tokens]
    # Stopwords define
    stopwords = set(['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't",
                     'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn',
                     "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during',
                     'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't",
                     'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn',
                     "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn',
                     "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or',
                     'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should',
                     "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them',
                     'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very',
                     'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why',
                     'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours',
                     'yourself', 'yourselves', 'could', 'he', 'i', 'us', 'you', 'he', 'she', 'we', 'they', 'them', 'my', 'your', 'his',
                     'her', 'our', 'their', 'from', 'by', 'at', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could',
                     'must', 'about', 'up', 'down', 'out', 'some', 'any', 'if', 'else', 'than', 'when', 'where', 'why', 'how', 'what', 'which'
                     ])
    # Initialize Porter Stemmer
    porter = PorterStemmer()
    # Stem each word in the cleaned_text list
    stemmed_text = [porter.stem(word)
                    for word in cleaned_text if word not in stopwords]
    return stemmed_text


def calculate_similarity(jd_text, resume_text):
    # Preprocess the text
    jd_tokens = preprocess_text(jd_text)
    resume_tokens = preprocess_text(resume_text)

    # Filter tokens to include only those present in the Word2Vec model
    jd_tokens = [
        token for token in jd_tokens if token in word2vec_model.key_to_index]
    resume_tokens = [
        token for token in resume_tokens if token in word2vec_model.key_to_index]

    # Check if the filtered lists are empty
    if len(jd_tokens) == 0 or len(resume_tokens) == 0:
        return 0.0  # Return zero similarity if no tokens are found

    # Calculate the average word embeddings for job description and resume
    jd_embedding = sum(word2vec_model.get_vector(token)
                       for token in jd_tokens) / len(jd_tokens)
    resume_embedding = sum(word2vec_model.get_vector(token)
                           for token in resume_tokens) / len(resume_tokens)

    # Compute cosine similarity
    similarity = cosine_similarity([jd_embedding], [resume_embedding])[0][0]

    # Convert similarity to percentage
    similarity_percentage = round(similarity * 100, 2)
    return similarity_percentage
