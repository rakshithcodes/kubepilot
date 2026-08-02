import typer
from kubepilot.kubernetes.pods import list_pods
from kubepilot.options import NamespaceOption, AllNamespacesOption
app = typer.Typer()


@app.command()
def hello():
    print("Hello from KubePilot")


@app.command()
def version():
    print("0.1.0")

@app.command()
def pods(namespace: NamespaceOption = None, all_namespaces: AllNamespacesOption = False):
    list_pods(
        ns=namespace,
        all_namespaces=all_namespaces,
    )

if __name__ == "__main__":
    app()
