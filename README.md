# PEng Use Case Implementation

This repository includes the use case implementations for our privacy component development that can be found 
[here](https://github.com/PEng2020-Subject3/faas-policy-provider). The functions provided are python modules that can
be deployed as OpenFaaS functions, using either the normal OpenFaaS functionalities or the environment that can be 
installed with our [faas-policy-provider](https://github.com/PEng2020-Subject3/faas-policy-provider).

Use cases covered with these functions are the following:

1. an insurance broker who wants to have a driver score calculated, 
2. a car manufacturer engineer who wants to receive performance data from the "real world",
3. a fleet manager who wants transparent information regarding his fleet performance.

## Function Descriptions

Basically, this repository encompasses four functions (i.e. python modules): 
two functions for database access and two functions for score calculations and output JSON packing
(two functions for pseudonymous and anonymous identifier input respectively). 
The functions are hierarchically organized so that one has to call the `driverscores.py` or `performancescores.py`
to get information implicitly supplied from the respective `indiv-...scores.py`. After having deployed both functions 
for e.g. driver score calculation, the `driverscores.py` calls the `indiv-driverscores.py` to get information required 
for output scores.

## Getting Started

All four modules can be directly build, pushed and deployed as OpenFaaS functions.
In order to deploy the functions, please execute the following steps:

1. Install the [faas-cli](https://docs.openfaas.com/cli/install/) 
2. Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
3. Install [helm](https://helm.sh/docs/intro/install/)
4. Optionally install the [faas-policy-provider](https://github.com/PEng2020-Subject3/faas-policy-provider)  
   or use a classic OpenFaaS installation
5. Install and configure a database
   ```bash
   helm repo add bitnami https://charts.bitnami.com/bitnami
   helm repo update
   helm install usecase-postgres-db bitnami/postgresql --set postgresqlPassword=3BDAJjFHOA -n openfaas-fn
   ```
6. Configure the function .yml including database details
7. Deploy a function: `$ faas-cli deploy -g [YOUR GATEWAY URL HERE] -f [PATH TO YOUR FUNCTION YML]`

Now you can access the functions via the UI or URL using the following example inputs that can be found in the respective `handler.py` as well:

Example input and output for `driverscores.py`: `{"sensor_ID": "666", "function": "genDriverScore"}`.

Example input and output for `performancescores.py`: `{"sensor_ID": "prius", "function": "genPerformanceScore"}`.

(Please note that you can only call driverscores or performancescores for data sets that actually exist in the linked database.)

## Development

To deploy new changes made to the code of a function, when using minikube for local development:
```bash
# set docker to use the minikube docker environment
eval $(minikube docker-env)
# Build the function image in minikubes docker
faas-cli build -f [PATH TO YOUR FUNCTION YML]
# deploy the function - if the provider `imagePullPolicy` is set to `IfNotPresent` in its values.yaml
faas-cli delploy -g [YOUR GATEWAY URL HERE] -f [PATH TO YOUR FUNCTION YML]
```
