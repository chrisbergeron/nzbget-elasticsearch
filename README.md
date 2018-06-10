# NZBGet ElasticSearch Plugin #
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/)
[![Build Status](https://img.shields.io/travis/nzbget/nzbget/develop.svg)](https://travis-ci.org/nzbget/nzbget)

This Plugin for NZBGet inserts a record into a user specified ElasticSearch database.  It only requires 2 configuration options:
- the hostname of the elasticsearch instance
- the port of the elasticsearch instance

This script is written in python and it requires the installation of the elasticsearch module: `pip install elasticsearch`

The purpose of this script is to allow you to create a dashboard or other reporting around your downloads.  Using Grafana or the Kibana dashboard you can create neat visualizations.  

Here's a very simple example:


Fell free to create a Pull Request (PR) and submit improvements.  I'm new to Python and there are a lot of areas for improvement in this plugin.

## Roadmap: ##
- Separate Show Name, Episode Name, Season and Episode info, Quality and Crew into separate index fields in Elastic.
- Add case statement to parse and map NZBGet output codes into disposition names

Learn more about NZBGet here:
- [Home page (nzbget.net)](http://nzbget.net) - for first time visitors, learn more about NZBGet;
- [Forum](http://forum.nzbget.net) - get support, share your ideas, scripts, add-ons.