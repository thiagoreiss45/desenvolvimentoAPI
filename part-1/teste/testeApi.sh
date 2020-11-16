#!/bin/bash

for counter in $(seq 0 599)
do
	if ! (($counter % 10));	then
		curl -XPOST http://127.0.0.1:5000/linx.com/products/ -d '[{"id": 0, "name":"mesa"}]'

	fi
	sleep 1
  curl -X POST http://127.0.0.1:5000/linx.com/products/ -d '[{"id": '"$counter"', "name":"mesa"}]'

done
