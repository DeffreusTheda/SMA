#!/bin/bash

git add . && read -p "[Deffreus] Tell me briefly what you've changed: " GIT_MES && git commit -vsm "${GIT_MES}" && git push origin master
exit
