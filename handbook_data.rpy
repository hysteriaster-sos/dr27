## Handbook contents.
##
## Everything here is written by the school, not by the player. The player can
## read it and nothing else: no editing, no notes, no counters.
##
## Two students have entries because two students have been met in script.rpy.
## The other four have names on the register and nothing else, so their entries
## say so rather than inventing birthdays and talents.
##
## Portraits are cropped from the existing sprites by their alpha bounds, so
## they stay correct if the art is replaced with the same framing.
## Evidence shots are the project's own backgrounds at thumbnail size.

define hb_portrait_lythan = Transform("images/06_default.png", crop=(105, 43, 896, 1037), zoom=0.279)

define hb_portrait_ezra = Transform("images/05_default.png", crop=(1069, 51, 627, 1029), zoom=0.369)

define hb_students = [
    {
        "name": "Lythan",
        "initial": "L",
        "talent": "Ultimate Writer",
        "birthday": "Born 4 March",
        "portrait": hb_portrait_lythan,
        "paragraphs": [
            "Writes. Says he wants a book of his own in print before he leaves, and says it the way people describe something they have not started.",
            "Came through the gates on the first morning with one bag and a folded page of notes he did not show anyone. Eleven minutes passed between the gates and the classroom door, which is longer than the walk takes.",
            "Found in Classroom 4-B. He can describe the gates in detail. Everything between the gates and that room is missing.",
        ],
    },
    {
        "name": "Ezra",
        "initial": "E",
        "talent": "Talent unrecorded",
        "birthday": "Born 17 October",
        "portrait": hb_portrait_ezra,
        "paragraphs": [
            "Gave her name and stopped. Four minutes of nothing followed, and she spent them watching the door.",
            "Sits with her back to a wall. Counts the people who come into a room, and does it without turning her head.",
            "The handbook keeps a line for a talent. The line is empty, and nobody has asked her to fill it.",
        ],
    },
    {
        "name": "Kirsten",
        "initial": "K",
        "talent": "Talent unrecorded",
        "birthday": "Birthday not on file",
        "portrait": None,
        "paragraphs": [
            "Name on the register. Nothing recorded beyond the name.",
        ],
    },
    {
        "name": "Aster",
        "initial": "A",
        "talent": "Talent unrecorded",
        "birthday": "Birthday not on file",
        "portrait": None,
        "paragraphs": [
            "Name on the register. Nothing recorded beyond the name.",
        ],
    },
    {
        "name": "Zoe",
        "initial": "Z",
        "talent": "Talent unrecorded",
        "birthday": "Birthday not on file",
        "portrait": None,
        "paragraphs": [
            "Name on the register. Nothing recorded beyond the name.",
        ],
    },
    {
        "name": "Zach",
        "initial": "Z",
        "talent": "Talent unrecorded",
        "birthday": "Birthday not on file",
        "portrait": None,
        "paragraphs": [
            "Name on the register. Nothing recorded beyond the name.",
        ],
    },
]

define hb_evidence = [
    {
        "ref": "E-01",
        "title": "Gas ring, left open",
        "where": "Cookery room, chapter 1",
        "shot": Transform("images/cookeryroom_stove.png", zoom=0.0833),
        "body": "The rear ring on the range is lit at a quarter turn and there is no pan on it. The dial is worn smooth where a thumb would sit, and the wall behind the burner is warm to the back of the hand.",
    },
    {
        "ref": "E-02",
        "title": "Reagent shelf, third row",
        "where": "Chemistry lab, chapter 1",
        "shot": Transform("images/chemlab.png", zoom=0.0833),
        "body": "Eleven bottles and twelve labels. The gap sits on the third row, between the acetone and the distilled water. Clean patch on the shelf, a line of dust around it, and the bottle that should be there is not.",
    },
    {
        "ref": "E-03",
        "title": "Bench, wiped down",
        "where": "Chemistry lab, chapter 1",
        "shot": Transform("images/chemlab_table.png", zoom=0.0833),
        "body": "Only clean surface in the room. The cloth folded at the end of it is still damp. A beaker ring sits under the cloth, so the bench was cleaned while the beaker was still on it and the beaker was moved afterwards.",
    },
    {
        "ref": "E-04",
        "title": "Range hood, grease trail",
        "where": "Cookery room, chapter 1",
        "shot": Transform("images/cookeryroom.png", zoom=0.0833),
        "body": "Four fingers through the grease along the lower edge of the hood. The trail runs toward the door and stops at the third tile, where the floor has been washed and the grout has not dried.",
    },
    {
        "ref": "E-05",
        "title": "East gate, latch",
        "where": "School gates, chapter 1",
        "shot": Transform("images/schoolhall_entrance.png", zoom=0.0833),
        "body": "Latch down, gate shut. The bolt is bright along one edge, filed recently enough that the filings are still on the step. The gate was never locked. It was kept shut.",
    },
    {
        "ref": "E-06",
        "title": "Stage curtain, torn",
        "where": "Hall and stage, chapter 2",
        "shot": Transform("images/schoolhall_stage.png", zoom=0.0833),
        "body": "A tear two hands wide at shoulder height, edges frayed outward rather than cut. The curtain was pulled from behind. Whatever went through it did not come back the same way.",
    },
    {
        "ref": "E-07",
        "title": "The building, 04:12",
        "where": "East gate, chapter 2",
        "shot": Transform("images/school_corrupted.png", zoom=0.0833),
        "body": "Taken from the east gate at four in the morning. The roofline in the frame sits a storey higher than the roofline behind the camera. The longer you compare the two, the less they agree.",
    },
    {
        "ref": "E-08",
        "title": "Not yet logged",
        "where": "Hall and stage, chapter 2",
        "shot": None,
        "body": "",
    },
    {
        "ref": "E-09",
        "title": "Not yet logged",
        "where": "East wing, chapter 3",
        "shot": None,
        "body": "",
    },
]

