FROM python:3.9-slim-buster

RUN mkdir /app
WORKDIR /app

#COPY . .
COPY requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt


EXPOSE 7010



ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]


#CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
#CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]
CMD "/bin/bash"
