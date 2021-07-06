import requests
import json
from .details import management_base64, org_id

management_headers = {
	'Authorization': management_base64,
	'Content-Type': 'application/json'
	}
base_url = "https://management.api.umbrella.com/v1/organizations/"


def get_devices():
	response = requests.request("GET", base_url+org_id+"/virtualappliances", headers=management_headers)
	response_to_json = json.loads(response.text)

	interface_list = []
	for element in response_to_json:
		resultDict = {}
		# Learn some elements from the JSON entry, such as NAME, DOMAINS and TYPE
		resultDict["element_name"] = element['name']
		resultDict["element_health"] = element['health']
		domains = element['settings']['domains']
		resultDict["domains"] = (', '.join(domains))
		try:
			resultDict["host_type"] = element['settings']['hostType']
		except:
			resultDict["host_type"] = "unknown"
		resultDict["element_type"] = element['type']
		# If the element is an Umbrella Virtual Appliance, check the last domain synchronization time
		if resultDict["element_type"] == "virtual_appliance":
			resultDict["element_type"] = "Virtual Appliance"
			resultDict["last_updated"] = element['settings']['lastSyncTime']
		# Else, just check the last time the device was updated
		else:
				resultDict["last_updated"] = element['stateUpdatedAt']
		if resultDict["element_type"] == "connector":
			resultDict["element_type"] = "Connector"
		if resultDict["element_type"] == "domain_controller":
			resultDict["element_type"] = "Domain Controller"
		interface_list.append(resultDict)
	return interface_list

def get_va():
	response = requests.request("GET", base_url+org_id+"/virtualappliances", headers=management_headers)
	response_to_json = json.loads(response.text)

	interface_list = []
	for element in response_to_json:
		# Only fetch results if this is a virtual appliance
		if element['type'] == "virtual_appliance":
			resultDict = {}
			resultDict["element_type"] = "Virtual Appliance"
			resultDict["element_name"] = element['name']
			resultDict["element_health"] = element['health']
			resultDict["element_ip"] = element['settings']['internalIPs'][0]
			domains = element['settings']['domains']
			resultDict["domains"] = (', '.join(domains))
			resultDict["last_updated"] = element['settings']['lastSyncTime']
			try:
				resultDict["host_type"] = element['settings']['hostType']
			except:
				resultDict["host_type"] = "unknown"
			interface_list.append(resultDict)
		else:
			pass
	return interface_list

def get_ad_connector():
	response = requests.request("GET", base_url+org_id+"/virtualappliances", headers=management_headers)
	response_to_json = json.loads(response.text)

	interface_list = []
	for element in response_to_json:
		# Only fetch results if this is a virtual appliance
		if element['type'] == "connector":
			resultDict = {}
			resultDict["element_type"] = "Connector"
			resultDict["element_name"] = element['name']
			resultDict["element_health"] = element['health']
			resultDict["element_ip"] = element['settings']['internalIPs'][1]
			domains = element['settings']['domains']
			resultDict["domains"] = (', '.join(domains))
			resultDict["last_updated"] = element['settings']['lastSyncTime']
			try:
				resultDict["host_type"] = element['settings']['hostType']
			except:
				resultDict["host_type"] = "unknown"
			interface_list.append(resultDict)
		else:
			pass
	return interface_list

def get_dcs():
	response = requests.request("GET", base_url+org_id+"/virtualappliances", headers=management_headers)
	response_to_json = json.loads(response.text)

	interface_list = []
	for element in response_to_json:
		# Only fetch results if this is a virtual appliance
		if element['type'] == "domain_controller":
			resultDict = {}
			resultDict["element_type"] = "Domain Controller"
			resultDict["element_name"] = element['name']
			resultDict["element_health"] = element['health']
			resultDict["element_ip"] = element['settings']['internalIPs'][0]
			domains = element['settings']['domains']
			resultDict["domains"] = (', '.join(domains))
			interface_list.append(resultDict)
		else:
			pass
	return interface_list