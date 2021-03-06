from distutils.version import Version
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, Text

from click.core import Command, Group, Argument, Option, Parameter, Context
from click.types import ParamType

_T = TypeVar('_T')
_Decorator = Callable[[_T], _T]

_Callback = Callable[
    [Context, Union[Option, Parameter], Union[bool, int, str]],
    Any
]

def pass_context(_T) -> _T:
    ...


def pass_obj(_T) -> _T:
    ...


def make_pass_decorator(
    object_type: type, ensure: bool = ...
) -> Callable[[_T], _T]:
    ...


# NOTE: Decorators below have **attrs converted to concrete constructor
# arguments from core.pyi to help with type checking.

def command(
    name: Optional[str] = ...,
    cls: type = Command,
    # Command
    context_settings: Optional[Dict] = ...,
    help: Optional[str] = ...,
    epilog: Optional[str] = ...,
    short_help: Optional[str] = ...,
    options_metavar: str = ...,
    add_help_option: bool = ...,
) -> _Decorator:
    ...


# This inherits attrs from Group, MultiCommand and Command.

def group(
    name: Optional[str] = ...,
    cls: type = Group,
    # Group
    commands: Optional[Dict[str, Command]] = None,
    # MultiCommand
    invoke_without_command: bool = ...,
    no_args_is_help: Optional[bool] = ...,
    subcommand_metavar: Optional[str] = ...,
    chain: bool = ...,
    result_callback: Optional[Callable] = ...,
    # Command
    help: Optional[str] = ...,
    epilog: Optional[str] = ...,
    short_help: Optional[str] = ...,
    options_metavar: str = ...,
    add_help_option: bool = ...,
    # User-defined
    **kwargs: Any,
) -> _Decorator:
    ...


def argument(
    *param_decls: str,
    cls: type = Argument,
    # Argument
    required: Optional[bool] = ...,
    # Parameter
    type: Optional[Union[type, ParamType]] = None,
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...


def option(
    *param_decls: str,
    cls: type = Option,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = False,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: Optional[bool] = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = None,
    help: Optional[str] = ...,
    # Parameter
    default: Optional[Any] = ...,
    required: bool = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...


# Defaults copied from the decorator body.
def confirmation_option(
    *param_decls: str,
    cls: type = Option,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = 'Do you want to continue?',
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = None,
    help: str = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...


# Defaults copied from the decorator body.
def password_option(
    *param_decls: str,
    cls: type = Option,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = True,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: Optional[bool] = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = None,
    help: Optional[str] = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...


# Defaults copied from the decorator body.
def version_option(
    version: Optional[Union[str, Version]] = None,
    *param_decls: str,
    cls: type = Option,
    # Option
    prog_name: Optional[str] = ...,
    show_default: bool = ...,
    prompt: Union[bool, Text] = False,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = None,
    help: str = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...


# Defaults copied from the decorator body.
def help_option(
    *param_decls: str,
    cls: type = Option,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = False,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = None,
    help: str = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = None
) -> _Decorator:
    ...
