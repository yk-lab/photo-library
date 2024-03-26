from logging import getLogger
import os

logger = getLogger(__name__)


def strtobool(val: str | None) -> bool:
    """文字列をbool値に変換する.

    Args:
        val (str | None): 変換する文字列

    Returns:
        bool: 変換後のbool値
    """
    if val is None:
        return False
    return val.lower() in ("yes", "true", "t", "1", "y", "on")


def strtoint(val: str | None, default: int | None = None) -> int | None:
    """文字列をint値に変換する.

    Args:
        val (str | None): 変換する文字列

    Returns:
        int | None: 変換後のint値
    """
    if val is None:
        return default
    try:
        return int(val)
    except ValueError as e:
        logger.error(e)
        return default


def strtofloat(val: str | None, default: float | None = None) -> float | None:
    """文字列をfloat値に変換する.

    Args:
        val (str | None): 変換する文字列

    Returns:
        float | None: 変換後のfloat値
    """
    if val is None:
        return default
    try:
        return float(val)
    except ValueError as e:
        logger.error(e)
        return default


def comma_separated_list(val: str | None) -> list[str]:
    """文字列をカンマ区切りのリストに変換する.

    Args:
        val (str | None): 変換する文字列

    Returns:
        list[str]: 変換後のリスト
    """
    if val is None:
        return []
    return [item for item in val.split(",") if item]


def env_bool(name: str, default: bool | None) -> bool | None:
    """環境変数をbool値に変換する.

    Args:
        name (str): 環境変数名
        default (bool): デフォルト値

    Returns:
        bool: 変換後のbool値
    """
    return strtobool(os.getenv(name, str(default)))


def env_float(name: str, default: float | None) -> float | None:
    """環境変数をfloat値に変換する.

    Args:
        name (str): 環境変数名
        default (float): デフォルト値

    Returns:
        float: 変換後のfloat値
    """
    return strtofloat(os.getenv(name), default)


def env_comma_separated_list(name: str) -> list[str]:
    """環境変数をカンマ区切りのリストに変換する.

    Args:
        name (str): 環境変数名

    Returns:
        list[str]: 変換後のリスト
    """
    return comma_separated_list(os.getenv(name))
