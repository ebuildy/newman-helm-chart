import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../../../helpers"))
from helpers import helm_template

project = "newman"
helm_release_name = "release-name"
name = helm_release_name + "-" + project

def test_defaults():
    config = """
    """

    r = helm_template(config)

    assert name in r["job"]
    assert name in r["configmap"]

    assert "deployment" not in r
    assert "networkpolicy" not in r

    spec = r["job"][name]["spec"]
    container = spec["template"]["spec"]["containers"][0]

    assert 2 == spec["backoffLimit"]
    assert "newman" == container["name"]

    volume = spec["template"]["spec"]["volumes"][0]

    assert name == volume["configMap"]["name"]

def test_override_name():
    config = """
fullnameOverride: alicia
    """

    r = helm_template(config)

    assert "alicia" in r["job"]
    assert "alicia" in r["configmap"]

def test_networkpolicy():
    config = """
egress_rules:
- ports:
  - protocol: TCP
    port: 9200
  to:
  - podSelector:
      matchLabels:
        release: elasticsearch
    """

    r = helm_template(config)

    assert name in r["networkpolicy"]

    np = r["networkpolicy"][name]

    assert len(np["spec"]["egress"]) > 0
    assert "elasticsearch" == np["spec"]["egress"][0]["to"][0]["podSelector"]["matchLabels"]["release"]
    assert helm_release_name == np["spec"]["podSelector"]["matchLabels"]["app.kubernetes.io/instance"]

def test_extra_labels():
    config = """
labels:
  hello: world
    """

    r = helm_template(config)

    assert "world" == r["job"][name]["spec"]["template"]["metadata"]["labels"]["hello"]
