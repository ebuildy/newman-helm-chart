# Newman

From https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/:

> Newman is a command line Collection Runner for Postman. It allows you to run and test a Postman Collection directly from the command line.
> It is built with extensibility in mind so that you can easily integrate it with your continuous integration servers and build systems.

## Prerequisites

Kubernetes 1.14+

## values.yaml

* ``collection`` JSON encoded collection definition
* ``job``

## Get Repo Info

```console
helm repo add ebuildy https://ebuildy.github.io/newman-helm-chart
helm repo update
```

_See [helm repo](https://helm.sh/docs/helm/helm_repo/) for command documentation._

## Install Chart

```console
# Helm 3
$ helm install [RELEASE_NAME] ebuildy/newman

# Helm 2
$ helm install --name [RELEASE_NAME] ebuildy/newman
```

_See [configuration](#configuration) below._

_See [helm install](https://helm.sh/docs/helm/helm_install/) for command documentation._

## Uninstall Chart

```console
# Helm 3
$ helm uninstall [RELEASE_NAME]

# Helm 2
# helm delete --purge [RELEASE_NAME]
```

This removes all the Kubernetes components associated with the chart and deletes the release.

_See [helm uninstall](https://helm.sh/docs/helm/helm_uninstall/) for command documentation._

## Upgrading Chart

```console
# Helm 3 or 2
$ helm upgrade [RELEASE_NAME] [CHART] --install
```

_See [helm upgrade](https://helm.sh/docs/helm/helm_upgrade/) for command documentation._

## Configuration

See [Customizing the Chart Before Installing](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing). To see all configurable options with detailed comments, visit the chart's [values.yaml](./values.yaml), or run these configuration commands:

```console
# Helm 2
$ helm inspect values ebuildy/newman

# Helm 3
$ helm show values ebuildy/newman
```
