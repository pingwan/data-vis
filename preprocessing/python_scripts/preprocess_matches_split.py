import csv
import numpy
import glob
import os

#preprocess matches-zones.csv to split matches into separate files
os.chdir('..')
f = open("original_data/master-zones.csv", 'rt')
record = {};

try:
    reader = csv.reader(f)
    reader.next();
    header = "t,x,y,match,team,player,won,tstd,tsync,tper,tier,zone\n";
    currentMatch = "";
    matchSize = 0;
    totalMatches = 0;
    for row in reader:
        time = row[0]
        x = row[1]
        y = row[2]
        match = row[3]
        team = row[4]
        player = row[5]
        won = row[6]
        tstd = row[7]
        tsync = row[8]
        tper = row[9]
        tier = row[10]
        zone = row[11]
        entry = time +","+ x+"," + y+"," + match +"," + team+"," + player+"," + won+"," + tstd+"," + tsync+"," + tper+"," + tier+"," + zone+ "\n";
        if currentMatch == match:
            matchSize = matchSize +1;
            with open("master_zones/"+ match + ".csv", "a") as myfile:
                myfile.write(entry)
                myfile.close();
        else:
            with open("master_zones/" + match + ".csv", "w") as myfile:
                myfile.write(header)
                myfile.close();
            with open("master_zones/" + match + ".csv", "a") as myfile:
                myfile.write(entry)
                myfile.close();
            totalMatches = totalMatches +1;
            record[currentMatch] = matchSize;
            currentMatch = match;

finally:
    f.close()

print totalMatches
