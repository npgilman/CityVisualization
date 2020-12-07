import CityGen
import json

#executor file to draw a specific state or all states
with open('states.json') as states:
    data = json.load(states)
    desiredState = input('Visualise: ')
    if (desiredState.lower() == 'all'):
        for (State, info) in data.items():
            CityGen.spawnState(State)
    else:
        CityGen.spawnState(desiredState)
