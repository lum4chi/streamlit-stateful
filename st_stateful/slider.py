from functools import partial
from typing import Any, MutableMapping, Optional

import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.elements.widgets.slider import SliderScalar, SliderValue
from streamlit.runtime.state import WidgetCallback
from streamlit.type_util import Key

from st_stateful.base import _on_change_factory


def _update_value(session: MutableMapping[Key, Any], key: str):
    session[f"{key}.value"] = session[key]


def stateful_slider(
    label: str,
    key: str,
    min_value: Optional[SliderScalar] = None,
    max_value: Optional[SliderScalar] = None,
    value: Optional[SliderValue] = None,
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
):
    """
    A stateful slider that preserves value selection.
    """
    if f"{key}.min_value" not in session:
        session[f"{key}.min_value"] = min_value

    if f"{key}.max_value" not in session:
        session[f"{key}.max_value"] = max_value

    if f"{key}.value" not in session:
        session[f"{key}.value"] = value

    position.slider(
        label=label,
        min_value=session[f"{key}.min_value"],
        max_value=session[f"{key}.max_value"],
        value=session[f"{key}.value"],
        key=key,
        on_change=_on_change_factory(partial(_update_value, session, key))(on_change),
        **kwargs,
    )

    return session[f"{key}.value"]
