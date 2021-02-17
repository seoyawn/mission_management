#!/usr/bin/env python

import rospy
import json

if __name__ == "__main__":
	rospy.init_node("test")
	
	a = {"mum": {"son": {"a": 1, "b": 2}, "daugter": {"c": 3, "d": 4}}, "dad": {"dson": {"e": 5, "f": 6}, "ddaughter": {"g": 7, "h": 8}}}
	
	k = a.keys()
	rospy.loginfo(k) #mum, dad

	v = a.values()
	rospy.loginfo(v) #daughter, son, dson, ddaughter
	
	i=0
	sk = a[k[i]].keys()
	rospy.loginfo(sk) #daughter, son --> mum

	sv = a[k[i]].values()
	rospy.loginfo(sv) #c,d,a,b --> mum
	rospy.loginfo(sk[i]) #daughter --> mum
	rospy.loginfo(sv[i]) #c, d --> mum; son
	
	svk = sv[i].keys()
	rospy.loginfo(svk)
				#keys
				k = ast.literal_eval(json.dumps(self.mission_dict.keys()))
				rospy.loginfo(k)  #New, Two, Seoyeon_Path
				rospy.loginfo(k[i])
		
				#values
				v = ast.literal_eval(json.dumps(self.mission_dict.values()))
				rospy.loginfo(v) #Second(x,y,w, task, pause), ...
				rospy.loginfo(len(v))

				#sub-keys
				sk = ast.literal_eval(json.dumps(self.mission_dict[k[i]].keys()))
				rospy.loginfo(sk) #Second, Third ...
				rospy.loginfo(len(sk))
	
				#sub-keys-values
				skv = ast.literal_eval(json.dumps(self.mission_dict[k[i]].values()))
				rospy.loginfo(skv)
				rospy.loginfo(skv[i]["x"])

				missionAllPose = MissionAll()
				missionAllPose.Mission_Name = k[i]

				#for i in range(len(
				missionAllPose.location = sk[i]	
				i+=1

	rospy.spin()
		




			#keys
			k = ast.literal_eval(json.dumps(self.mission_dict.keys())) #Seoyeon Path, Second Mission
			#values
			v = ast.literal_eval(json.dumps(self.mission_dict.values())) #{Second Point: xyw, First point: xyw}, {First..}

			dict_len = len(self.mission_dict[req.Mission_Name].keys())

			i=0
			self.sub_mission_dict.clear()
			for i in range(dict_len):

				#sub-keys
				sk = ast.literal_eval(json.dumps(self.mission_dict[req.Mission_Name].keys()))
				#sub-keys-values
				skv = ast.literal_eval(json.dumps(self.mission_dict[req.Mission_Name].values()))

				self.sub_mission_dict[sk[i]] = {"x": skv[n]["x"], "y": skv[n]["y"] , "w": skv[n]["w"], "task": skv[n]["task"], "pause time": skv[n]["pause time"]}
				self.dump_sub_mission_database(self.sub_mission_dict)
				rospy.loginfo(self.sub_mission_dict)
				i+=1









		if self.mission_dict == "":

			empty_array = [Invalid]
			return "No existing mission. Please add a mission.", empty_array

		else:
			mission_array = []

			i=0
			for k, v in self.mission_dict.items():

				rospy.loginfo(len(self.mission_dict.keys()))
	
				#keys
				k = ast.literal_eval(json.dumps(self.mission_dict.keys()))
				#values
				v = ast.literal_eval(json.dumps(self.mission_dict.values()))
				#sub-keys
				sk = ast.literal_eval(json.dumps(self.mission_dict[k[i]].keys()))
				#sub-keys-values
				skv = ast.literal_eval(json.dumps(self.mission_dict[k[i]].values()))

				missionAllPose = MissionAll()
				missionAllPose.Mission_Name = k[i]

				i+=1

				n=0
				for n in range(len(sk)):

					missionAllPose.location = sk[n]	
					missionAllPose.x = skv[n]["x"]		
					missionAllPose.y = skv[n]["y"]	
					missionAllPose.w = skv[n]["w"]		
					missionAllPose.task = skv[n]["task"]			
					missionAllPose.time = skv[n]["pause time"]
					n+=1
					mission_array.append(missionAllPose)	
					rospy.loginfo(mission_array)
		
			return "Successfully retrieved. Following are all the saved path: ", mission_array

