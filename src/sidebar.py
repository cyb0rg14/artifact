import streamlit as st

stop_msg = "## STOP AND READ BELOW!!"
preinfo = """
You could tweak some values to generate more better articles, let's consider some examples so you could better understand it.
"""
example1 = " Dangers of excessive use of social media"
example2 = """
Dangers of excessive use of social media --kid\n
Dangers of excessive use of social media --adult\n
Dangers of excessive use of social media --athlete\n
Dangers of excessive use of social media --corporate worker\n
"""
example3 = """
Dangers of excessive use of social media --kid --300\n
Dangers of excessive use of social media --adult --500\n
"""
afterinfo = """
And you need to use parameters in order you can't use --300 before --kid
"""
contactInfo = """
## For any Queries:-
### You could connect with me on [LinkedIn](https://www.linkedin.com/in/cyb0rg14/) or could mail me [here](mailto:cyborgdomain@proton.me)
"""

examples = [example1, example2, example3]

def sidebar_conf():
    sidebar = st.sidebar
    sidebar.title("Artifact - A SEO friendly article generator bot")
    sidebar.divider()
    sidebar.markdown(stop_msg)
    sidebar.caption(preinfo)
    sidebar.markdown("* To simply generate a article")
    sidebar.info(examples[0])
    sidebar.markdown("* To generate articles about certain group like kids, adults, athletes, corporate workers")
    sidebar.info(examples[1])
    sidebar.markdown("* If you wanna keep it to certain words")
    sidebar.info(examples[2])
    sidebar.caption(afterinfo)
    sidebar.divider()
    sidebar.markdown(contactInfo)
    sidebar.markdown("# Made with ❤️ by cyb0rg14")

if __name__ == "__main__":
    sidebar_conf()
