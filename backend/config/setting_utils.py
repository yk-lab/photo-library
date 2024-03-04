from logging import getLogger

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
