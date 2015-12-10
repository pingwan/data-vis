import csv
import numpy
import glob

#preprocess matches-zones.csv to split matches into separate files
f = open("master-zones.csv", 'rt')
#f = open("matches/master-zones-1.csv", 'rt')
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
        bla = time +","+ x+"," + y+"," + match +"," + team+"," + player+"," + won+"," + tstd+"," + tsync+"," + tper+"," + tier+"," + zone+ "\n";
        if currentMatch == match:
            matchSize = matchSize +1;
            with open("matches2/"+ match + ".csv", "a") as myfile:
                myfile.write(bla)
                myfile.close();
        else:
            with open("matches2/" + match + ".csv", "w") as myfile:
                myfile.write(header)
                myfile.close();
                #myfile.write(row)
            with open("matches2/" + match + ".csv", "a") as myfile:
                #myfile.write(header)
                myfile.write(bla)
                myfile.close();
            totalMatches = totalMatches +1;
            record[currentMatch] = matchSize;
            currentMatch = match;

    #print record

finally:
    f.close()

print totalMatches
