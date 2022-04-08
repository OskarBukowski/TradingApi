import requests
import json
from requests.auth import HTTPBasicAuth

response = requests.get('http://jenkins.local:8000/computer/api/json', auth=HTTPBasicAuth('****', '****'))

r = response.json()

###
# AVAILABLE AGENTS
###

print([x for x in [r['computer'][i]['assignedLabels'][0]['name'] for i in range(1, len(r['computer']))]])

ex_response = {'_class': 'hudson.model.ComputerSet',
               'busyExecutors': 0,
               'computer': [{'_class': 'hudson.model.Hudson$MasterComputer',
                             'actions': [],
                             'assignedLabels': [{'name': 'built-in'}],
                             'description': "the Jenkins controller's built-in node",
                             'displayName': 'Built-In Node', 'executors': [{}, {}],
                             'icon': 'symbol-computer',
                             'iconClassName': 'symbol-computer',
                             'idle': True,
                             'jnlpAgent': False,
                             'launchSupported': True,
                             'loadStatistics': {'_class': 'hudson.model.Label$1'},
                             'manualLaunchAllowed': True,
                             'monitorData': {'hudson.node_monitors.SwapSpaceMonitor': {
                                 '_class': 'hudson.node_monitors.SwapSpaceMonitor$MemoryUsage2',
                                 'availablePhysicalMemory': 278675456,
                                 'availableSwapSpace': 840167424,
                                 'totalPhysicalMemory': 7660396544,
                                 'totalSwapSpace': 2147479552},
                                             'hudson.node_monitors.TemporarySpaceMonitor': {
                                                 '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                                                 'timestamp': 1649388802104,
                                                 'path': '/tmp',
                                                 'size': 409712103424},
                                             'hudson.node_monitors.DiskSpaceMonitor': {
                                                 '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                                                 'timestamp': 1649388802102,
                                                 'path': '/var/jenkins_home',
                                                 'size': 409712103424},
                                             'hudson.node_monitors.ArchitectureMonitor': 'Linux (amd64)',
                                             'hudson.node_monitors.ResponseTimeMonitor': {
                                                 '_class': 'hudson.node_monitors.ResponseTimeMonitor$Data',
                                                 'timestamp': 1649388802103,
                                                 'average': 0},
                                             'hudson.node_monitors.ClockMonitor': {
                                                 '_class': 'hudson.util.ClockDifference',
                                                 'diff': 0}}, 'numExecutors': 2,
                             'offline': False,
                             'offlineCause': None,
                             'offlineCauseReason': '',
                             'oneOffExecutors': [],
                             'temporarilyOffline': False},
                            {'_class': 'hudson.slaves.SlaveComputer',
                             'actions': [],
                             'assignedLabels': [{'name': 'aws-london'}],
                             'description': '',
                             'displayName': 'aws-london',
                             'executors': [{}],
                             'icon': 'symbol-computer-offline',
                             'iconClassName': 'symbol-computer-offline',
                             'idle': True,
                             'jnlpAgent': True,
                             'launchSupported': False,
                             'loadStatistics': {'_class': 'hudson.model.Label$1'},
                             'manualLaunchAllowed': True,
                             'monitorData': {'hudson.node_monitors.SwapSpaceMonitor': None,
                                             'hudson.node_monitors.TemporarySpaceMonitor': None,
                                             'hudson.node_monitors.DiskSpaceMonitor': None,
                                             'hudson.node_monitors.ArchitectureMonitor': None,
                                             'hudson.node_monitors.ResponseTimeMonitor': None,
                                             'hudson.node_monitors.ClockMonitor': None},
                             'numExecutors': 1,
                             'offline': True,
                             'offlineCause': None,
                             'offlineCauseReason': '',
                             'oneOffExecutors': [],
                             'temporarilyOffline': False,
                             'absoluteRemotePath': None},
                            {'_class': 'hudson.slaves.SlaveComputer',
                             'actions': [],
                             'assignedLabels': [{'name': 'aws-virginia'}],
                             'description': 'Aws EC2 instance 1CPU 1RAM 30SSD', 'displayName': 'aws-virginia',
                             'executors': [{}], 'icon': 'symbol-computer-offline', 'iconClassName': 'icon-computer',
                             'idle': True, 'jnlpAgent': False, 'launchSupported': True,
                             'loadStatistics': {'_class': 'hudson.model.Label$1'}, 'manualLaunchAllowed': True,
                             'monitorData': {'hudson.node_monitors.SwapSpaceMonitor': None,
                                             'hudson.node_monitors.TemporarySpaceMonitor': None,
                                             'hudson.node_monitors.DiskSpaceMonitor': None,
                                             'hudson.node_monitors.ArchitectureMonitor': None,
                                             'hudson.node_monitors.ResponseTimeMonitor': None,
                                             'hudson.node_monitors.ClockMonitor': None}, 'numExecutors': 1,
                             'offline': True, 'offlineCause': None, 'offlineCauseReason': '', 'oneOffExecutors': [],
                             'temporarilyOffline': False, 'absoluteRemotePath': None}], 'displayName': 'Nodes',
               'totalExecutors': 2}
