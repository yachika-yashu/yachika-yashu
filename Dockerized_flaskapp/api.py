import requests

ner_url = "https://namedentityrecognition.p.rapidapi.com/ner"



headers_ner = {
	"x-rapidapi-key": "32d6e48c3amsh5305e97980c6544p172cc7jsn30832f83242a",
	"x-rapidapi-host": "namedentityrecognition.p.rapidapi.com",
	"Content-Type": "application/json"
}



def ner(text):
    ner = requests.post(ner_url, json=text, headers=headers_ner)
    return ner.json()





sa_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"



headers_sa = {
	"x-rapidapi-key": "32d6e48c3amsh5305e97980c6544p172cc7jsn30832f83242a",
	"x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
}



def sa(text):
    sa = requests.post(sa_url, json=text, headers=headers_sa)
    return sa.json()