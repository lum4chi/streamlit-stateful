import streamlit as st
from typing import Any, MutableMapping
from streamlit.type_util import Key
from streamlit.delta_generator import DeltaGenerator


def stateful_expander(
    label: str,
    key: str,
    *args,
    expanded: bool = False,
    session: MutableMapping[Key, Any] = st.session_state,
    position: DeltaGenerator = st._main,
    **kwargs,
):
    """
    A stateful expander that preserves expanded status.
    """
    # TODO not working properly, miss a way to update expanded status when clicked
    if f"{key}.expanded" not in session:
        session[f"{key}.expanded"] = expanded

    return position.expander(
        label,
        *args,
        expanded=session[f"{key}.expanded"],
        **kwargs,
    )
