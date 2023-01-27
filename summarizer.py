from transformers import pipeline
summarizer = pipeline("summarization", model = "pablo-chocobar/summarizer")
import sys 
def summarize(arg1):
    x = arg1
    
    def clean(Article_text):
        lines_list = []

        for line in Article_text.split("\n"):

            stripped_line = line.strip()
            
            if len(stripped_line) >= 100:
                lines_list.append(stripped_line)
        return "   ".join(lines_list)
    
    x = clean(x)
    article_text = """ """
    for i in x:
        article_text += i

    import re
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    article_text1  = article_text[:1000]
    summary = summarizer(article_text1, max_length=200, min_length=100, do_sample=False)

    b = summary[0]["summary_text"]
    return b

if __name__ == "__main__":
    summarize(sys.argv[1])
