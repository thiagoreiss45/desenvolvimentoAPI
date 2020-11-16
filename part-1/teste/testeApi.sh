#!/bin/bash

for counter in $(seq 0 600)
do
	if ! (($counter % 10));	then
		curl -XPOST http://127.0.0.1:5000/linx.com/products/ -d '[{"id": 0, "name":"mesa"}]'
		
	fi
	
  curl -X POST http://127.0.0.1:5000/linx.com/products/ -d '[{"id": '"$counter"', "name":"mesa"}]'
  sleep 1

done
