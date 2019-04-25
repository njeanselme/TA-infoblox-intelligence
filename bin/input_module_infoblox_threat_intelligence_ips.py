import os
import sys
import time
import datetime
import json
import base64

'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # profile = definition.parameters.get('profile', None)
    pass

def collect_events(helper, ew):
    """Implement your data collection logic here
    """

    # The following examples get the arguments of this input.
    # Note, for single instance mod input, args will be returned as a dict.
    # For multi instance mod input, args will be returned as a single value.
    opt_profile = helper.get_arg('profile')
    interval = helper.get_arg('interval')
    
    helper.set_log_level("debug")
    helper.log_debug("Interval is " + str(interval))
    # In single instance mode, to get arguments of a particular input, use
    # opt_profile = helper.get_arg('profile', stanza_name)

    # get input type
    helper.get_input_type()

    # The following examples get input stanzas.
    # get all detailed input stanzas
    #helper.get_input_stanza()
    # get specific input stanza with stanza name
    # helper.get_input_stanza(stanza_name)
    # get all stanza names
    # helper.get_input_stanza_names()

    # The following examples get options from setup page configuration.
    # get the loglevel from the setup page
    loglevel = helper.get_log_level()
    # get proxy setting configuration
    proxy_settings = helper.get_proxy()
    # get account credentials as dictionary
    # account = helper.get_user_credential_by_username("username")
    # account = helper.get_user_credential_by_id("account id")
    # get global variable configuration
    global_apikey = helper.get_global_setting("apikey")

    # The following examples show usage of logging related helper functions.
    #helper.set_log_level("info")
    # write to the log for this modular input using configured global log level or INFO as default
    # helper.log("log message")
    # write to the log using specified log level
    helper.log_info("Start download for Infoblox Threatlist")

    # set the log level for this modular input
    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
    
    
    url = "https://platform.activetrust.net:8000/api/data/threats/IP?data_format=json"
    
    #if opt_profile and not opt_profile.isspace():
    #    url = url + "&profile=" + opt_profile
    if interval:
        period = int(interval)/3600
        url = url + "&period=" + str(period) + "%20hours"
    else:
        url = url +"&period=1%20hours"
    method="GET"
    
    auth = base64.encodestring('%s:%s' % (global_apikey,' ')).replace('\n', '')
    headers = {
   'Authorization':'Basic %s' % auth,
   'Content-Type':'application/x-www-form-urlencoded',
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
   'Cache-Control': 'no-cache'
    }


    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, method, parameters=None, payload=None,
                                        headers=headers, cookies=None, verify=True, cert=None,
                                        timeout=(600,600), use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    #r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()
    
    
    try:
        r_json=json.loads(r_text)
    except:
        raise Exception("Unable to load into a json format")
    
    try:
        r_json_threat = r_json["threat"]
        for item in r_json_threat:
            data = json.dumps(item)
            event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
            ew.write_event(event)
    except:
        helper.log_info("Unable to get threats from json output")
    
    helper.log_info("Infoblox TIDE download completed")
    