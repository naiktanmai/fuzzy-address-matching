FROM docker.elastic.co/logstash/logstash:6.4.2
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/logstash.conf /usr/share/logstash/pipeline/
ADD config/logstash.yml /usr/share/logstash/config/
RUN bin/logstash-plugin install logstash-filter-prune
