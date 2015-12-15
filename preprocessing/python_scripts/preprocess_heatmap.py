import csv
import numpy
import glob
import os

#preprocess information to create csv files with heatmap info
def preprocess(t, fre, filename, win):
    data = numpy.zeros((125, 125))
    
    for files in glob.glob("master_zones/*.csv"):

        f = open(files, 'rt')

        try:
            reader = csv.reader(f)
            reader.next();
            openingData = numpy.zeros((125, 125))
            maxTime = 0;

            for row in reader:
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
                if tsync > maxTime:
                    maxTime = tsync
                
            opening = 0.1 * maxTime;
            f.seek(0);
            reader.next();
            for row in reader:
                x = int(row[1])
                y = int(row[2])
                tsync = int(row[8])
                won = int(row[6])
                team = row[4]
                if tsync < opening:
                    if won == 1 & win == 1:
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
                    elif won == 0 & win == 0:
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
                    elif win == 2:
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
            data = numpy.add(data, openingData)
        finally:
            f.close()


    data = data / numpy.max(data)

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
            
    numpy.savetxt(filename, saveData,fmt='%i,%i,%.4f', header='x,y,heat', comments='')
    return
	
os.chdir('..')
preprocess("", 0, "heatmaps/openings_heatmap_lose.csv", 0);
preprocess("", 1, "heatmaps/openings_heatmap2_lose.csv", 0);
preprocess("radiant", 0, "heatmaps/openings_heatmap_radiant_lose.csv", 0);
preprocess("radiant", 1, "heatmaps/openings_heatmap_radiant2_lose.csv", 0);
preprocess("dire", 0, "heatmaps/openings_heatmap_dire_lose.csv", 0);
preprocess("dire", 1, "heatmaps/openings_heatmap_dire2_lose.csv", 0);

preprocess("", 0, "heatmaps/openings_heatmap.csv", 1);
preprocess("", 1, "heatmaps/openings_heatmap2.csv", 1);
preprocess("radiant", 0, "heatmaps/openings_heatmap_radiant.csv", 1);
preprocess("radiant", 1, "heatmaps/openings_heatmap_radiant2.csv", 1);
preprocess("dire", 0, "heatmaps/openings_heatmap_dire.csv", 1);
preprocess("dire", 1, "heatmaps/openings_heatmap_dire2.csv", 1);

preprocess("", 0, "heatmaps/openings_heatmap_all.csv", 2);
preprocess("", 1, "heatmaps/openings_heatmap2_all.csv", 2);
preprocess("radiant", 0, "heatmaps/openings_heatmap_radiant_all.csv", 2);
preprocess("radiant", 1, "heatmaps/openings_heatmap_radiant2_all.csv", 2);
preprocess("dire", 0, "heatmaps/openings_heatmap_dire_all.csv", 2);
preprocess("dire", 1, "heatmaps/openings_heatmap_dire2_all.csv", 2);

