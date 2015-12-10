import csv
import numpy
import glob

#preprocess info from DotaLabels, and match csv's to get the team value and times
store = numpy.zeros((130, 130))
f = open('DotaLabels.csv', 'rt')

try:
    reader = csv.reader(f)
    reader.next();

    zones = 0;
    zone = "";

    for row in reader:
        x = int(row[0])
        y = int(row[1])
        zone = row[2]
        value = int(row[3])
        store[x][y] = row[3];
        #print store[row[2]]
        zones = zones + 1
    #print store


finally:
    f.close()
for files in glob.glob("matches2/*.csv"):
    f = open(files, 'rt')

    try:
        reader = csv.reader(f)
        reader.next();
        maxTime = 0;
        for row in reader:
            time = row[0]
            x = int(row[1])
            y = int(row[2])
            match = row[3]
            team = row[4]
            player = row[5]
            won = row[6]
            tstd = row[7]
            tsync = int(row[8])
            tper = row[9]
            tier = row[10]
            zone = row[11]
            if tsync > maxTime:
                    maxTime = tsync

        f.seek(0);
        reader.next();
        radiant = numpy.zeros((maxTime+1,3))
        dire = numpy.zeros((maxTime+1,3))

        match_id = "";
        for row in reader:
            time = row[0]
            x = int(row[1])
            y = int(row[2])
            match = row[3]
            match_id = match
            team = row[4]
            player = row[5]
            won = row[6]
            tstd = row[7]
            tsync = int(row[8])
            tper = row[9]
            tier = row[10]
            zone = row[11]
            #print [x, y]
            if team == "radiant":
                #radiant[tsync][0] = 'radiant'
                radiant[tsync][0] = 1
                radiant[tsync][1] = tsync
                radiant[tsync][2] = radiant[tsync][2] + store[x][y]

            else:
                dire[tsync][0] = 0
                dire[tsync][1] = tsync
                dire[tsync][2] = dire[tsync][2] + store[x][y]
        result = numpy.concatenate((radiant, dire), axis=0)
        filename = "matches_value/" + match_id + ".csv"
        print filename
        print result
        numpy.savetxt("matches_value/" + match_id + ".csv", result,fmt='%i,%i,%i', header='team,time,value', comments='')


    finally:
        f.close()