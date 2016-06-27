import json
from pprint import pprint
from pygame import mixer

mixer.init()

with open('answers.json') as data_file:    
    data = json.load(data_file)

if __name__ == '__main__':
	while True:
		question_string = input("Ask me anything you want: \n");
		tags = question_string.split()
		similar = []
		for number in range(len(data["answers"])):
			similarity = 0
			for tag_answer in data["answers"][number]["tags"]:
				for tag_question in tags:
					if (tag_question == tag_answer):
						similarity +=1
			similar.append(similarity)
		print (max(similar))
		if (max(similar) == 0):
			print ("I don\'t know what to say")
		else:
			index = similar.index(max(similar))
			print ("I think answer " + data["answers"][index]["audio_name"])
			mixer.music.load("./"+data["answers"][index]["audio_files"][0])
			mixer.music.play()