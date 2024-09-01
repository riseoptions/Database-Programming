# Database-Programming
PyMySQL &amp; MySQL Connector

# Andmebaasiprogrammeerimine Pythonis: PyMySQL ja MySQL Connector

**Andmebaasiprogrammeerimine** on oluline osa rakenduste arendamisest, võimaldades salvestada, hallata ja pärida andmeid andmebaasist. Python pakub mitmeid teeke, mis lihtsustavad MySQL andmebaasidega suhtlemist.

## PyMySQL

**PyMySQL** on puhtalt Pythonis kirjutatud teek, mis võimaldab ühenduda MySQL andmebaasidega ja sooritada SQL-päringuid. See on lihtne ja kerge alternatiiv, mis ei vaja eraldi binaarfaile.

- **Paigaldamine**: Paigalda PyMySQL teek käsurealt:  
  ```bash
  pip install pymysql


```python
import pymysql
connection = pymysql.connect(host='localhost',
                             user='kasutaja',
                             password='salasõna',
                             database='andmebaas')
cursor = connection.cursor()
cursor.execute("SELECT * FROM tabel")
tulemused = cursor.fetchall()

for rida in tulemused:
    print(rida)

connection.close()
```


## MySQL Connector
**MySQL Connector** on ametlik MySQL'i poolt pakutav teek, mis võimaldab Pythonil suhelda MySQL andmebaasidega. See on usaldusväärne ja hästi dokumenteeritud lahendus, mis toetab uusimaid MySQL funktsioone.
