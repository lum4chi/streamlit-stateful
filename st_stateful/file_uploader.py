from functools import partial
from typing import Any, List, MutableMapping, Optional

import streamlit as st
from streamlit.type_util import Key
from streamlit.runtime.state import WidgetCallback
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.uploaded_file_manager import UploadedFile

from st_stateful.base import _on_change_factory


def _update_uploaded(session: MutableMapping[Key, Any], key: str):
    if key in session:
        session[f"{key}_uploaded"] = session[key]


def stateful_file_uploader(
    label: str,
    key: str,
    position: DeltaGenerator = st._main,
    session: MutableMapping[Key, Any] = st.session_state,
    on_change: Optional[WidgetCallback] = None,
    **kwargs,
) -> Optional[List[UploadedFile]]:
    """
    A stateful file uploader that preserves uploaded files.
    """
    # NOTE: even if files are preserved, widget does not show uploaded files controls to delete them.
    if f"{key}_uploaded" not in session:
        session[f"{key}_uploaded"] = None

    position.file_uploader(
        label=label,
        key=key,
        on_change=_on_change_factory(partial(_update_uploaded, session, key))(
            on_change
        ),
        **kwargs,
    )

    return session[f"{key}_uploaded"]
