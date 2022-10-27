# Configuration file for lab.

c = get_config()  # noqa

#------------------------------------------------------------------------------
# ServerApp(JupyterApp) configuration
#------------------------------------------------------------------------------
## Allow requests where the Host header doesn't point to a local server
#
#         By default, requests get a 403 forbidden response if the 'Host' header
#         shows that the browser thinks it's on a non-local domain.
#         Setting this option to True disables this check.
#
#         This protects against 'DNS rebinding' attacks, where a remote web server
#         serves you a page and then changes its DNS to send later requests to a
#         local IP, bypassing same-origin checks.
#
#         Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local,
#         along with hostnames configured in local_hostnames.
#  Default: False
c.ServerApp.allow_remote_access = True

## Whether to allow the user to run the server as root.
#  Default: False
c.ServerApp.allow_root = True

## The IP address the Jupyter server will listen on.
#  Default: 'localhost'
c.ServerApp.ip = '0.0.0.0'

## The port the server will listen on (env: JUPYTER_PORT).
#  Default: 0
c.ServerApp.port = 80

## The directory to use for notebooks and kernels.
#  Default: ''
c.ServerApp.root_dir = '/workspace'