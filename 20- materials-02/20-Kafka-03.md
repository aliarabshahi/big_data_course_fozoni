### Avro Schema 

```java
{
  "namespace": "ir.mfozouni.types",
  "type": "record",
  "name": "DeliveryAddress",
  "fields": [
    {"name": "AddressLine","type": ["null","string"]},
    {"name": "City","type": ["null","string"]},
    {"name": "State","type": ["null","string"]},
    {"name": "PinCode","type": ["null","string"]},
    {"name": "ContactNumber","type": ["null","string"]}
  ]
}
```

```java
{
  "namespace": "ir.mfozouni.types",
  "type": "record",
  "name": "LineItem",
  "fields": [
    {"name": "ItemCode","type": ["null","string"]},
    {"name": "ItemDescription","type": ["null","string"]},
    {"name": "ItemPrice","type": ["null","double"]},
    {"name": "ItemQty","type": ["null","int"]},
    {"name": "TotalValue","type": ["null","double"]}
  ]
}
```

```java
{
  "namespace": "ir.mfozouni.types",
  "type": "record",
  "name": "PosInvoice",
  "fields": [
    {"name": "InvoiceNumber","type": ["null","string"]},
    {"name": "CreatedTime","type": ["null","long"]},
    {"name": "CustomerCardNo","type": ["null","string"]},
    {"name": "TotalAmount","type": ["null","double"]},
    {"name": "NumberOfItems","type": ["null","int"]},
    {"name": "PaymentMethod","type": ["null","string"]},
    {"name": "TaxableAmount","type": ["null","double"]},
    {"name": "CGST","type": ["null","double"]},
    {"name": "SGST","type": ["null","double"]},
    {"name": "CESS","type": ["null","double"]},
    {"name": "StoreID","type": ["null","string"]},
    {"name": "PosID","type": ["null","string"]},
    {"name": "CashierID","type": ["null","string"]},
    {"name": "CustomerType","type": ["null","string"]},
    {"name": "DeliveryType","type": ["null","string"]},
    {"name": "DeliveryAddress","type": ["null","DeliveryAddress"]},
    {"name": "InvoiceLineItems","type": {"type": "array", "items": "LineItem"}}
  ]
}
```

### Add some properties (Client Library)

```java
properties.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class);

properties.put(AbstractKafkaSchemaSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG,"http://localhost:8081");
```

### We can consume form local Confluent Kafka 😎

🛑 For the first time that we want to run Confluent Kafka we will see this error: 

**Classpath is empty. Please build the project first e.g. by running ‘gradlew jarAll’**

For solving the issue go to the following URL: 

https://medium.com/@praveenkumarsingh/confluent-kafka-on-windows-how-to-fix-classpath-is-empty-cf7c31d9c787

### You want to see human-readable output?

```bash
docker exec -it schema-registry bash
```

```bash
kafka-avro-console-consumer --bootstrap-server broker:29092 --topic pos --from-beginning
```

### Want to see the Schema-Registry subjects?

Open your browser and go to this address:

http://localhost:8081/subjects/ 

and then 

http://localhost:8081/subjects/pos-value/versions/1

or we can use cURL

```bash
curl -X GET http://schema-registry:8081/subjects
```

**You can delete a subject by using REST API of Schema-Registry**

```bash
curl -X DELETE http://localhost:8081/subjects/NAME_OF_YOUR_SUBJECT
```

**Also you can register your schema manually like this:**

```bash
SCHEMA=$(cat ./NAME_OF_YOUR_SCHEMA.avsc | jq -R -s -c .)

curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" --data "{\"schema\":$SCHEMA}" http://localhost:8081/subjects/NAME_OF_YOUR_TOPIC-value/versions
```

**And you cab see the compatibility by running the following command:**

```bash
curl -X GET http://localhost:8081/config
```

**We can change the compatibility mode by running this:**

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"compatibility":"FORWARD"}' \
  http://localhost:8081//config
```

**You can see the full compatibility relations in the following pic:**

![](.\pics\compatibility.png)

### Let's see some drawings to understand Compatibility better

#### i: Backward

![](.\pics\backward.png)

#### ii: Forward

![](.\pics\forward.png)

#### iii: Full

![](.\pics\full.png)

#### iv: And finally "No Compatibility Modes", End of the Story!

Not providing any compatibility checks provides a great deal of freedom. But the tradeoff is you’re vulnerable to breaking changes that might go undetected until the worst possible time: in **production**.

