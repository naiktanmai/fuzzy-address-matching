FROM python:3.6.1 as python-base
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

FROM python:3.6.1-alpine
WORKDIR /usr/src/app
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base /usr/src/app /usr/src/app
RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf /root/.cache

CMD mongo-connector -m mongodb -t esdb -d elastic2_doc_manager --oplog-ts oplogstatus.txt
