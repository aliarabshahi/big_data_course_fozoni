### Install Confluent Platform Kafka (cp-kafka)

Set the DNS of [403.online](https://403.online/) or [shecan.ir](https://shecan.ir/). Then

```bash
curl -O https://packages.confluent.io/archive/7.6/confluent-community-7.6.1.tar.gz
```

I got the above link from [HERE](https://docs.confluent.io/platform/current/installation/installing_cp/zip-tar.html).

🛑 If we already put the bin directory of kafka, we do not anymore put the same for kafka-confluent. Just set the CONFLUECT_HOME variable. 
