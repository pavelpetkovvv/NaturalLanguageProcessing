from .lsa import LsaSummarizer
import nltk

def lsa_summarize(text, language='english'):
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    from nltk.corpus import stopwords

    # text = """
    # Artificial Intelligence (AI) is rapidly transforming industries by automating tasks, improving decision-making, and enhancing customer experiences.
    # Businesses are integrating AI-powered chatbots, predictive analytics, and computer vision into their workflows to increase efficiency.
    # Healthcare providers use AI-driven diagnostics to detect diseases earlier, while financial institutions rely on AI for fraud detection and risk assessment.
    # The retail sector employs AI for personalized recommendations, and manufacturing benefits from predictive maintenance powered by machine learning.
    # However, AI also raises ethical concerns, including bias in algorithms, data privacy issues, and job displacement. AI systems can unintentionally reinforce biases present in training data,
    # leading to unfair outcomes. Additionally, as AI-driven automation replaces repetitive jobs, workers in certain sectors may face unemployment, necessitating reskilling programs.
    # Data privacy remains a significant concern, as AI relies on vast amounts of personal data to function effectively. As AI continues to evolve, it is crucial to develop regulations and
    # frameworks to ensure responsible and fair usage of this technology. Governments and organizations must work together to establish guidelines that promote transparency and accountability.
    # Ethical AI development should prioritize fairness, security, and human oversight to mitigate potential risks. While AI presents tremendous opportunities for progress, it must be implemented
    # thoughtfully to balance innovation with societal well-being.
    # """

    summarizer = LsaSummarizer()

    stopwords = stopwords.words(language)
    summarizer.stop_words = stopwords
    summary =summarizer(text, 3)

    # print("====== Original text =====")
    # print(text)
    # print("====== End of original text =====")



    print("\n========= Summary =========")
    print(" ".join(summary))
    print("========= End of summary =========")