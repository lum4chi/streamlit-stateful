# Streamlit stateful widgets
Wrappers around streamlit widgets to hide state management.

Goal of this widget collection is to effortlessy use widgets that need stateful interaction, like:
- preserving a value while navigating the app and changing pages;
- solving clicking twice to make a setting [_stick_](https://docs.streamlit.io/knowledge-base/using-streamlit/widget-updating-session-state);
- variables set via session state are write-protected from streamlit and duplicating it avoid collisions with session state API
  and prevent warning/errors like:  
    - `The widget with key "<your key>" was created with a default value but also had its value set via the Session State API.`
    - `StreamlitAPIException st.session_state.<var> cannot be modified after the widget with key <var> is instantiated.`

## 🚧 Work in progress! 🚧
This library is under development, please be aware that something can change!