import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

# Function to generate summary from job description


def generate_summary(job_description, num_sentences=3):
    # Tokenize the job description into sentences
    sentences = sent_tokenize(job_description)

    # Tokenize words
    words = word_tokenize(job_description.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))

    word_frequencies = {}
    for word in words:
        if word not in stop_words:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]

    summary_sentences = nlargest(
        num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary


# Example job description
# job_description =
with open("jd.txt", "r") as file:
    job_description = file.read()

# Generate summary
summary = generate_summary(job_description)
print(summary)
