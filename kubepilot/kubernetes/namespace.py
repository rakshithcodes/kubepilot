from kubernetes import client, config
from kubernetes.config.kube_config import KUBE_CONFIG_DEFAULT_LOCATION
from kubepilot.kubernetes.client import get_core_v1_api

v1 = get_core_v1_api()

def get_current_namespace():
    contexts, active_context = config.list_kube_config_contexts()

    if active_context:
        namespace = active_context["context"].get("namespace")
        return namespace or "default"

    return "default"