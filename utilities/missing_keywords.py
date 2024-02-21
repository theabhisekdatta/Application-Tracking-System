from PyPDF2 import PdfReader


def extract_keywords(text):
    # Function to extract keywords from text
    # You may need to customize this based on your requirements
    # For a simple implementation, we can split the text into words
    # and remove common stopwords (if necessary)
    keywords = text.lower().split()  # Convert to lowercase and split by space
    stopwords = set(['a', 'an', 'the', 'and', 'or', 'of', 'to',
                    'in', 'for', 'on', 'with', 'technology'])  # Add more if necessary
    keywords = [word.strip(",.!?()[]")
                for word in keywords if word not in stopwords]
    return set(keywords)


def find_missing_keywords(resume, jd):
    # Extract keywords from resume and job description
    resume_keywords = extract_keywords(resume)
    jd_keywords = extract_keywords(jd)

    # Find missing keywords
    missing_keywords = jd_keywords - resume_keywords

    return missing_keywords


# if __name__ == "__main__":
#     # Example usage
#     # Read resume and job description from files or any source
#     reader = PdfReader('AbhisekDatta_Resume.pdf')
#     page = reader.pages[0]

#     # extracting text from page
#     resume_text = page.extract_text()
#     # with open("resume.txt", "r") as file:
#     #     resume_text = file.read()

#     with open("jd.txt", "r") as file:
#         jd_text = file.read()

#     # Find missing keywords
#     missing_keywords = find_missing_keywords(resume_text, jd_text)

#     print("Missing keywords in the resume compared to the job description:")
#     print(missing_keywords)
