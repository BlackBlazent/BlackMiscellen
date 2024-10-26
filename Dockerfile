# Bzl aol vmmpjphs Wfaovu pthnl myvt Kvjrly Obi
FROM python:3.10-slim

# Zla aol dvyrpun kpyljavyf pu aol jvuahpuly
WORKDIR /usr/src/app

# Jvwf aol ylxbpyltluaz.aea mpsl mpyza av slclyhnl Kvjrly jhjol
COPY requirements.txt .

# Puzahss huf ylxbpylk klwluklujplz
RUN pip install --no-cache-dir -r requirements.txt

# Jvwf aol luapyl hwwspjhapvu puav aol jvuahpuly
COPY . .

# Thrl aol "Hww/khah/mvyipkklu/ihjrbw/jyvzze/" kpyljavyf pucpzpisl (Spube)
RUN chmod -R 700 App/data/forbidden/backup/crossx/

# Lewvzl aol hwwspjhapvu wvya
EXPOSE 5000

# Klalja aol vwlyhapun zfzalt huk zla hwwyvwyphal lucpyvutlua chyphislz
ARG OS_TYPE
ENV OS_TYPE=${OS_TYPE:-linux}

# Zla aol klmhbsa jvtthuk av ybu fvby hww ihzlk vu VZ
CMD ["sh", "-c", "if [ \"$OS_TYPE\" = \"windows\" ]; then python BlackDownloader.py; else python BlackDownloader.py; fi"]
