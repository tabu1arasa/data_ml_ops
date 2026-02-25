import os

import dockerspawner
from traitlets.config.application import get_config

config = get_config()
config.JupyterHub.hub_ip = "0.0.0.0"
config.JupyterHub.hub_port = 8123
config.JupyterHub.hub_connect_ip = "jph"

config.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
config.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"
config.ConfigurableHTTPProxy.pid_file = "/data/jupyterhub-proxy.pid"

config.JupyterHub.admin_users = [os.environ["JPH_ADMIN_USER"]]
config.JupyterHub.authenticator_class = "dummy"
config.DummyAuthenticator.password = os.environ["JPH_DUMMY_PASSWORD"]

config.JupyterHub.spawner_class = dockerspawner.DockerSpawner

notebook_dir = os.getenv("DOCKER_NOTEBOOK_DIR", "/home/jovyan")
config.DockerSpawner.notebook_dir = notebook_dir
config.DockerSpawner.volumes = {"jupyter-user-{username}": notebook_dir}
config.DockerSpawner.environment = {
    "JPH_SINGLEUSER_JPHCONTENTS_ROOTDIR": "/home/jovyan",
}

config.DockerSpawner.use_internal_ip = True
config.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]

config.DockerSpawner.remove = True
config.DockerSpawner.debug = True
