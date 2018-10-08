from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
import csv,json
import pprint
def set_customers_mappings(es):
    with open("settings.json") as settings_file:
        settings = json.load(settings_file)
        es.indices.create(index="customers", body=settings, ignore=400)

def gen_data(records):
    for record in records:
        yield {
            "_op_type": "update",
            "_index": "customers",
            "_type": "customer",
            "_id": record["Customer"],
            "doc": {
                "Customer_Number": record["Customer_Number"],
                "Service_street2": record["Service_street2"],
                "Service_Street1": record["Service_Street1"],
                "Service_City": record["Service_City"]
            },
            "doc_as_upsert":True
        }


def bulk_insert_customers(es, input_file):
    data = json.loads(json.dumps(list(csv.DictReader(open(input_file)))))

    for ok, result in streaming_bulk(
            es,
            gen_data(data),
            index="customers",
            doc_type='customer',
            chunk_size=50
        ):
        action, result = result.popitem()
        doc_id = '/%s/customer/%s' % ("customers", result['_id'])
        if not ok:
            print('Failed to %s document %s: %r' % ("bulk", doc_id, result))
        else:
            print(doc_id)

if __name__ == '__main__':
    es = Elasticsearch(
        ['localhost'],
        scheme="http",
        port=9200,
    )

    set_customers_mappings(es)
    bulk_insert_customers(es, input_file = "AWECRMDatasyn_067_176.csv")
