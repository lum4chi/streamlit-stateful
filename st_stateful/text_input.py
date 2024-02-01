from functools import partial
from typing import Any, MutableMapping, Optional

import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.state import WidgetCallback
from streamlit.type_util import Key

from st_stateful.base import _on_change_factory


def _update_value(session: MutableMapping[Key, Any], key: str):
    session[f"{key}.value"] = session[key]


def stateful_text_input(
    label: str,
    key: str,
    value: str = "",
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
):
    """
    A stateful text_input that preserves value.
    """
    if f"{key}.value" not in session:
        session[f"{key}.value"] = value

    position.text_input(
        label=label,
        value=session[f"{key}.value"],
        key=key,
        on_change=_on_change_factory(partial(_update_value, session, key))(on_change),
        **kwargs,
    )

    return session[f"{key}.value"]
