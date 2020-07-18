# PEng Use Case Implementation

This repository includes the use case implementations for our privacy component development that can be found [here](https://github.com/PEng2020-Subject3/faas-policy-provider). The functions provided are python modules that can be deployed as OpenFaaS functions, using either the normal OpenFaaS functionalities or the evironment that can be installed with our [faas-policy-provider](https://github.com/PEng2020-Subject3/faas-policy-provider).

Use cases covered with these functions are the following:

1. an insurance broker who wants to have a driver score calculated, 
1. an car manufacturer engineer who wants to receive performance data from the "real world",
1. a fleet manager who wants transparent information regarding his fleet performance.

## Function Descriptions

Basically, this repository encompasses four functions (i.e. python modules): two functions for database access and two functions for score calculations and output JSON packing (two functions for pseudonymous and personal data identifier input respectively). The functions are hierachically organized so that one has to call the driverscores.py or `performancescores.py` to get information implicitly supplied from the respective `indiv-...scores.py`. After having deployed both functions for e.g. driver score calculation, the `driverscores.py` calls the `indiv-driverscores.py` to get information required for output scores.

While the `driverscores.py` processes personal data, the `performancescores.py` processes pseudomized data. Hence, respective ID inputs differ accordingly.

## Getting Started

All four modules can be directly build, pushed and deployed as OpenFaaS functions. In order to deploy the functions, please execute the following steps:

1. Install the [faas-cli](https://docs.openfaas.com/cli/install/) 
1. Optionally install the [faas-policy-provider](https://github.com/PEng2020-Subject3/faas-policy-provider)
1. Configure the function .yml including database details
1. Build, push and deploy your function: `$ faas-cli up -g [YOUR GATEWAY URL HERE] -f [PATH TO YOUR FUNCTION YML]`

Now you can access the functions via the UI or URL using the following example inputs that can be found in the respective `handler.py` as well:

Example input and output for `driverscores.py`: `{"persID": 666, "function": "genDriverScore"}`, XXX.

Example input and output for `performancescores.py`: `{"typeID": "prius", "function": "genPerformanceScore"}`, XXX.

(Please note that you can only call driverscores or performancescores for data sets that acutally exist in the linked database.)
