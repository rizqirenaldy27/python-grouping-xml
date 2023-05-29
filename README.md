
# Grouping XML

Grouping xml with spesific tag

## Running
```
pyhton main.py
```

### XML 1
```
<report>
    <location>
        <town>Kebayoran Baru</town>
        <city>Jakarta Selatan</city>
        <state>DKI Jakarta</state>
    </location>
    <transaction>
        <transactionnumber>123456</transactionnumber>
        <transaction_description>PAYMENT AND COLLECTION SUCCESSFULLY</transaction_description>
        <date_transaction>T00:00:00 </date_transaction>
        <transmode_code>TMDN</transmode_code>
        <amount>3000</amount>
    </transaction>
    <report_indicators>
        <indicator>IND</indicator>
    </report_indicators>
</report>
```

### XML 2
```
<report>
    <location>
        <town>Kebayoran Baru</town>
        <city>Jakarta Selatan</city>
        <state>DKI Jakarta</state>
    </location>
    <transaction>
        <transactionnumber>123457</transactionnumber>
        <transaction_description>PAYMENT SUCCESSFULLY</transaction_description>
        <date_transaction>T00:00:00 </date_transaction>
        <transmode_code>TMDN</transmode_code>
        <amount>13000</amount>
    </transaction>
    <report_indicators>
        <indicator>IND</indicator>
    </report_indicators>
</report>
```

### XML Result
```
<report>
    <location>
        <town>Kebayoran Baru</town>
        <city>Jakarta Selatan</city>
        <state>DKI Jakarta</state>
    </location>
    <transaction>
        <transactionnumber>123456</transactionnumber>
        <transaction_description>PAYMENT AND COLLECTION SUCCESSFULLY</transaction_description>
        <date_transaction>T00:00:00 </date_transaction>
        <transmode_code>TMDN</transmode_code>
        <amount>3000</amount>
    </transaction>
    <transaction>
        <transactionnumber>123457</transactionnumber>
        <transaction_description>PAYMENT SUCCESSFULLY</transaction_description>
        <date_transaction>T00:00:00 </date_transaction>
        <transmode_code>TMDN</transmode_code>
        <amount>13000</amount>
    </transaction>
    <report_indicators>
        <indicator>IND</indicator>
    </report_indicators>
</report>
```

