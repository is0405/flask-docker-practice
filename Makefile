dcompose-build:
	docker-compose build

dcompose-up:
	docker-compose up

d-images-show:
	docker images

d-images-show-all:
	docker images -a

d-rm-images:
	docker rmi `docker images -a -q`

d-rm-container:
	docker rm `docker ps -a -q`
