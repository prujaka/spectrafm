clean_png:
	@rm data/png/*

mp3_to_png:
	@python -m spectrafm.preprocessing
