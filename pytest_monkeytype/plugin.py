"""Enable MonkeyType tracing & logging to collect type info."""

import os
import sys
import typing


if typing.TYPE_CHECKING:
    from typing import Optional
    from monkeytype.tracing import CallTracer


class MonkeyTypePlugin(object):
    """Enable MonkeyType tracing & logging to collect type info.

    A pytest plugin that profiles function calls to extract type info.
    """

    def __init__(self, typed_dict_size=0):
        """Create a new PyAnnotatePlugin that analyzes function calls to extract type info.

        Initialize the plugin that profiles calls to extract type info.
        """
        from monkeytype.config import DefaultConfig

        self.typed_dict_size = typed_dict_size
        self.config = DefaultConfig()
        self.trace_logger = self.config.trace_logger()
        self.tracer: "Optional[CallTracer]" = None

    def pytest_collection_finish(self, session):
        """Configure MonkeyType and set as profiler after collection.

        Explicitly delay importing until all tests have been collected. This
        gives gevent a chance to monkey patch the world before importing
        CallTracer.
        """
        from monkeytype.tracing import CallTracer

        self.tracer = CallTracer(
            logger=self.trace_logger,
            max_typed_dict_size=self.typed_dict_size,
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
        "--monkeytype-output",
        help=(
            "Output file where MonkeyType stats should be saved.  Eg:"
            ' "monkeytype.sqlite3"'
        ),
    )
    parser.addoption(
        "--monkeytype-max-typed-dict-size",
        help=(
            "Maximum number of fields to include in generate TypedDict types"
        )
    )


def pytest_configure(config):
    """Enable and configure the output location."""
    option_value = config.getoption("--monkeytype-output")
    typed_dict_size = config.getoption("--monkeytype-max-typed-dict-size") or 0
    typed_dict_size = int(typed_dict_size)

    if option_value:
        os.environ["MT_DB_PATH"] = os.path.abspath(option_value)
        config.pluginmanager.register(MonkeyTypePlugin(typed_dict_size))
