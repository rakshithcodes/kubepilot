from kubernetes import client, config
from kubepilot.kubernetes.client import get_core_v1_api
from kubepilot.kubernetes.namespace import get_current_namespace


def list_pods(
    ns: str = None,
    all_namespaces: bool = False,
    ):
    v1 = get_core_v1_api()
    if all_namespaces:
        pods = v1.list_pod_for_all_namespaces()
    elif ns:
        pods = v1.list_namespaced_pod(namespace=ns)
    else:
        current_namespace = get_current_namespace()
        pods = v1.list_namespaced_pod(namespace=current_namespace)
    for pod in pods.items:
        print(f"{pod.metadata.namespace}\t{pod.metadata.name}")