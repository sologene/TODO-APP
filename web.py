import streamlit as st
import functions as f
todos = f.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    f.upd_todo(todos)


todos = f.get_todos()
st.title("My todo app")

for todo in todos:
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.remove(todo)
        f.upd_todo(todos)
        del st.session_state[todo]
        st.rerun()
st.session_state
st.text_input(label="Enter a todo", placeholder="Add a new Todo", on_change=add_todo,key='new_todo')
