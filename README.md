# VISCA PTZ Camera Controller Auditor

## Summary

### Problem Statement

In July 2026, my church was in need of a new PTZ camera controller.
Despite the availability of dozens of [VISCA](#visca)-compatible camera controllers on the market at varying prices, I quickly found that the quality of the PTZ controls specifically is often quite lacking - while also varying greatly between manufacturers and products.
In most cases, only a limited range of PTZ control speeds are covered, and only at limited resolution.
(See [Testing Approach](docs/Testing-Approach.md) for an illustrated example.)

Many of the available controllers also have disappointing limitations in the supported number of cameras they can control, and/or in the supported number of call presets.
While at least these limitations are frequently referenced in available product specifications, I have yet to see any specifications (outside of now this project) that include the range and resolution of the PTZ control speeds.

### VISCA

VISCA (Video System Control Architecture) is an industry-standard control protocol originally developed by Sony for remotely controlling PTZ (pan/tilt/zoom) cameras and related audiovisual equipment.
It is supported by most professional broadcast, production, and surveillance cameras, including those used for stage productions, churches, conference rooms, other live-event and presentation environments, and security applications.
It defines a command/response protocol for functions such as camera selection, pan/tilt, zoom, focus, exposure, presets, and status.
It is commonly transported over RS-232/RS-422 serial connections, as well as IP-based implementations (including UDP and TCP).

## Audits

See [audits](docs/audits/), including [Testing Approach](docs/Testing-Approach.md).

Each audit includes a suite of test results, including any more-functional observations found during testing, support responsiveness, related hardware, and specifics of the firmware version tested.
Click into each linked audit for full results.
Included in the below overview is only the PTZ coverage % as a key metric.

Current highlights, sorted by PTZ coverage %:

| Manufacturer | Product | PTZ Coverage |
| --- | --- | --: |
| AVKANS | [AV-JOY-PRO](docs/audits/AVKANS-AV-JOY-PRO.md) | 82.03% |
| Lumens | [VS-K20](docs/audits/Lumens-VS-K20.md) | 50.00% |
| Zowietek | [ZowieKBD](docs/audits/Zowietek-ZowieKBD.md) | 40.63% |
| Tenveo | [TEVO-KB200MAX](docs/audits/Tenveo-TEVO-KB200MAX.md) | 39.06% |

### Audit Requests and Contributions

If you are a manufacturer of a VISCA-compatible PTZ controller, I would be happy to evaluate your product or products at no charge (beyond shipping), and include the results here.
See [Audit Requests](docs/Audit-Requests.md).

## visca_audit Code

[`visca_audit`](src/visca_audit/) includes a set of MicroPython utilities for testing and auditing controllers in an easy and repeatable fashion.

These modules are designed to be run from inexpensive and readily-available microcontrollers.
I am using a [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/), though these would also easily run on an original [Raspberry Pi Pico (1)](https://www.raspberrypi.com/products/raspberry-pi-pico/) or other similar devices.

Ensure use of appropriate level shifters, as the Pico and many other microcontrollers have UARTs that typically operate at low-voltage logic levels such as 3.3v TTL - compared to RS-232 device levels that may operate at significantly higher positive and negative voltages.

These modules do require [MicroPython's `typing.mpy` module](https://micropython-stubs.readthedocs.io/en/main/typing_mpy.html) from [micropython-stubs](https://github.com/josverl/micropython-stubs).
[`mpy.ps1`](mpy.ps1) can be used to assist with its installation.

[`visca_audit.py`](src/visca_audit/visca_audit.py) is otherwise designed to run stand-alone without any other required libraries or dependencies.
It can be run as a module, or by using "Run current file on Pico" from [MicroPico](https://github.com/paulober/MicroPico), or by other means.

## Sample Specifications

A few examples of supporting cameras with well-defined references of the VISCA protocol:

* [Lumens VC-A50P](https://www.mylumens.com/Download/VC-A50P_VC-A50PN%20RS-232%20command%20set_1_3.pdf)
* [Lumens VC-A51](https://www.mylumens.com/Download/VC-A51_VC-A51S%20RS-232%20command%20set_1_1.pdf)
* [Sony <!-- cSpell:disable -->ILME-FR7<!-- cSpell:enable -->](https://pro.sony/s3/2022/09/14131603/VISCA-Command-List-Version-2.00.pdf)

## Trademarks

Company names, trademarks, product names, and logos referenced in this project are the property of their respective owners and are used for identification and informational purposes only.
Their inclusion does not imply affiliation, sponsorship, endorsement, or certification.

VISCA and related product or technology names may be trademarks of their respective owners.

## Author

Mark Ziesemer

* 🌐 <https://www.ziesemer.com>
* 🔗 <https://www.linkedin.com/in/ziesemer/>
