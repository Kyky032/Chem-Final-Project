from drafter import *
from dataclasses import dataclass
import random
from pathlib import Path

@dataclass
class State:
    score: int
    current_element: str
    logged_in: bool

# A dictionary of elements and their electron configurations
ELEMENTS = {
    "1s1": "Hydrogen",
    "1s2": "Helium",
    "1s2 2s1": "Lithium",
    "1s2 2s2": "Beryllium",
    "1s2 2s2 2p1": "Boron",
    "1s2 2s2 2p2": "Carbon",
    "1s2 2s2 2p3": "Nitrogen",
    "1s2 2s2 2p4": "Oxygen",
    "1s2 2s2 2p5": "Fluorine",
    "1s2 2s2 2p6": "Neon",
    "1s2 2s2 2p6 3s1": "Sodium",
    "1s2 2s2 2p6 3s2": "Magnesium",
    "1s2 2s2 2p6 3s2 3p1": "Aluminum",
    "1s2 2s2 2p6 3s2 3p2": "Silicon",
    "1s2 2s2 2p6 3s2 3p3": "Phosphorus",
    "1s2 2s2 2p6 3s2 3p4": "Sulfur",
    "1s2 2s2 2p6 3s2 3p5": "Chlorine",
    "1s2 2s2 2p6 3s2 3p6": "Argon",
    "1s2 2s2 2p6 3s2 3p6 4s1": "Potassium",
    "1s2 2s2 2p6 3s2 3p6 4s2": "Calcium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d1": "Scandium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d2": "Titanium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d3": "Vanadium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d4": "Chromium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d5": "Manganese",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d6": "Iron",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d7": "Cobalt",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d8": "Nickel",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d9": "Copper",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10": "Zinc",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1": "Gallium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2": "Germanium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3": "Arsenic",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4": "Selenium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5": "Bromine",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6": "Krypton",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1": "Rubidium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2": "Strontium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1": "Yttrium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2": "Zirconium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3": "Niobium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4": "Molybdenum",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5": "Technetium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d6": "Ruthenium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7": "Rhodium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8": "Palladium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d9": "Silver",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10": "Cadmium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1": "Indium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2": "Tin",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3": "Antimony",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4": "Tellurium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5": "Iodine",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6": "Xenon",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1": "Cesium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2": "Barium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f1": "Lanthanum",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f2": "Cerium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f3": "Praseodymium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f4": "Neodymium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f5": "Promethium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f6": "Samarium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f7": "Europium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f8": "Gadolinium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f9": "Terbium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f10": "Dysprosium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f11": "Holmium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f12": "Erbium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f13": "Thulium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f14": "Ytterbium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d2 4f14": "Lutetium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d3": "Hafnium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d4": "Tantalum",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d5": "Tungsten",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d6": "Rhenium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d7": "Osmium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d8": "Iridium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d9": "Platinum",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 5d10": "Gold",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10": "Mercury",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p1": "Thallium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p2": "Lead",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p3": "Bismuth",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p4": "Polonium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p5": "Astatine",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 6p6": "Radon",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 6d2 5f2": "Radium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f3": "Actinium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f4": "Thorium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f5": "Protactinium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f6": "Uranium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f7": "Neptunium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f8": "Plutonium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f9": "Americium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f10": "Curium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f11": "Berkelium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f12": "Californium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f13": "Einsteinium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 5f14": "Fermium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d1 5f14": "Mendelevium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d2 5f14": "Nobelium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d3 5f14": "Lawrencium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d4": "Rutherfordium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d5": "Dubnium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d6": "Seaborgium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d7": "Bohrium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d8": "Hassium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d9": "Meitnerium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10": "Darmstadtium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p1": "Roentgenium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p2": "Copernicium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p3": "Nihonium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p4": "Flerovium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p5": "Moscovium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p6": "Livermorium",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p7": "Tennessine",
    "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 7s2 6d10 7p8": "Oganesson"
}

# Helper function to select a random element's configuration
def generate_element() -> str:
    return random.choice(list(ELEMENTS.keys()))

@route
def index(state: State) -> Page:
    if not state.logged_in:
        return Page(state, [
            Header("Welcome to Electron Config Quiz!"),
            "Test your knowledge of electron configurations.",
            Button("Start the Quiz", login),
        ])
    else:
        return quiz_page(state)

@route
def login(state: State) -> Page:
    state.logged_in = True
    state.score = 0
    state.current_element = generate_element()
    return quiz_page(state)

@route
def quiz_page(state: State) -> Page:
    return Page(state, [
        Header("Identify the Element"),
        f"Electron Configuration: {state.current_element}",
        TextBox("answer", placeholder="Type the element name here"),
        Button("Submit Answer", check_answer),
        f"Current Score: {state.score}",
        Button("Restart Quiz", login)
    ])

@route
def check_answer(state: State, answer: str) -> Page:
    correct_answer = ELEMENTS[state.current_element]
    if answer.strip().lower() == correct_answer.lower():
        state.score += 1
        feedback = "Correct! Great job!"
    else:
        feedback = f"Wrong! The correct answer was: {correct_answer}."
    
    state.current_element = generate_element()  # Generate a new question
    return Page(state, [
        Header("Feedback"),
        feedback,
        Button("Next Question", quiz_page),
        f"Current Score: {state.score}",
        Button("Restart Quiz", login)
    ])

start_server(State(0, "", False))


