import csv
import numpy
import glob

#preprocess information to create csv files with heatmap info
def preprocess(t, fre, filename):
    data = numpy.zeros((125, 125))
    
    for files in glob.glob("matches2/*.csv"):
        #print files 

        f = open(files, 'rt')

        try:
            reader = csv.reader(f)
            reader.next();
            openingData = numpy.zeros((125, 125))
            maxTime = 0;

            for row in reader:
                #entry = int(row[0])
                time = row[0]
                x = int(row[1])
                y = int(row[2])
                match = int(row[3])
                team = row[4]
                player = row[5]
                won = int(row[6])
                tstd = row[7]
                tsync = int(row[8])
                tper = row[9]
                tier = row[10]
                zone = row[11]
                #print row
                if tsync > maxTime:
                    maxTime = tsync
                
            opening = 0.1 * maxTime;
            #print opening
            f.seek(0);
            reader.next();
            for row in reader:
                x = int(row[1])
                y = int(row[2])
                tsync = int(row[8])
                won = int(row[6])
                team = row[4]
                if tsync < opening:
                    if won:
                        #if team == 'dire':
                        if team == t:
                            if fre == 1:
                                openingData[x][y] =openingData[x][y] + 1
                            else:
                                openingData[x][y] = 1
                        elif t == "":
                            if fre == 1:
                                openingData[x][y] =openingData[x][y] + 1
                            else:
                                openingData[x][y] = 1
                            #openingData[x][y] = 1
                        #openingData[x][y] =openingData[x][y] + 1
                        #openingData[x][y] = 1
                
            data = numpy.add(data, openingData)
            #print maxTime
            #print openingData.sum()

        finally:
            f.close()


    data = data / numpy.max(data)
    print numpy.max(data)
    size = 0
    for x in range(0, 125):
        for y in range(0, 125):
            if data[x][y] > 0:
                size = size + 1

    saveData = numpy.zeros(size, dtype='uint8, uint8, float64')
    index = 0
    for x in range(0, 125):
        for y in range(0, 125):
            if data[x][y] > 0:
                saveData[index][0] = x
                saveData[index][1] = y
                saveData[index][2] = data[x][y]
                index = index + 1



    #print data
            
    numpy.savetxt(filename, saveData,fmt='%i,%i,%.4f', header='x,y,heat', comments='')
    return

preprocess("", 0, "openings_heatmap.csv");
preprocess("", 1, "openings_heatmap2.csv");
preprocess("radiant", 0, "openings_heatmap_radiant.csv");
preprocess("radiant", 1, "openings_heatmap_radiant2.csv");
preprocess("dire", 0, "openings_heatmap_dire.csv");
preprocess("dire", 1, "openings_heatmap_dire2.csv");