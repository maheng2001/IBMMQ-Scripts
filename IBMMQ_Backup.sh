#!/bin/bash

DATE_FORMAT=`date "+%d%m%Y"`
MQADM_SCRIPT=/opt/mqm/bin
BACKUP_PATH=/var/mqm/MQ_backup/
QMLIST=`$MQADM_SCRIPT/dspmq | awk -F "(" '{print $2}' | cut -d ")" -f1`

for QM in $QMLIST;
	do QM_INST_NAME=`echo $QM | cut -d "." -f1`; 
	   echo "Backup start for "$QM;
		$MQADM_SCRIPT/dmpmqcfg -m $QM -a > $BACKUP_PATH/$QM_INST_NAME"_BACKUP_"$DATE_FORMAT.MQSC;
	done
