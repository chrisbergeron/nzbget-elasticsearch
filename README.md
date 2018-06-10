# NZBGet ElasticSearch Plugin #
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/)
[![Build Status](https://img.shields.io/travis/nzbget/nzbget/develop.svg)](https://travis-ci.org/nzbget/nzbget)

This Plugin for NZBGet inserts a record into a user specified ElasticSearch database.  It only requires 2 configuration options:
- the hostname of the elasticsearch instance
- the port of the elasticsearch instance

This script is written in python and it requires the installation of the elasticsearch module: `pip install elasticsearch`

The purpose of this script is to allow you to create a dashboard or other reporting around your downloads.  Using Grafana or the Kibana dashboard you can create neat visualizations.  

Here's a very simple example:
![Simple Kibana Visualization](https://raw.githubusercontent.com/chrisbergeron/nzbget-elasticsearch/master/screenshots/kibana_visualization.png)
![Simple Kibana Search](https://raw.githubusercontent.com/chrisbergeron/nzbget-elasticsearch/master/screenshots/kibana_search.png)

Fell free to create a Pull Request (PR) and submit improvements.  I'm new to Python and there are a lot of areas for improvement in this plugin.

## Usage: ##
Download and copy the ESLog.py file from this repo into your `NZBGet/scripts` directory.

In NZBGet go into `Settings` and at the bottom left you should see `ESLog`:
![Configuring Plugin](https://raw.githubusercontent.com/chrisbergeron/nzbget-elasticsearch/master/screenshots/configuring-plugin.png)

Add the hostname of your ElasticSearch instance (not Kibana or Logstash) and the Port number it's listening on (default is 9200).

If configured properly, you'll see lines like this in your NZBGet `Messages`:
![Sample Log Output](https://raw.githubusercontent.com/chrisbergeron/nzbget-elasticsearch/master/screenshots/nzbget-example-log-entry.png)

## Roadmap: ##
- [ ] Separate Show Name, Episode Name, Season and Episode info, Quality and Crew into separate index fields in Elastic.
- [ ] Add case statement to parse and map NZBGet output codes into disposition names

Learn more about NZBGet here:
- [Home page (nzbget.net)](http://nzbget.net) - for first time visitors, learn more about NZBGet;
- [Forum](http://forum.nzbget.net) - get support, share your ideas, scripts, add-ons.