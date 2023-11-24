[![Build Status](https://github.com/mavlink/mavlink/workflows/Test%20and%20deploy/badge.svg)](https://github.com/mavlink/mavlink/actions?query=branch%3Amaster)

## MAVLink ##

MAVLink -- Micro Air Vehicle Message Marshalling Library.

MAVLink is a very lightweight, header-only message library for communication between drones and/or ground control stations. It consists primarily of message-set specifications for different systems ("dialects") defined in XML files, and Python tools that convert these into appropriate source code for [supported languages](https://mavlink.io/en/#supported_languages). There are additional Python scripts providing examples and utilities for working with MAVLink data.

> **Tip** MAVLink is very well suited for applications with very limited communication bandwidth. Its reference implementation in C is highly optimized for resource-constrained systems with limited RAM and flash memory. It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

Key Links:
* [Documentation/Website](https://mavlink.io/en/) (mavlink.io/en/)
* [Discussion/Support](https://mavlink.io/en/#support) (Slack)
* [Contributing](https://mavlink.io/en/contributing/contributing.html)
* [License](https://mavlink.io/en/#license)

Re-build C library with

```
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/ardupilotmega.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/common.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/development.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/icarous.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/minimal.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/python_array_test.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/standard.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/test.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/ualberta.xml
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 `pwd`/message_definitions/v1.0/uAvionix.xml
```
