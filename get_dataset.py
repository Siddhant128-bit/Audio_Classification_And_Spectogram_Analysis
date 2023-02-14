#Run this file it has combined preprocess portions on itself too 
import pre_process as pp
import os
import pandas as pd 


def convert_all(path):
    print('\nPre-Process 2/3\nGenerating Spectogram for all wav files')
    files_in_path=os.listdir(path)
    for files in files_in_path: 
        if files.endswith('.wav'):
            pp.graph_spectrogram(path+'\\'+files)
            

def get_path_and_convert_all_classes_to_spectograms():
    print('\nPre-Process 1/3')
    number_of_classes=int(input('Enter number of classes: '))
    total_paths=[]
    for i in range(1,number_of_classes+1):
        path_input=input('Enter path of '+str(i)+' class  dataset: ')
        total_paths.append(path_input)
        convert_all(path_input)
    return total_paths



def get_all_paths_convert_all_images_to_numpy_array(paths):
    print('\nPre-Process 3/3\nConverting all spectogram to single dataframe to dump as csv')
    data=[]
    label=[]
    dataset=pd.DataFrame(columns=['Data','Label'])
    for path in paths: 
        for file in os.listdir(path):
            if file.endswith('.png'):
                data.append(path+'\\'+file)
                label.append(path.split('\\')[-1])
    dataset['Data']=data
    dataset['Label']=label
    return dataset

def dump_to_folder(dataset):
    try:
        os.mkdir('Dataset_csv')
    except:
        pass

    dataset.to_csv('Dataset_csv\\dataset.csv',index=False)


if __name__=='__main__':
    all_paths=get_path_and_convert_all_classes_to_spectograms()
    dataset=get_all_paths_convert_all_images_to_numpy_array(all_paths)
    dataset=pp.label_encoding_dataframe(dataset)
    dump_to_folder(dataset)
    
