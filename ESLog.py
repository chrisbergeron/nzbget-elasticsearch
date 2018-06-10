#!/usr/bin/env python
#
# Insert a document(record) into ElasticSearch upon completion
#

##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Log output to ElasticSearch
# Created by Chris Bergeron <nzbget@chrisbergeron.com>
#
# Inserts NZBGet logs into ElasticSearch.  Options are hostname and port.
# See https://chrisbergeron.com/ for details
#
#
# NOTE: This script requires Python to be installed on your system and the
# Elasticsearch python module (pip install elasticsearch)
# Visit:  https://chrisbergeron.com/ for more information

##############################################################################
### OPTIONS                                                                ###

# ElasticSearch server host
#Host=localhost

# ElasticSearch port (default is 9200); uncomment if different from default
#Port=9200

# NZB Disposition (the outcome of the download attempt)
#Disposition=Download Complete

### NZBGET POST-PROCESSING SCRIPT
##############################################################################

import os,datetime,sys,uuid
from datetime import datetime
import elasticsearch
from elasticsearch import Elasticsearch

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_ERROR=94
POSTPROCESS_NONE=95

# Check if the script is called from nzbget 15.0 or later
if not 'NZBOP_NZBLOG' in os.environ:
    print('*** NZBGet post-processing script ***')
    print('This script is supposed to be called from nzbget (15.0 or later).')
    sys.exit(POSTPROCESS_ERROR)

# Make sure all our options are set (Settings -> ESLog)
required_options = ('NZBPO_HOST', 'NZBPO_PORT', 'NZBPO_DISPOSITION', 'NZBPP_NZBNAME')
for	optname in required_options:
	if (not optname in os.environ):
		print('[ERROR] Option %s is missing in configuration file. Please check script settings' % optname[6:])
		sys.exit(POSTPROCESS_ERROR)

# Get environment variables/options from NZBGet
id = uuid.uuid4()
nzbname = os.environ['NZBPP_NZBNAME']
host = os.environ['NZBPO_HOST']
port = os.environ['NZBPO_PORT']
disposition = os.environ['NZBPO_DISPOSITION']

# Create ES server object
try:
  es = Elasticsearch([{'host': host, 'port': port}])
  # print('Connected ', es.info())
except Exception as ex:
  print ('Error: ', ex)

# Replace periods with spaces in our filename log entry
nzbname=nzbname.replace('.', ' ')
timestamp=datetime.now()

# Insert our record into ES
try:
  es = Elasticsearch([{'host': host, 'port': port}])

  doc = {
    'nzbname': nzbname,
    'disposition': disposition,
    'timestamp': timestamp,
  }
  res = es.index(index="nzbget", doc_type='document', id=id, body=doc)
  # print(res['result'])

except Exception as ex:
  print ('Couldnt Insert: ', ex)

print ("[DETAIL] Inserting record into ElasticSearch: ", disposition, " ", nzbname, " ", timestamp)
sys.stdout.flush()

# All OK, returning exit status 'POSTPROCESS_SUCCESS' (int <93>) to let NZBGet know
# that our script has successfully completed.
sys.exit(POSTPROCESS_SUCCESS)
