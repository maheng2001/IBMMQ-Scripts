#!/usr/bin/python
import re
Queue_New=raw_input('Enter the queue Name : ')
Queue_Attr_InputFile=open(r'/tmp/mq_queue1.mqsc', 'r')
Queue_Attr_ReadFile=Queue_Attr_InputFile.readlines()
Queue_Attr_InputFile.close()
for NewQueue in Queue_Attr_ReadFile:
	SplitQueueAttr=re.split('\(|\)' ,NewQueue)
	Dict=(SplitQueueAttr)
	print (Dict)
#	CheckLen = len(SplitQueueAttr)
#	if CheckLen == 1:
#		print "This is the Queue Atttr: {}".format(SplitQueueAttr[0])
#	else:
#		print  "This is the Queue Atttr: {}".format(SplitQueueAttr[0])
#		print  "And its value is  {}".format(SplitQueueAttr[1])
