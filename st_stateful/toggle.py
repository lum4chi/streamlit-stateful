from functools import partial
import streamlit as st

from typing import Any, MutableMapping, Optional
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.state import WidgetCallback
from streamlit.type_util import Key

from st_stateful.base import _on_change_factory


def _update_value(session: MutableMapping[Key, Any], key: str):
    session[f"{key}.value"] = session[key]


def stateful_toggle(
    label: str,
    key: str,
    value: bool = False,
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
) -> bool:
    """
    A stateful toggle that preserves value.
    """
    # TODO Very similar to a checkbox, avoid repetition!

    if f"{key}.value" not in session:
        session[f"{key}.value"] = value

    position.toggle(
        label=label,
        value=session[f"{key}.value"],
        key=key,
        on_change=_on_change_factory(partial(_update_value, session, key))(on_change),
        **kwargs,
    )

    return session[f"{key}.value"]
