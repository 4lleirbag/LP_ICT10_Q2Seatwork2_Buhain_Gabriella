from pyscript import document

def compute_average(event):
    filipino = float(document.getElementById("filipino").value)
    english = float(document.getElementById("english").value)
    math = float(document.getElementById("math").value)
    ict = float(document.getElementById("ict").value)
    science = float(document.getElementById("science").value)
    ss = float(document.getElementById("ss").value)
    
    document.getElementById("filipino_output").innerText = filipino
    document.getElementById("english_output").innerText = english
    document.getElementById("math_output").innerText = math
    document.getElementById("ict_output").innerText = ict
    document.getElementById("science_output").innerText = science
    document.getElementById("ss_output").innerText = ss

    total = filipino + english + math + ict +science + ss
    average = total / 6

    first = document.getElementById("first").value
    last = document.getElementById("last").value

    document.getElementById("name").innerText = f"Name: {first} {last}"
    document.getElementById("output").innerText = f"Your General Weighted Average is {round(average, 2)}"
    document.getElementById("grades_container").style.display = "block"