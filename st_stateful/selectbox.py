from functools import partial
from typing import Any, MutableMapping, Optional

import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.state import WidgetCallback
from streamlit.type_util import Key, OptionSequence, T

from st_stateful.base import _on_change_factory


def _update_index(
    session: MutableMapping[Key, Any], key: str, options: OptionSequence[T]
):
    session[f"{key}.index"] = options.index(session[key])


def stateful_selectbox(
    label: str,
    options: OptionSequence[T],
    key: str,
    index: int = 0,
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
):
    """
    A stateful selectbox that preserves index selection.
    """
    if f"{key}.index" not in session:
        session[f"{key}.index"] = index

    # Prevent the following when options are changed:
    # `streamlit.errors.StreamlitAPIException: Selectbox index must be between 0 and length of options`
    index = session[f"{key}.index"] if 0 < session[f"{key}.index"] < len(options) else 0

    position.selectbox(
        label=label,
        options=options,
        index=index,
        key=key,
        on_change=_on_change_factory(partial(_update_index, session, key, options))(
            on_change
        ),
        **kwargs,
    )

    return session[key]
