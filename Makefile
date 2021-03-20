init:
	hugo --cleanDestinationDir
	@hugo
hugo:
	hugo
server:
	hugo server
deploy:
	@hugo
	firebase deploy
