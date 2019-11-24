from apistar import test

from iso_ne_ixq_app import app, PROJECT_NOT_FOUND, projects

client = test.TestClient(app)


def test_list_projects():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    car_count = len(projects)
    assert len(json_resp) == car_count

    expected = {"id": 0,
    "Pos.": 276,
    "Owner/Developer": "EDF Renewables Development, Inc.",
    "Project Name": "Homer Solar Energy Center",
    "(MW)": 90.0,
    "(MW).1": 90.0,
    "Fuel": "S",
    "County/State": "Cortland, NY",
    "Unnamed: 8": "C",
    "Point": "Cortland - Fenner 115kV",
    "Utility ": "NM-NG",
    "S": 9.0,
    "of Studies": "FES, SRIS"}
    assert json_resp[0] == expected