define hb_rules = [
    {
        "number": "1",
        "text": "Students live on the school grounds for the whole term. The gates are shut at night and watched through the day. Nobody leaves before the last day, and the last day is set by the school.",
    },
    {
        "number": "2",
        "text": "Curfew is 22:00. Rooms are checked at 22:30. A bed with nobody in it is recorded as a missing student.",
    },
    {
        "number": "3",
        "text": "The cookery room and the laboratories are staff areas. A student found in either after hours is reported to the office, and the office decides what follows.",
    },
    {
        "number": "4",
        "text": "The east corridor is walked in twos after dark.",
    },
    {
        "number": "5",
        "text": "Damage to school property is repaired from the allowance of the student responsible. The school sets the cost of the repair.",
    },
    {
        "number": "6",
        "text": "The roof is out of bounds to all students at all hours.",
        "amendment": "Amended 4 November. The rooftop door is now padlocked. The rule did not change. The door did.",
    },
    {
        "number": "7",
        "text": "The handbook belongs to the school. Staff write the entries. A student may ask for a correction in writing and the office answers within the week.",
    },
    {
        "number": "8",
        "text": "A student who sees a rule broken reports it before the next meal.",
    },
    {
        "number": "9",
        "text": "At assembly, students answer to their talent before their name.",
    },
]

define hb_floors = [
    {
        "label": "Floor 4",
        "plan": Transform("images/p_f4_floorplan.png", zoom=0.30),
        "caption": "Classroom floor. Laboratories on the north side, staff rooms along the south corridor.",
        "rooms": [
            {"name": "Staff room", "note": "Six chairs and a kettle that is still warm. The noticeboard holds a timetable with one name inked out."},
            {"name": "Chemistry lab", "note": "Two rows of benches and eleven bottles on the shelf. The windows are painted over on the inside, which is not something the school does."},
            {"name": "Library", "note": "Chained from the corridor side. The librarian desk is in there, and so is the key."},
            {"name": "Classroom 4-B", "note": "Desks pushed back against the walls. Fourteen chairs for a class of six. The window opens a hand width and stops there."},
            {"name": "Stairwell A", "note": "The stairs turn at a half landing. Paint on the handrail is worn through where a lot of hands have held it."},
            {"name": "Faculty office", "note": "Locked, then unlocked. Two mugs on the desk, both cold, both still full."},
        ],
    },
    {
        "label": "Floor 5",
        "plan": Transform("images/p_f5_floorplan.png", zoom=0.30),
        "caption": "Cookery, the hall, and the rooms the school leaves off the tour.",
        "rooms": [
            {"name": "Cookery room", "note": "Ranges along the north wall, one of them lit. The fridge does not shut on its own and nobody has come to fix it."},
            {"name": "Hall and stage", "note": "Stage at the far end, curtain shut. Three hundred seats and no assembly called since term began."},
            {"name": "Storage", "note": "Shelves to the ceiling. The inventory by the door lists forty-one items and thirty-nine are there."},
            {"name": "Infirmary", "note": "Six beds, five made. The sixth has been slept in and left."},
            {"name": "Stairwell B", "note": "Same turn as Stairwell A. The half landing window looks out on the east wing instead of the gates."},
            {"name": "Roof access", "note": "One door, one padlock, one sign that repeats rule six. Nobody has been up there since term began."},
        ],
    },
    {
        "label": "Grounds",
        "plan": None,
        "caption": "Outside the main building. The gates are the only way off the site.",
        "rooms": [
            {"name": "School gates", "note": "Two piers, an iron gate, a gatehouse window with a light on. The bolt has been filed."},
            {"name": "Courtyard", "note": "Paving in a ring around a dry fountain. Six students could stand in it and not touch each other."},
            {"name": "East garden", "note": "Knot beds and a bench. The gravel has been raked into lines that do not follow the path."},
            {"name": "Gatehouse", "note": "One room, one window, one clock that runs four minutes slow."},
            {"name": "East wing", "note": "Bricked at the join with the main corridor. The brick is newer than the wall around it."},
            {"name": "Playing field", "note": "Marked out for a game that needs more players than the school has."},
        ],
    },
]
