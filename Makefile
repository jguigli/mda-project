all:
	docker-compose up --build -d

up:
	docker-compose up --build

build:
	docker-compose build

logs:
	docker-compose logs -f

down:
	docker-compose down	

stop:
	docker-compose stop

start:
	docker-compose start

restart:
	docker-compose restart

clean:
	rm -rf $(shell docker-compose ps -q)

re: clean up

