# KubePilot

A command-line tool for interacting with Kubernetes clusters with a simple and efficient interface for performing common Kubernetes operations directly from the terminal.

## Features

- List pods in the active namespace
- List pods in a specific namespace
- List pods across all namespaces
- Automatically detect the active Kubernetes context and namespace

## Requirements

- Python 3.9+
- `kubectl` configured with access to your Kubernetes cluster

## Installation

Clone the repository:

```bash
git clone git@github.com:rakshithcodes/kubepilot.git
cd kubepilot
```

Install dependencies:

```bash
uv sync
```

## Usage

View help information:

```bash
uv run kubepilot --help
```

### List pods in the current namespace

```bash
kubepilot pods
```

### List pods in a specific namespace

```bash
kubepilot pods -n kube-system
```

### List pods across all namespaces

```bash
kubepilot pods -A
```

## Commands

- `kubepilot hello` - Hello message
- `kubepilot version` - Show version
- `kubepilot pods` - List Kubernetes pods

## Roadmap

- [ ] Pod listing (in progress)
- [ ] Events
- [ ] Logs
- [ ] Deployments

Services

Pod diagnostics