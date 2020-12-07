import math, turtle, imgCnvrt
import csv, json

def spawnState(ActiveState):
    scale = 0
    refy = 0
    refx = 0
    state_ID = ''

    #get specific information to each state for a proper visualization of the cities
    with open('states.json') as states:
        data = json.load(states)
        desiredState = ActiveState
        for (State, info) in data.items():
            if (State == desiredState):
                state_ID = info['State_ID']
                refx = info['Long']
                refy = info['Lat']
                scale = info['Scale']

    #initialize turtle object and disable time delay
    city = turtle.Turtle()
    turtle.tracer(0,0)

    #visualize cities
    with open('uscities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #draw each city of the specified state
                if(row[2] == state_ID):
                    city.penup()
                    city.setpos((float(row[7])-refx)*scale, (float(row[6])-refy)*scale)
                    city.pendown()
                    city.dot(3)
                line_count += 1

    #save the visualization result to a jpg
    path = 'EPSres/' + state_ID + '.eps'
    turtle.getscreen().getcanvas().postscript(file=path)
    imgCnvrt.convert(path, 'PNGres/' + state_ID + '.png')
    turtle.Screen().clear()


