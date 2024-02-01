# Streamlit stateful widgets
Wrappers around streamlit widgets to hide state management.

Goal of this widget collection is to effortlessy use widgets that need stateful interaction, like:
- preserving a value while navigating the app and changing pages,
- variables set via session state are write-protected from streamlit, manual set avoid collisions with session state API
  and prevent errors like:  
  `StreamlitAPIException st.session_state.<var> cannot be modified after the widget with key <var> is instantiated.`
- solving clicking twice to make a setting [_stick_](https://docs.streamlit.io/knowledge-base/using-streamlit/widget-updating-session-state).

## 🚧 Work in progress! 🚧
This library is under development, so it's better to rely on commit id as version tracking!