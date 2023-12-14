awscli-plugin-proxy
===================

This awscli plugin allows usage of proxy for AWS services as configured in profile configuration.

------------
Installation
------------

The easiest way to install awscli-plugin-proxy is to use `pip`:

    $ pip install awscli-plugin-proxy

You can also install the latest package from GitHub source which can contain changes not yet pushed to PyPI:

    $ pip install git+https://github.com/cyralinc/awscli-plugin-proxy.git

or, if you install `awscli` via Homebrew, which bundles its own python, install as following:

    $ /usr/local/opt/awscli/libexec/bin/pip install awscli-plugin-proxy


---------------
Getting Started
---------------

Before using awscli-plugin-proxy plugin, you need to [configure awscli](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) first.

**MUST**: Once that's done, to enable `awscli-plugin-proxy` plugin for S3, you can run:

    $ aws configure set plugins.s3-proxy awscli_plugin_proxy

The above command adds below section to your aws config file. You can also directly edit your `~/.aws/config` with below configuration.

    [plugins]
    s3-proxy = awscli_plugin_s3_proxy

To add proxy configure to a profile (assuming you have a **test** profile), you can run:

    $ aws configure --profile test set s3.proxy http://proxy-host.com:8080

The above command adds below section to your profile:

    [profile test]
	s3 =
		proxy = http://proxy-host.com:8080
	s3api =
		proxy = http://proxy-host.com:8080

Now you can access S3 using proxy with profile:

    $ aws s3 ls --profile test

If You want to use profile without passing it every time as parameter, use environment variable, ex:

    export AWS_PROFILE=test

Alternative (classic) method
----------------------------
You can follow the [guide by AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html) which describes how to use proxy using system environment variables. Here is the example:

    export http_proxy=http://proxy-host.com:8080
    export https_proxy=http://proxy-host.com:8080
    export HTTP_PROXY=http://proxy-host.com:8080
    export HTTPS_PROXY=http://proxy-host.com:8080

Remember that after setting these variables, `ALL` clients using this settings will be going through proxy!

Additionally, if You are using awscli on EC2 host, add `NO_PROXY` variable to allow awscli communicate with metadata endpoint:

    NO_PROXY=169.254.169.254
