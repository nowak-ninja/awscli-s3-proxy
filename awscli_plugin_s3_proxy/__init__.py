import os

PROXY = 'proxy'

def get_proxy_from_profile(profile, command):
    proxy = None
    if command in profile:
            if PROXY in profile[command]:
                proxy = profile[command][PROXY]
    return proxy

def set_proxy_from_profile(parsed_args, **kwargs):
    command = parsed_args.command
    session = kwargs['session']
    if parsed_args.profile:
        session.set_config_variable('profile', parsed_args.profile)
    service_proxy = get_proxy_from_profile(session.get_scoped_config(), command)
    if service_proxy is not None:
        print('Using S3 proxy: ' + service_proxy)
        os.environ["http_proxy"] = service_proxy
        os.environ["https_proxy"] = service_proxy
        os.environ["HTTP_PROXY"] = service_proxy
        os.environ["HTTPS_PROXY"] = service_proxy
        os.environ["NO_PROXY"] = "169.254.169.254"

def awscli_initialize(cli):
    cli.register('top-level-args-parsed', set_proxy_from_profile)
