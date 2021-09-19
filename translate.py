import csv
import time
import tracemalloc

tracemalloc.start()
start_time = time.time()


source_file = open('t8.shakespeare.txt', 'r').read()
with open('output/frequency.csv','w',newline ='') as freq_dic:
    fieldnames = ['English word','French word','Frequency']
    csv_writer = csv.DictWriter(freq_dic,fieldnames=fieldnames)
    csv_writer.writeheader()


with open('french_dictionary.csv', 'r') as text_to_find:
    csv_reader = csv.reader(text_to_find)
    for line in csv_reader:
        freq = source_file.count(line[0])


        with open('output/frequency.csv','a',newline ='') as freq_dic:
            fieldnames = ['English word','French word','Frequency']
            csv_writer = csv.DictWriter(freq_dic,fieldnames=fieldnames)
            csv_writer.writerow({'English word':line[0],'French word':line[1],'Frequency':freq})

        if freq>0:
            source_file = source_file.replace(line[0],line[1])


    with open('output/t8.shakespeare.translated.txt','w') as file:
        file.write(source_file)


end_time = time.time()
time = round(end_time-start_time)
mem = tracemalloc.get_traced_memory()
mem = mem[1]/(1024*1024)
tracemalloc.stop()

with open('output/performance.txt','w') as per:
    per.write("Time to process: "+str(time//60)+" minutes "+ str(time%60) +" seconds\n")
    per.write("Memory used: "+ str(round(mem,2))+" MB")
