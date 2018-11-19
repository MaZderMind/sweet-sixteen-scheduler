#!/bin/bash

if [ "$1" = "restart-on-device" ]; then
	echo "on device $(hostname), killing and restarting"

	pkill -f "^\./env/bin/python scheduler.py";
	./env/bin/python scheduler.py -vv 2>>/tmp/sweet-sixteen-scheduler >>/tmp/sweet-sixteen-scheduler &

elif [ "$1" = "sync-and-restart" ]; then
	echo "on host $(hostname), syncing and restarting"

	rsync -av \
		--exclude "/env" \
		--exclude "/.git" \
		--exclude "__pycache__" \
		--exclude "*.pyc" \
		--exclude "node_modules" \
		./ pi@sweet-sixteen.local:~/sweet-sixteen-scheduler/

	ssh pi@sweet-sixteen.local "cd ~/sweet-sixteen-scheduler/; ./rsync-and-restart-on-change.sh restart-on-device"

else

	echo "waiting for changes"
	# go get github.com/cespare/reflex
	reflex --regex='\.(py|js|ts|less|css|html|svg|ini)$$' --only-files -- bash -c "./rsync-and-restart-on-change.sh sync-and-restart"

fi
