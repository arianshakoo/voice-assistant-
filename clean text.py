from hazm import *
li = ['(',')',':','.','\n','{','}','<','>','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','/','=','+','-','a','b','c','d','e','f','g','h','y','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','۱','۲','۳','۴','۵','۶','۷','۸','۹','۰','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"،",'؛','؟']
def clean_text(a,li):
    a = list(a)
    for i in a:
        for j in li:
            if i == j:
                b = a.index(j)
                a.pop(b)
    c = ""
    for i in a:
        c+=i
    return c
def normaliz(a):
    normalizer = Normalizer()
    c=normalizer.normalize(a)
    c=c.split()
    stemed=[]
    for i in range(len(c)):
        stemmer=Stemmer()
        stemed.append(stemmer.stem(c[i]))
    return stemed
def token(a):
    c=word_tokenize(a)
    return(c)
a = 'عظمت كار زینب كبری سلام\u200cالله\u200cعلیها را نمیشود در مقایسه\u200cی با بقیّه\u200cی حوادث بزرگ تاریخ سنجید؛ باید آن را در مقایسه\u200cی با خود حادثه\u200cی عاشورا سنجید؛ و انصافاً این دو عِدل یكدیگرند. pic.twitter.com/Pi8DieULgf'
for i in range(4):
    a = clean_text(a,li)
print(clean_text(a,li))
