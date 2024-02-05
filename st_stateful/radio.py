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


def stateful_radio(
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
    A stateful radio that preserves index selection.
    """
    # TODO Very similar to a selectbox, avoid repetition!

    if f"{key}.index" not in session:
        session[f"{key}.index"] = index

    index = session[f"{key}.index"] if 0 < session[f"{key}.index"] < len(options) else 0

    position.radio(
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
