from kubernetes import client, config
def get_core_v1_api():
    config.load_kube_config()
    return client.CoreV1Api()