# json2yaml

Convert JSON file to formatted YAML file

## Install

    $ install python3
    $ pip3 install -r requirements.txt

## Convert JSON to YAML
    $ python3 json2yaml.py infile.json outfile.yaml


## Example input
    {
    "agent.dhcp.sendToDatabase": "false",
    "agent.dhcp.updateWebServer": "true",
    "agent.hibernation.hibernate.duration.minutes": "4320",
    "agent.hibernation.checkInterval.minutes": "5",
    "agent.hibernation.lastSeen.threshold.minutes": "2",
    "version": "0.1.0"
    }

## Example output
	---
	agent:
	  dhcp:
	    sendToDatabase: 'false'
	    updateWebServer: 'true'
	  hibernation:
	    hibernate:
	      duration:
	        minutes: '4320'
	    checkInterval:
	      minutes: '5'
	    lastSeen:
	      threshold:
	        minutes: '2'
	version: 0.1.0
