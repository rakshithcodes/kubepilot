import typer
from typing import Annotated

NamespaceOption = Annotated[
    str | None,
    typer.Option("--namespace", "-n", help="Namespace")
]

AllNamespacesOption = Annotated[
    bool,
    typer.Option("--all-namespaces", "-A", help="All namespaces")
]