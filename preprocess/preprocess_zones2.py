import csv
import numpy
import glob

#preprocess heatmap information to get the zone popularity
store = {}

f = open('DotaLabels.csv', 'rt')

try:
    reader = csv.reader(f)
    reader.next();

    zones = 0;
    zone = "";

    for row in reader:
        x = row[0]
        y = row[1]
        zone = row[2]
        value = int(row[3])
        #print zone
        store[x+','+y] = zone;
        #print store[row[2]]
        zones = zones + 1
    #print store
finally:
    f.close()
#print store

def popularity(filename, target):
    store2 = {};
    f = open(filename, 'rt')
    try:
        reader = csv.reader(f)
        reader.next();
        for row in reader: 
            x = row[0]
            y = row[1]
            heat = float(row[2])
            key = store[x+','+y]
            #print key
            try:
                store2[key] = store2[key] + heat
            except KeyError:
                store2[key] = heat
    finally:
        f.close()

    #print store2

    with open(target, "w") as myfile:
        myfile.write("zone,value\n")
        myfile.close();

    sumHeat = 0;
    for key, value in store2.iteritems() :
        sumHeat = sumHeat + value
    #print sumHeat

    for key, value in store2.iteritems() :
        store2[key] = (store2[key] / sumHeat)
    print store2

    #store2 = sorted(store2);

    for key, value in store2.iteritems() :
        with open(target, "a") as myfile:
            myfile.write(key + "," + str(value) + "\n")
            myfile.close();
        #print key, value
    return

popularity('heatmaps/openings_heatmap_radiant.csv', "heatmaps/radiant.csv");
popularity('heatmaps/openings_heatmap_radiant2.csv', "heatmaps/radiant2.csv");
popularity('heatmaps/openings_heatmap_dire.csv', "heatmaps/dire.csv");
popularity('heatmaps/openings_heatmap_dire2.csv', "heatmaps/dire2.csv");

