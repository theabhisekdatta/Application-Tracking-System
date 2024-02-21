from collections import Counter
import re


def extract_keywords(text):
    # Function to extract keywords from text
    # You may need to customize this based on your requirements
    # For a simple implementation, we can split the text into words
    # and remove common stopwords (if necessary)
    text = text.lower()
    # Removing special characters except alphanumeric and space
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    keywords = text.split()  # Convert to lowercase and split by space
    stopwords = set(['a', 'an', 'the', 'and', 'or', 'of', 'to', 'in', 'for', 'on', 'with', 'as', 'us', 'it', 'all', 'can', 'be', 'is', 'are', 'this', 'that', 'there', 'was', 'were', 'i', 'you', 'he', 'she', 'we', 'they', 'them', 'my', 'your', 'his',
                    'her', 'our', 'their', 'from', 'by', 'at', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'must', 'about', 'up', 'down', 'out', 'some', 'any', 'if', 'else', 'than', 'when', 'where', 'why', 'how', 'what', 'which'])
    keywords = [word.strip(",.!?()[]")
                for word in keywords if word not in stopwords]
    return keywords


def find_missing_keywords(resume, jd):
    # Extract keywords from resume and job description
    resume_keywords = extract_keywords(resume)
    jd_keywords = extract_keywords(jd)

    # Find missing keywords
    missing_keywords = list(set(jd_keywords) - set(resume_keywords))

    # Count the frequency of missing keywords
    keyword_frequency = Counter(missing_keywords)

    # Sort the keywords based on their frequency
    sorted_keywords = sorted(
        keyword_frequency, key=keyword_frequency.get, reverse=True)

    # Return only the top 10 missing keywords
    top_10_missing_keywords = sorted_keywords[:10]

    return top_10_missing_keywords
