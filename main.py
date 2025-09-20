from pyscript import when, display, document

@when("click", "#genbtn")
def generate_msg(event):
    name = document.querySelector("#name_input").value
    age = document.querySelector("#age_input").value
    school = document.querySelector("#school_input").value

    document.querySelector("#output").innerText = ""

    msg = f"""👤Student Information\n
    Name\t: {name}
    Age\t: {age}
    School\t: {school}
    
    ✏️ Notes: 
    {name} is {age} years old and studies at {school}
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """
    
    display(msg, target="#output")