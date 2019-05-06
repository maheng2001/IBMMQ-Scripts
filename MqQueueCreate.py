#!/usr/bin/python
Queue_New=raw_input('Enter the queue Name : ')
Queue_Attr_InputFile=open(r'/tmp/mq_queue1.mqsc', 'r')
Queue_Attr_ReadFile=Queue_Attr_InputFile.readlines()
Queue_Attr_InputFile.close()
print Queue_New
for NewQueue in Queue_Attr_ReadFile:
        if "BOTHRESH" in NewQueue:
                print "Default backout Threshhold value is 0"
                BOTHRESH_Info=raw_input('Press Y to Contune or press C to change : ')

                if BOTHRESH_Info =="C":
                        BOTHRESH_NewValue=int(raw_input('Enter the New backout Threshhold value : '))
                        Queue_AttrIndex=Queue_Attr_ReadFile.index(NewQueue)
                        Queue_Attr_ReadFile[Queue_AttrIndex]='BOTHRESH(%s)'%BOTHRESH_NewValue
print Queue_Attr_ReadFile
