from functools import partial
from typing import Any, MutableMapping, Optional

import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.state import WidgetCallback
from streamlit.type_util import Key, OptionSequence, T

from st_stateful.base import _on_change_factory


def _update_default(session: MutableMapping[Key, Any], key: str):
    session[f"{key}.default"] = session[key]


def stateful_multiselect(
    label: str,
    options: OptionSequence[T],
    key: str,
    default: Optional[Any] = None,
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
):
    """
    A stateful multiselect that preserves default selection.
    Can be reset to default state.
    """
    container = st.container()

    if f"{key}.options" not in session:
        session[f"{key}.options"] = options if options is not None else []

    if f"{key}.default" not in session:
        session[f"{key}.default"] = default if default is not None else []

    if st.button(
        "Reset",
        key=f"{key}.reset",
    ):
        del session[f"{key}.options"]
        del session[f"{key}.default"]
        st.rerun()

    with container:
        position.multiselect(
            label=f"{label} ({len(session[key]) if key in session else len(default) if default else 0}/{len(options)})",  # type: ignore
            options=session[f"{key}.options"],
            default=session[f"{key}.default"],
            key=key,
            on_change=_on_change_factory(partial(_update_default, session, key))(
                on_change
            ),
            **kwargs,
        )

        return session[f"{key}.default"]
