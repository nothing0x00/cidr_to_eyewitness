# CIDR_to_Eyewitness

## A script to automate eyewitness scanning for an entire CIDR range

This script will, through prompts, take a CIDR range as input, generate a list of IPs, parse them into HTTP and HTTPS services and then scan them with eyewitness to identify live aand accessible services.

Note: This will result in only checking services on ports 80 and 443. If other ports need to be checked, it may be better to scan the CIDR range with nmap, output in XML format and then ingest that XML into eyewitness.

### Installation and Usage

The script is written in Python 2.7 (I know...) due to issues with ushlex in Python 3. In order to use the script do the following:

`pip install ushlex`

`git clone https://github.com/nothing0x00/cidr_to_eyewitness.git`

`cd cidr_to_eyewitness`

`python cidr_to_eyewitness.py`

Follow the prompts

Updates to this code are upcoming.
