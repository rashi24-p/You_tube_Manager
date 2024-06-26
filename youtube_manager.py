import json


def load_data():
    try:
       with open('youtube.txt','r')as file:
           return json.load(file)
        #    print(type(test))
        
        
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w')as file:
        json.dump(videos,file)

def list_latest_videos(videos):
    print('\n')
    print('*'*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.Video Name : {video.get('name')} , Duration: {video.get('time')}")
    

def add_all_videos(videos):
    name = input('Enter the video name : ')
    time = input('Enter the video timing : ')
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_latest_videos(videos):
    list_latest_videos(videos)
    index = int(input('Enter the video number to update : '))
    if 1<=index<= len(videos):
        name = input('Enter the new video name : ')
        time = input('Enter the new video time : ')
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
        
    else:
        print('Invalid Index selected!')

def delete_the_videos(videos):
    list_latest_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('invalid choice!')

def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose the option ")
        print("1. list all the latest videos ")
        print("2. add all the videos ")
        print("3. update all the latest videos details")
        print("4. delete the videos ")
        print("5. Exit the APP")
        
        choice = input("Enter the chosed option : ")
        # print(videos)
        match choice:
            case "1":
                list_latest_videos(videos)
                
            case "2":
                add_all_videos(videos)
                
            case "3":
                update_latest_videos(videos)
                
            case "4":
                delete_the_videos(videos)
                
            case "5":
                break
            
            case _:
                print("Invalid Option!")
                
if __name__ == "__main__":
    main()
      
                