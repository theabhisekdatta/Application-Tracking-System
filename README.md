# Application Tracking System

## Project Description:
The Application Tracking System is a tool designed to assist users in comparing job descriptions with resumes using various Natural Language Processing (NLP) techniques. The system primarily employs two key features: job description matching and summary generation based on word frequencies.

1. **Job Description Matching:**
   - Utilizes cosine similarities and word embeddings (via average word2vec) to compare job descriptions and resumes.
   - Cosine similarities help in assessing the similarity between the job requirements and the applicant's qualifications.
   - Word embeddings enhance the understanding of semantic relationships between words, contributing to more accurate comparisons.

2. **Summary Generation:**
   - Generates summaries based on word frequencies extracted from the job description and resume.
   - Provides a concise overview of the key terms and phrases present in both documents.

Despite the availability of more advanced AI models, the system opts for basic NLP techniques due to issues with inconsistent output from more complex models like GPT.

## How to Use the Project:
To utilize the Application Tracking System, follow these steps:

1. **Input Job Description and Resume:**
   - Provide the job description text and the applicant's resume.
   - Ensure the text is in a readable format and devoid of unnecessary formatting.

2. **Job Description Matching:**
   - The system will calculate cosine similarities and word embeddings to assess the match between the job description and the resume.
   - It will output the degree of similarity and highlight areas of alignment or divergence between the two documents.

3. **Summary Generation:**
   - The system will generate a summary based on the word frequencies extracted from the job description and resume.
   - This summary will offer insights into the most significant terms and phrases present in both documents.

4. **Deployment:**
   - The application is deployed on Hugging Spaces Faces for easy access and usage.
   - Users can access the application through the provided link and interact with it seamlessly.

5. **Limitations:**
   - Note that the cosine similarities may not always accurately calculate the distance between the documents as expected.
   - Users should be aware of these limitations and interpret the results with caution.

Enjoy using the Application Tracking System to streamline your job application process and gain valuable insights into matching job requirements with candidate qualifications.
