import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.elements.plotly_chart import FigureOrData


def stateful_plotly_chart(
    figure_or_data: FigureOrData,
    *args,
    position: DeltaGenerator = st._main,
    **kwargs,
):
    """
    A stateful plotly chart that preserves zooming.
    Source: https://github.com/streamlit/streamlit/issues/6324
    """
    figure_or_data.update_layout({"uirevision": "foo"}, overwrite=True)
    return position.plotly_chart(
        figure_or_data,
        *args,
        **kwargs,
    )
