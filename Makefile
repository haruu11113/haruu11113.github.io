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
publications:
	python3 scripts/rm2json.py $(JSONL)
	@echo "Run 'make hugo' to rebuild the site"
