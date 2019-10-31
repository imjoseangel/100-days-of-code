FROM python

COPY ./dockersignal.py ./dockersignal.py
RUN pip install requests

ENTRYPOINT ["python", "/dockersignal.py"]
