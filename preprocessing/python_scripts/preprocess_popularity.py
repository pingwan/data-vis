import csv
import numpy
import glob
import os

#preprocess heatmap information to get the zone popularity
store = {}
os.chdir('..')
f = open('original_data/DotaLabels.csv', 'rt')

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
        store[x+','+y] = zone;
        zones = zones + 1
finally:
    f.close()


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
            try:
                store2[key] = store2[key] + heat
            except KeyError:
                store2[key] = heat
    finally:
        f.close()


    with open(target, "w") as myfile:
        myfile.write("zone,value\n")
        myfile.close();

    sumHeat = 0;
    for key, value in store2.iteritems() :
        sumHeat = sumHeat + value


    for key, value in store2.iteritems() :
        store2[key] = (store2[key] / sumHeat)
    print store2



    for key, value in store2.iteritems() :
        with open(target, "a") as myfile:
            myfile.write(key + "," + str(value) + "\n")
            myfile.close();
    return

popularity('heatmaps/openings_heatmap_radiant.csv', "popularity/radiant.csv");
popularity('heatmaps/openings_heatmap_radiant2.csv', "popularity/radiant2.csv");
popularity('heatmaps/openings_heatmap_dire.csv', "popularity/dire.csv");
popularity('heatmaps/openings_heatmap_dire2.csv', "popularity/dire2.csv");
popularity('heatmaps/openings_heatmap.csv', "popularity/both.csv");
popularity('heatmaps/openings_heatmap2.csv', "popularity/both2.csv");

popularity('heatmaps/openings_heatmap_radiant_all.csv', "popularity/radiant_all.csv");
popularity('heatmaps/openings_heatmap_radiant2_all.csv', "popularity/radiant2_all.csv");
popularity('heatmaps/openings_heatmap_dire_all.csv', "popularity/dire_all.csv");
popularity('heatmaps/openings_heatmap_dire2_all.csv', "popularity/dire2_all.csv");
popularity('heatmaps/openings_heatmap_all.csv', "popularity/both_all.csv");
popularity('heatmaps/openings_heatmap2_all.csv', "popularity/both2_all.csv");

popularity('heatmaps/openings_heatmap_radiant_lose.csv', "popularity/radiant_lose.csv");
popularity('heatmaps/openings_heatmap_radiant2_lose.csv', "popularity/radiant2_lose.csv");
popularity('heatmaps/openings_heatmap_dire_lose.csv', "popularity/dire_lose.csv");
popularity('heatmaps/openings_heatmap_dire2_lose.csv', "popularity/dire2_lose.csv");
popularity('heatmaps/openings_heatmap_lose.csv', "popularity/both_lose.csv");
popularity('heatmaps/openings_heatmap2_lose.csv', "popularity/both2_lose.csv");
