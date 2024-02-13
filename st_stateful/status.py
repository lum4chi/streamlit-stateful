import streamlit as st
from typing import Any, MutableMapping
from streamlit.type_util import Key
from streamlit.delta_generator import DeltaGenerator


def stateful_status(
    label: str,
    key: str,
    *args,
    expanded: bool = False,
    session: MutableMapping[Key, Any] = st.session_state,
    position: DeltaGenerator = st._main,
    **kwargs,
):
    """
    A stateful that preserves expanded status.
    """
    if f"{key}.expanded" not in session:
        session[f"{key}.expanded"] = expanded

    return position.status(
        label,
        *args,
        expanded=session[f"{key}.expanded"],
        **kwargs,
    )
