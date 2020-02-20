from newspaper import Article
 
url = "https://www.wsj.com/articles/dear-voter-heres-why-political-texts-are-blowing-up-your-phone-11582210800?mod=hp_lead_pos10"

article = Article(url)

article.download()

article.parse()

print(article.authors)

print(article.text)


print((type)(article.text))