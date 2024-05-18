#!/bin/bash

PULL_RES="$(git fetch && git pull --rebase origin master 2>&1)"
echo $PULL_RES

if [[ $PULL_RES == *"You have unstaged changes."* ]]; then
	echo "[Deffreus] You need to execute Push.sh first, otherwise your changes might be deleted"
	read -p "[Deffreus] :3 Wanna let me do it for you? y/N: " IS_PUSH 
	if [[ $IS_PUSH == *[yY]* ]]; then
		echo "[Deffreus] Seems like that's a yes." && ./Push.sh
	elif [[ $IS_PUSH == *[^yYnN]* ]]; then
		echo "[Deffreus] I don't understand."
	fi
fi

exit
