# Copyright 2017 Kensho Technologies, Inc.
"""The pytest plugin that calls out to PyAnnotate."""

import os
import sys
import typing


class PyAnnotatePlugin(object):
    """A pytest plugin that profiles function calls to extract type info."""

    def __init__(self, output_file):
        """Create a new PyAnnotatePlugin that analyzes function calls to extract type info."""
        from monkeytype.config import DefaultConfig
        from monkeytype.tracing import CallTracer

        os.environ[DefaultConfig.DB_PATH_VAR] = output_file
        self.tracer: typing.Optional[CallTracer] = None

    def pytest_collection_finish(self, session):
        """Handle the pytest collection finish hook: configure pyannotate.

        Explicitly delay importing `collect_types` until all tests have been collected. This
        gives gevent a chance to monkey patch the world before importing pyannotate.
        """
        from monkeytype.tracing import CallTracer
        from monkeytype.config import DefaultConfig

        config = DefaultConfig()
        tracer = CallTracer(
            logger=config.trace_logger(),
            code_filter=config.code_filter(),
            sample_rate=None,
        )
        self.tracer = tracer
        sys.setprofile(self.tracer)

    def pytest_unconfigure(self, config):
        """Unconfigure the pytest plugin. Happens when pytest is about to exit."""
        sys.setprofile(None)
        self.tracer.logger.flush()

    def pytest_runtest_call(self):
        """Handle the pytest hook event that a test is about to be run: start type collection."""
        sys.setprofile(self.tracer)

    def pytest_runtest_teardown(self):
        """Handle the pytest test end hook event: stop type collection."""
        sys.setprofile(None)
        self.tracer.logger.flush()


def pytest_addoption(parser):
    """Add our --analyze option to the pytest option parser."""
    parser.addoption(
        '--monkeytype-output',
        help='Output file where PyAnnotate stats should be saved.  Eg: "monkeytype.sqlite3"')


def pytest_configure(config):
    """Configure the plugin based on the supplied value for the  option."""
    option_value = config.getoption('--monkeytype-output')
    if option_value:
        base_path = os.path.abspath(option_value)
        config.pluginmanager.register(PyAnnotatePlugin(base_path))
