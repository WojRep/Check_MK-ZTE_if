# Check_MK-ZTE_if

Plugin for the Check_MK monitoring system

Some ZTE devices do not respond to the standard snmp interface description (ifDescription) query with valid data, and returns an empty or null value. This plugin eliminates the problem by directing the query to a different OID, dedicated to ZTE interfaces.

![Screenshot-1](https://github.com/WojRep/Check_MK-ZTE_if/blob/main/.html/zte_if-1.png)
