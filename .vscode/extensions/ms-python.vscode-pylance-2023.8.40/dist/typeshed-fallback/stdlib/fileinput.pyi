import sys
from _typeshed import AnyStr_co, StrOrBytesPath
from collections.abc import Callable, Iterable, Iterator
from types import TracebackType
from typing import IO, Any, AnyStr, Generic, Protocol, overload
from typing_extensions import Literal, Self, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = [
    "input",
    "close",
    "nextfile",
    "filename",
    "lineno",
    "filelineno",
    "fileno",
    "isfirstline",
    "isstdin",
    "FileInput",
    "hook_compressed",
    "hook_encoded",
]

if sys.version_info >= (3, 11):
    _TextMode: TypeAlias = Literal["r"]
else:
    _TextMode: TypeAlias = Literal["r", "rU", "U"]

class _HasReadlineAndFileno(Protocol[AnyStr_co]):
    def readline(self) -> AnyStr_co: ...
    def fileno(self) -> int: ...

if sys.version_info >= (3, 10):
    # encoding and errors are added
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: _TextMode = "r",
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> FileInput[str]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: Literal["rb"],
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
        encoding: None = None,
        errors: None = None,
    ) -> FileInput[bytes]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: str,
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> FileInput[Any]: ...

elif sys.version_info >= (3, 8):
    # bufsize is dropped and mode and openhook become keyword-only
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: _TextMode = "r",
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
    ) -> FileInput[str]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: Literal["rb"],
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
    ) -> FileInput[bytes]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        *,
        mode: str,
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
    ) -> FileInput[Any]: ...

else:
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        bufsize: int = 0,
        mode: _TextMode = "r",
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
    ) -> FileInput[str]: ...
    # Because mode isn't keyword-only here yet, we need two overloads each for
    # the bytes case and the fallback case.
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        bufsize: int = 0,
        *,
        mode: Literal["rb"],
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
    ) -> FileInput[bytes]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None,
        inplace: bool,
        backup: str,
        bufsize: int,
        mode: Literal["rb"],
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
    ) -> FileInput[bytes]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
        inplace: bool = False,
        backup: str = "",
        bufsize: int = 0,
        *,
        mode: str,
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
    ) -> FileInput[Any]: ...
    @overload
    def input(
        files: StrOrBytesPath | Iterable[StrOrBytesPath] | None,
        inplace: bool,
        backup: str,
        bufsize: int,
        mode: str,
        openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
    ) -> FileInput[Any]: ...

def close() -> None: ...
def nextfile() -> None: ...
def filename() -> str: ...
def lineno() -> int: ...
def filelineno() -> int: ...
def fileno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...

class FileInput(Iterator[AnyStr], Generic[AnyStr]):
    if sys.version_info >= (3, 10):
        # encoding and errors are added
        @overload
        def __init__(
            self: FileInput[str],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: _TextMode = "r",
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
            encoding: str | None = None,
            errors: str | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[bytes],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: Literal["rb"],
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
            encoding: None = None,
            errors: None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[Any],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: str,
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
            encoding: str | None = None,
            errors: str | None = None,
        ) -> None: ...

    elif sys.version_info >= (3, 8):
        # bufsize is dropped and mode and openhook become keyword-only
        @overload
        def __init__(
            self: FileInput[str],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: _TextMode = "r",
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[bytes],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: Literal["rb"],
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[Any],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            *,
            mode: str,
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
        ) -> None: ...

    else:
        @overload
        def __init__(
            self: FileInput[str],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            bufsize: int = 0,
            mode: _TextMode = "r",
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[str]] | None = None,
        ) -> None: ...
        # Because mode isn't keyword-only here yet, we need two overloads each for
        # the bytes case and the fallback case.
        @overload
        def __init__(
            self: FileInput[bytes],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            bufsize: int = 0,
            *,
            mode: Literal["rb"],
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[bytes],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None,
            inplace: bool,
            backup: str,
            bufsize: int,
            mode: Literal["rb"],
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[bytes]] | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[Any],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None = None,
            inplace: bool = False,
            backup: str = "",
            bufsize: int = 0,
            *,
            mode: str,
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
        ) -> None: ...
        @overload
        def __init__(
            self: FileInput[Any],
            files: StrOrBytesPath | Iterable[StrOrBytesPath] | None,
            inplace: bool,
            backup: str,
            bufsize: int,
            mode: str,
            openhook: Callable[[StrOrBytesPath, str], _HasReadlineAndFileno[Any]] | None = None,
        ) -> None: ...

    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> AnyStr: ...
    if sys.version_info < (3, 11):
        def __getitem__(self, i: int) -> AnyStr: ...

    def nextfile(self) -> None: ...
    def readline(self) -> AnyStr: ...
    def filename(self) -> str: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

if sys.version_info >= (3, 10):
    def hook_compressed(
        filename: StrOrBytesPath, mode: str, *, encoding: str | None = None, errors: str | None = None
    ) -> IO[Any]: ...

else:
    def hook_compressed(filename: StrOrBytesPath, mode: str) -> IO[Any]: ...

def hook_encoded(encoding: str, errors: str | None = None) -> Callable[[StrOrBytesPath, str], IO[Any]]: ...
