from contextlib import contextmanager

from .dependency_context import DependencyContext
from .dependency_registry import DependencyRegistry


def close_all_dependency_contexts():
    DependencyRegistry.reset()


def dependency(dep):
    context = DependencyRegistry.current_context()
    if context:
        return context.get(dep)
    return dep


@contextmanager
def dependency_context():
    context = open_dependency_context()
    yield context
    context.close()


def open_dependency_context():
    context = DependencyContext()
    DependencyRegistry.register(context)
    return context
