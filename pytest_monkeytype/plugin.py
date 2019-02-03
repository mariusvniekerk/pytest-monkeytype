# Copyright 2017 Kensho Technologies, Inc.
"""Enable MonkeyType tracing & logging to collect type info."""

import os
import sys

if False:
    from typing import Optional
    from monkeytype.tracing import CallTracer


class MonkeyTypePlugin(object):
    """Enable MonkeyType tracing & logging to collect type info."""
    """A pytest plugin that profiles function calls to extract type info."""

    def __init__(self):
        """Create a new PyAnnotatePlugin that analyzes function calls to extract type info."""

        """Initialize the plugin that profiles calls to extract type info."""
        from monkeytype.config import DefaultConfig

        self.config = DefaultConfig()
        self.trace_logger = self.config.trace_logger()
        self.tracer = None  # type: Optional[CallTracer]

    def pytest_collection_finish(self, session):
        """Configure MonkeyType and set as profiler after collection.

        Explicitly delay importing until all tests have been collected. This
        gives gevent a chance to monkey patch the world before importing
        CallTracer.
        """
        from monkeytype.tracing import CallTracer

        self.tracer = CallTracer(
            logger=self.trace_logger,
            code_filter=self.config.code_filter(),
            sample_rate=None,
        )
        sys.setprofile(self.tracer)

    def pytest_unconfigure(self, config):
        """Unconfigure by disabling profiling and flushing the logger."""
        sys.setprofile(None)
        self.trace_logger.flush()

    def pytest_runtest_call(self):
        """Start collection by installing the CallTracer as profiler."""
        sys.setprofile(self.tracer)

    def pytest_runtest_teardown(self):
        """Stop collection by disabling profiling and flushing the logger."""
        sys.setprofile(None)
        self.trace_logger.flush()


def pytest_addoption(parser):
    """Add our --monkeytype-output option to the pytest option parser."""
    parser.addoption(
        '--monkeytype-output',
        help='Output file where MonkeyType stats should be saved.  Eg: "monkeytype.sqlite3"')


def pytest_configure(config):
    """Enable and configure the output location."""
    option_value = config.getoption('--monkeytype-output')
    if option_value:
        os.environ['MT_DB_PATH'] = os.path.abspath(option_value)
        config.pluginmanager.register(MonkeyTypePlugin())
